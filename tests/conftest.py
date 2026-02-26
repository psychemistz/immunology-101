"""Shared test fixtures."""

from __future__ import annotations

from pathlib import Path

import pytest

from immunology101.models import (
    Difficulty,
    Exercise,
    ExerciseType,
    Module,
    ModuleProgress,
    UserProgress,
)

CONTENT_DIR = Path(__file__).parent.parent / "immunology101" / "content"


@pytest.fixture
def content_dir() -> Path:
    return CONTENT_DIR


@pytest.fixture
def tmp_progress_dir(tmp_path: Path) -> Path:
    return tmp_path / "progress"


@pytest.fixture
def mc_exercise() -> Exercise:
    return Exercise(
        id="test_mc",
        type=ExerciseType.MULTIPLE_CHOICE,
        difficulty=Difficulty.EASY,
        question="What is 1+1?",
        choices=["A) 1", "B) 2", "C) 3", "D) 4"],
        answer="B",
        hint="It's even.",
        explanation="1+1=2.",
        tags=["math"],
    )


@pytest.fixture
def matching_exercise() -> Exercise:
    return Exercise(
        id="test_match",
        type=ExerciseType.MATCHING,
        difficulty=Difficulty.MEDIUM,
        question="Match items:",
        left_items=["Cat", "Dog"],
        right_items=["Meow", "Bark"],
        answer={"Cat": "Meow", "Dog": "Bark"},
        explanation="Cats meow, dogs bark.",
        tags=["animals"],
    )


@pytest.fixture
def fill_exercise() -> Exercise:
    return Exercise(
        id="test_fill",
        type=ExerciseType.FILL_IN_THE_BLANK,
        difficulty=Difficulty.MEDIUM,
        question="The powerhouse of the cell is the ____.",
        answer="mitochondria",
        explanation="Mitochondria produce ATP.",
        tags=["biology"],
    )


@pytest.fixture
def ordering_exercise() -> Exercise:
    return Exercise(
        id="test_order",
        type=ExerciseType.ORDERING,
        difficulty=Difficulty.MEDIUM,
        question="Order from smallest to largest:",
        choices=["Cell", "Organ", "Tissue", "Organism"],
        answer=["Cell", "Tissue", "Organ", "Organism"],
        explanation="Cell < Tissue < Organ < Organism.",
        tags=["biology"],
    )


@pytest.fixture
def case_exercise() -> Exercise:
    return Exercise(
        id="test_case",
        type=ExerciseType.CASE_STUDY,
        difficulty=Difficulty.HARD,
        question="Describe the cell.",
        answer=["membrane", "nucleus", "cytoplasm"],
        explanation="A cell has a membrane, nucleus, and cytoplasm.",
        tags=["biology"],
    )


@pytest.fixture
def sample_module(mc_exercise: Exercise, fill_exercise: Exercise) -> Module:
    return Module(
        id="test_module",
        title="Test Module",
        description="A test module.",
        order=1,
        lesson_content="# Test\nThis is a test lesson.",
        exercises=[mc_exercise, fill_exercise],
    )


@pytest.fixture
def sample_progress() -> UserProgress:
    return UserProgress(
        modules={
            "mod_a": ModuleProgress(module_id="mod_a", completed=True, lesson_read=True),
        }
    )
