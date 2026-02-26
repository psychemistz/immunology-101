"""Tests for Pydantic models."""

from __future__ import annotations

import pytest
from pydantic import ValidationError

from immunology101.models import (
    CourseManifest,
    Difficulty,
    Exercise,
    ExerciseResult,
    ExerciseType,
    Module,
    ModuleEntry,
    ModuleProgress,
    Reference,
    UserProgress,
)


class TestExercise:
    def test_multiple_choice_valid(self, mc_exercise):
        assert mc_exercise.type == ExerciseType.MULTIPLE_CHOICE
        assert mc_exercise.answer == "B"
        assert len(mc_exercise.choices) == 4

    def test_multiple_choice_requires_choices(self):
        with pytest.raises(ValidationError):
            Exercise(
                id="bad",
                type=ExerciseType.MULTIPLE_CHOICE,
                question="No choices?",
                answer="A",
                explanation="Oops.",
            )

    def test_matching_valid(self, matching_exercise):
        assert matching_exercise.type == ExerciseType.MATCHING
        assert len(matching_exercise.left_items) == 2

    def test_matching_requires_items(self):
        with pytest.raises(ValidationError):
            Exercise(
                id="bad",
                type=ExerciseType.MATCHING,
                question="No items?",
                answer={"a": "b"},
                explanation="Oops.",
            )

    def test_fill_in_blank(self, fill_exercise):
        assert fill_exercise.type == ExerciseType.FILL_IN_THE_BLANK
        assert fill_exercise.answer == "mitochondria"

    def test_ordering(self, ordering_exercise):
        assert ordering_exercise.type == ExerciseType.ORDERING
        assert len(ordering_exercise.answer) == 4

    def test_case_study(self, case_exercise):
        assert case_exercise.type == ExerciseType.CASE_STUDY
        assert isinstance(case_exercise.answer, list)

    def test_default_difficulty(self):
        ex = Exercise(
            id="default",
            type=ExerciseType.FILL_IN_THE_BLANK,
            question="Test?",
            answer="yes",
            explanation="Yes.",
        )
        assert ex.difficulty == Difficulty.MEDIUM


class TestReference:
    def test_reference(self):
        ref = Reference(title="Test", source="OpenStax", url="https://example.com")
        assert ref.license == "CC BY 4.0"


class TestModule:
    def test_module(self, sample_module):
        assert sample_module.id == "test_module"
        assert len(sample_module.exercises) == 2

    def test_empty_module(self):
        mod = Module(id="empty", title="Empty", description="Nothing", order=1)
        assert mod.exercises == []
        assert mod.prerequisites == []


class TestCourseManifest:
    def test_manifest(self):
        m = CourseManifest(
            title="Test Course",
            version="1.0",
            description="A test.",
            modules=[
                ModuleEntry(
                    id="m1", title="Mod 1", description="First", order=1, directory="m1"
                )
            ],
        )
        assert len(m.modules) == 1


class TestProgress:
    def test_module_progress_score(self):
        mp = ModuleProgress(
            module_id="test",
            exercise_results={
                "a": ExerciseResult(exercise_id="a", correct=True),
                "b": ExerciseResult(exercise_id="b", correct=False),
            },
        )
        assert mp.score == 50.0

    def test_module_progress_empty_score(self):
        mp = ModuleProgress(module_id="test")
        assert mp.score == 0.0

    def test_user_progress_unlock(self, sample_progress):
        # mod_b requires mod_a (which is completed)
        assert sample_progress.is_module_unlocked("mod_b", ["mod_a"])
        # mod_c requires mod_x (not completed)
        assert not sample_progress.is_module_unlocked("mod_c", ["mod_x"])
        # no prereqs
        assert sample_progress.is_module_unlocked("mod_d", [])

    def test_get_module_creates_new(self):
        up = UserProgress()
        mod = up.get_module("new_mod")
        assert mod.module_id == "new_mod"
        assert "new_mod" in up.modules
