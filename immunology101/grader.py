"""Answer evaluation for different exercise types."""

from __future__ import annotations

from typing import Any, Dict, List, Tuple

from thefuzz import fuzz

from immunology101.models import Exercise, ExerciseType

# Minimum fuzzy match ratio to accept a fill-in-the-blank answer
FUZZY_THRESHOLD = 75


def grade(exercise: Exercise, user_answer: Any) -> Tuple[bool, str]:
    """Grade a user's answer against an exercise.

    Returns (correct: bool, feedback: str).
    """
    graders = {
        ExerciseType.MULTIPLE_CHOICE: _grade_multiple_choice,
        ExerciseType.MATCHING: _grade_matching,
        ExerciseType.FILL_IN_THE_BLANK: _grade_fill_in_blank,
        ExerciseType.ORDERING: _grade_ordering,
        ExerciseType.CASE_STUDY: _grade_case_study,
    }
    grader_fn = graders[exercise.type]
    return grader_fn(exercise, user_answer)


def _grade_multiple_choice(exercise: Exercise, answer: str) -> Tuple[bool, str]:
    """Grade a multiple choice answer (e.g., 'A', 'B', 'C', 'D')."""
    normalized = answer.strip().upper()
    # Accept both "A" and "A)" formats
    if len(normalized) > 1 and normalized[1] == ")":
        normalized = normalized[0]

    correct_answer = str(exercise.answer).strip().upper()
    if len(correct_answer) > 1 and correct_answer[1] == ")":
        correct_answer = correct_answer[0]

    if normalized == correct_answer:
        return True, "Correct!"
    return False, f"Incorrect. The correct answer is {exercise.answer}."


def _grade_matching(exercise: Exercise, answer: Dict[str, str]) -> Tuple[bool, str]:
    """Grade a matching exercise. Answer is a dict mapping left→right."""
    correct_map: Dict[str, str] = exercise.answer
    if not isinstance(answer, dict):
        return False, "Please provide your answer as a mapping of left items to right items."

    wrong = []
    for left, expected_right in correct_map.items():
        user_right = answer.get(left, "")
        if fuzz.ratio(user_right.lower().strip(), expected_right.lower().strip()) < FUZZY_THRESHOLD:
            wrong.append(f"  {left} → {expected_right}")

    if not wrong:
        return True, "All matches correct!"
    return False, "Incorrect matches:\n" + "\n".join(wrong)


def _grade_fill_in_blank(exercise: Exercise, answer: str) -> Tuple[bool, str]:
    """Grade a fill-in-the-blank answer using fuzzy matching."""
    expected = str(exercise.answer).lower().strip()
    given = answer.lower().strip()

    # Exact match
    if given == expected:
        return True, "Correct!"

    # Fuzzy match
    ratio = fuzz.ratio(given, expected)
    if ratio >= FUZZY_THRESHOLD:
        return True, f"Correct! (accepted: '{exercise.answer}')"

    return False, f"Incorrect. The expected answer is: {exercise.answer}"


def _grade_ordering(exercise: Exercise, answer: List[str]) -> Tuple[bool, str]:
    """Grade an ordering exercise. Answer is a list of items in user's order."""
    correct_order: List[str] = exercise.answer
    if not isinstance(answer, list):
        return False, "Please provide your answer as an ordered list."

    if len(answer) != len(correct_order):
        return False, f"Expected {len(correct_order)} items, got {len(answer)}."

    wrong_positions = []
    for i, (user_item, correct_item) in enumerate(zip(answer, correct_order), 1):
        if fuzz.ratio(user_item.lower().strip(), correct_item.lower().strip()) < FUZZY_THRESHOLD:
            wrong_positions.append(i)

    if not wrong_positions:
        return True, "Correct order!"

    return False, (
        f"Incorrect. Positions {wrong_positions} are wrong.\n"
        f"Correct order:\n"
        + "\n".join(f"  {i}. {item}" for i, item in enumerate(correct_order, 1))
    )


def _grade_case_study(exercise: Exercise, answer: str) -> Tuple[bool, str]:
    """Grade a case study using keyword matching.

    The exercise.answer is a list of keywords. The user must mention
    enough of them to pass.
    """
    keywords: List[str] = exercise.answer
    if not isinstance(keywords, list):
        keywords = [str(keywords)]

    answer_lower = answer.lower()
    matched = [kw for kw in keywords if kw.lower() in answer_lower]
    match_ratio = len(matched) / len(keywords) if keywords else 0

    if match_ratio >= 0.5:
        return True, f"Good answer! Matched keywords: {', '.join(matched)}"
    return False, (
        f"Not quite. Your answer matched {len(matched)}/{len(keywords)} key concepts.\n"
        f"Key concepts to include: {', '.join(keywords)}"
    )
