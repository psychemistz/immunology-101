"""JSON-based progress persistence."""

from __future__ import annotations

import json
import os
from datetime import datetime
from pathlib import Path

from immunology101.models import ExerciseResult, UserProgress

DEFAULT_DIR = Path.home() / ".immunology101"
PROGRESS_FILE = "progress.json"


def _ensure_dir(progress_dir: Path) -> None:
    progress_dir.mkdir(parents=True, exist_ok=True)


def load_progress(progress_dir: Path | None = None) -> UserProgress:
    """Load user progress from disk."""
    progress_dir = progress_dir or DEFAULT_DIR
    path = progress_dir / PROGRESS_FILE
    if not path.exists():
        return UserProgress()
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    return UserProgress(**data)


def save_progress(progress: UserProgress, progress_dir: Path | None = None) -> None:
    """Save user progress to disk."""
    progress_dir = progress_dir or DEFAULT_DIR
    _ensure_dir(progress_dir)
    path = progress_dir / PROGRESS_FILE
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        json.dump(progress.model_dump(mode="json"), f, indent=2, default=str)


def reset_progress(progress_dir: Path | None = None) -> None:
    """Delete all saved progress."""
    progress_dir = progress_dir or DEFAULT_DIR
    path = progress_dir / PROGRESS_FILE
    if path.exists():
        path.unlink()


def mark_lesson_read(
    progress: UserProgress, module_id: str, progress_dir: Path | None = None
) -> UserProgress:
    """Mark a module's lesson as read."""
    mod = progress.get_module(module_id)
    mod.lesson_read = True
    if mod.started_at is None:
        mod.started_at = datetime.now()
    progress.last_active = datetime.now()
    save_progress(progress, progress_dir)
    return progress


def record_exercise(
    progress: UserProgress,
    module_id: str,
    exercise_id: str,
    correct: bool,
    progress_dir: Path | None = None,
) -> UserProgress:
    """Record an exercise attempt result."""
    mod = progress.get_module(module_id)
    if mod.started_at is None:
        mod.started_at = datetime.now()

    existing = mod.exercise_results.get(exercise_id)
    if existing:
        existing.correct = existing.correct or correct
        existing.attempts += 1
        existing.last_attempt = datetime.now()
    else:
        mod.exercise_results[exercise_id] = ExerciseResult(
            exercise_id=exercise_id, correct=correct
        )

    # Update streak
    if correct:
        progress.current_streak += 1
        progress.longest_streak = max(progress.longest_streak, progress.current_streak)
    else:
        progress.current_streak = 0

    progress.last_active = datetime.now()
    save_progress(progress, progress_dir)
    return progress


def complete_module(
    progress: UserProgress, module_id: str, progress_dir: Path | None = None
) -> UserProgress:
    """Mark a module as completed."""
    mod = progress.get_module(module_id)
    mod.completed = True
    mod.completed_at = datetime.now()
    progress.last_active = datetime.now()
    save_progress(progress, progress_dir)
    return progress
