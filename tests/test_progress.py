"""Tests for progress persistence."""

from __future__ import annotations

from pathlib import Path

from immunology101.models import UserProgress
from immunology101.progress import (
    complete_module,
    load_progress,
    mark_lesson_read,
    record_exercise,
    reset_progress,
    save_progress,
)


class TestProgressPersistence:
    def test_save_and_load(self, tmp_progress_dir):
        prog = UserProgress()
        prog.current_streak = 5
        save_progress(prog, tmp_progress_dir)

        loaded = load_progress(tmp_progress_dir)
        assert loaded.current_streak == 5

    def test_load_nonexistent(self, tmp_progress_dir):
        prog = load_progress(tmp_progress_dir)
        assert prog.modules == {}

    def test_reset(self, tmp_progress_dir):
        prog = UserProgress()
        prog.current_streak = 3
        save_progress(prog, tmp_progress_dir)

        reset_progress(tmp_progress_dir)
        loaded = load_progress(tmp_progress_dir)
        assert loaded.current_streak == 0

    def test_reset_nonexistent(self, tmp_progress_dir):
        # Should not raise
        reset_progress(tmp_progress_dir)


class TestMarkLessonRead:
    def test_mark_read(self, tmp_progress_dir):
        prog = UserProgress()
        prog = mark_lesson_read(prog, "mod1", tmp_progress_dir)
        assert prog.modules["mod1"].lesson_read
        assert prog.modules["mod1"].started_at is not None
        assert prog.last_active is not None


class TestRecordExercise:
    def test_record_correct(self, tmp_progress_dir):
        prog = UserProgress()
        prog = record_exercise(prog, "mod1", "ex1", True, tmp_progress_dir)
        assert prog.modules["mod1"].exercise_results["ex1"].correct
        assert prog.current_streak == 1

    def test_record_incorrect(self, tmp_progress_dir):
        prog = UserProgress()
        prog = record_exercise(prog, "mod1", "ex1", False, tmp_progress_dir)
        assert not prog.modules["mod1"].exercise_results["ex1"].correct
        assert prog.current_streak == 0

    def test_streak(self, tmp_progress_dir):
        prog = UserProgress()
        prog = record_exercise(prog, "mod1", "ex1", True, tmp_progress_dir)
        prog = record_exercise(prog, "mod1", "ex2", True, tmp_progress_dir)
        assert prog.current_streak == 2
        assert prog.longest_streak == 2

        prog = record_exercise(prog, "mod1", "ex3", False, tmp_progress_dir)
        assert prog.current_streak == 0
        assert prog.longest_streak == 2

    def test_retry_updates_existing(self, tmp_progress_dir):
        prog = UserProgress()
        prog = record_exercise(prog, "mod1", "ex1", False, tmp_progress_dir)
        prog = record_exercise(prog, "mod1", "ex1", True, tmp_progress_dir)
        result = prog.modules["mod1"].exercise_results["ex1"]
        assert result.correct  # Updated to true
        assert result.attempts == 2


class TestCompleteModule:
    def test_complete(self, tmp_progress_dir):
        prog = UserProgress()
        prog = complete_module(prog, "mod1", tmp_progress_dir)
        assert prog.modules["mod1"].completed
        assert prog.modules["mod1"].completed_at is not None
