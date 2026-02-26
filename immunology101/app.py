"""Main interactive course loop."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, Optional

from immunology101 import ai
from immunology101.grader import grade
from immunology101.loader import load_all_modules
from immunology101.models import Exercise, ExerciseType, Module, UserProgress
from immunology101.progress import (
    complete_module,
    load_progress,
    mark_lesson_read,
    record_exercise,
    save_progress,
)
from immunology101.renderer import (
    console,
    render_ai_response,
    render_error,
    render_exercise,
    render_explanation,
    render_feedback,
    render_hint,
    render_info,
    render_lesson,
    render_module_complete,
    render_module_list,
    render_welcome,
)


def run_course(
    module_id: Optional[str] = None,
    content_dir: Optional[Path] = None,
    progress_dir: Optional[Path] = None,
) -> None:
    """Launch the interactive course."""
    modules = load_all_modules(content_dir)
    progress = load_progress(progress_dir)

    render_welcome()

    if module_id:
        target = next((m for m in modules if m.id == module_id), None)
        if not target:
            render_error(f"Module '{module_id}' not found.")
            return
        if not progress.is_module_unlocked(target.id, target.prerequisites):
            render_error(f"Module '{target.title}' is locked. Complete prerequisites first.")
            return
        _run_module(target, modules, progress, progress_dir)
    else:
        _run_all_modules(modules, progress, progress_dir)


def _run_all_modules(
    modules: List[Module],
    progress: UserProgress,
    progress_dir: Optional[Path],
) -> None:
    """Run through all unlocked modules sequentially."""
    for module in sorted(modules, key=lambda m: m.order):
        if not progress.is_module_unlocked(module.id, module.prerequisites):
            render_info(f"Module '{module.title}' is locked.")
            continue

        mod_prog = progress.modules.get(module.id)
        if mod_prog and mod_prog.completed:
            render_info(f"Module '{module.title}' already completed (score: {mod_prog.score:.0f}%).")
            answer = console.input("[dim]Redo this module? (y/N): [/dim]").strip().lower()
            if answer != "y":
                continue

        if not _run_module(module, modules, progress, progress_dir):
            break  # User quit


def _run_module(
    module: Module,
    all_modules: List[Module],
    progress: UserProgress,
    progress_dir: Optional[Path],
) -> bool:
    """Run a single module. Returns False if user quit."""
    render_info(f"\n{'='*60}")
    render_info(f"Module {module.order}: {module.title}")
    render_info(f"{'='*60}")

    # Lesson
    render_lesson(module.lesson_content)
    user_input = console.input().strip().lower()
    if user_input == "q":
        return False

    progress = mark_lesson_read(progress, module.id, progress_dir)

    # Exercises
    ai_available = ai.is_available()
    for i, exercise in enumerate(module.exercises, 1):
        result = _run_exercise(
            exercise, i, len(module.exercises), module, progress, ai_available, progress_dir
        )
        if result is None:  # User quit
            return False
        progress = result

    # Module completion
    mod_prog = progress.get_module(module.id)
    if mod_prog.exercises_done == len(module.exercises) and len(module.exercises) > 0:
        progress = complete_module(progress, module.id, progress_dir)
        render_module_complete(module, mod_prog.score)

    return True


def _run_exercise(
    exercise: Exercise,
    index: int,
    total: int,
    module: Module,
    progress: UserProgress,
    ai_available: bool,
    progress_dir: Optional[Path],
) -> Optional[UserProgress]:
    """Run a single exercise. Returns updated progress, or None if user quit."""
    render_exercise(exercise, index, total)

    while True:
        raw = console.input("[bold]> [/bold]").strip()
        if not raw:
            continue

        cmd = raw.lower()
        if cmd == "q":
            return None
        if cmd == "h":
            if exercise.hint:
                render_hint(exercise.hint)
            else:
                render_info("No hint available for this exercise.")
            continue
        if cmd == "s":
            render_info("Skipped.")
            render_explanation(exercise.explanation)
            progress = record_exercise(progress, module.id, exercise.id, False, progress_dir)
            break

        # Parse answer based on exercise type
        user_answer = _parse_answer(exercise, raw)
        if user_answer is None:
            render_error("Could not parse your answer. Please try again.")
            continue

        correct, feedback = grade(exercise, user_answer)
        render_feedback(correct, feedback)
        render_explanation(exercise.explanation)
        progress = record_exercise(progress, module.id, exercise.id, correct, progress_dir)

        # AI follow-up
        if ai_available:
            _handle_ai_followup(exercise, module, progress, progress_dir)
        break

    return progress


def _parse_answer(exercise: Exercise, raw: str) -> Any:
    """Parse raw user input into the appropriate answer type."""
    if exercise.type == ExerciseType.MULTIPLE_CHOICE:
        return raw

    if exercise.type == ExerciseType.FILL_IN_THE_BLANK:
        return raw

    if exercise.type == ExerciseType.CASE_STUDY:
        return raw

    if exercise.type == ExerciseType.MATCHING:
        return _parse_matching_answer(exercise, raw)

    if exercise.type == ExerciseType.ORDERING:
        return _parse_ordering_answer(exercise, raw)

    return raw


def _parse_matching_answer(exercise: Exercise, raw: str) -> Optional[Dict[str, str]]:
    """Parse matching answer like '1A,2C,3B,4D'."""
    left = exercise.left_items or []
    right = exercise.right_items or []
    result: Dict[str, str] = {}

    pairs = [p.strip() for p in raw.replace(" ", "").split(",")]
    for pair in pairs:
        if len(pair) < 2:
            return None
        try:
            num = int(pair[:-1]) - 1
            letter_idx = ord(pair[-1].upper()) - 65
        except (ValueError, IndexError):
            return None
        if 0 <= num < len(left) and 0 <= letter_idx < len(right):
            result[left[num]] = right[letter_idx]
        else:
            return None

    return result if result else None


def _parse_ordering_answer(exercise: Exercise, raw: str) -> Optional[List[str]]:
    """Parse ordering answer like '1,3,2,4,5,6'."""
    choices = exercise.choices or []
    try:
        indices = [int(x.strip()) - 1 for x in raw.split(",")]
    except ValueError:
        return None

    if any(i < 0 or i >= len(choices) for i in indices):
        return None

    return [choices[i] for i in indices]


def _handle_ai_followup(
    exercise: Exercise,
    module: Module,
    progress: UserProgress,
    progress_dir: Optional[Path],
) -> None:
    """Handle optional AI follow-up question after an exercise."""
    console.print("[dim]Ask a follow-up question (or press Enter to continue):[/dim]")
    question = console.input("[magenta]? [/magenta]").strip()
    if not question:
        return

    render_info("Thinking...")
    response = ai.ask_tutor(
        lesson_title=module.title,
        lesson_excerpt=module.lesson_content[:500],
        exercise_question=exercise.question,
        exercise_explanation=exercise.explanation,
        student_question=question,
    )
    if response:
        render_ai_response(response)
        progress.ai_questions_asked += 1
        save_progress(progress, progress_dir)
    else:
        render_error("AI tutor unavailable. Check your ANTHROPIC_API_KEY.")
