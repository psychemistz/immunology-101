"""Pydantic models for course content, exercises, and progress."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field, model_validator

# ---------------------------------------------------------------------------
# Exercise types
# ---------------------------------------------------------------------------

class ExerciseType(str, Enum):
    MULTIPLE_CHOICE = "multiple_choice"
    MATCHING = "matching"
    FILL_IN_THE_BLANK = "fill_in_the_blank"
    ORDERING = "ordering"
    CASE_STUDY = "case_study"


class Difficulty(str, Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


# ---------------------------------------------------------------------------
# Exercise model
# ---------------------------------------------------------------------------

class Exercise(BaseModel):
    """A single exercise within a module."""

    id: str
    type: ExerciseType
    difficulty: Difficulty = Difficulty.MEDIUM
    question: str
    choices: list[str] | None = None  # multiple_choice, ordering
    left_items: list[str] | None = None  # matching
    right_items: list[str] | None = None  # matching
    answer: Any  # str, list[str], dict[str,str] depending on type
    hint: str | None = None
    explanation: str
    tags: list[str] = Field(default_factory=list)

    @model_validator(mode="after")
    def check_type_specific_fields(self) -> Exercise:
        if self.type == ExerciseType.MULTIPLE_CHOICE and not self.choices:
            raise ValueError("Multiple choice exercises require choices")
        if self.type == ExerciseType.MATCHING:
            if not self.left_items or not self.right_items:
                raise ValueError("Matching exercises require left_items and right_items")
        return self


# ---------------------------------------------------------------------------
# Reference model
# ---------------------------------------------------------------------------

class Reference(BaseModel):
    """A citation / learning resource."""

    title: str
    url: str | None = None
    source: str  # e.g. "OpenStax", "Frontiers"
    license: str = "CC BY 4.0"
    notes: str | None = None


# ---------------------------------------------------------------------------
# Module model
# ---------------------------------------------------------------------------

class Module(BaseModel):
    """A course module containing a lesson and exercises."""

    id: str
    title: str
    description: str
    order: int
    prerequisites: list[str] = Field(default_factory=list)
    lesson_content: str = ""  # markdown
    exercises: list[Exercise] = Field(default_factory=list)
    references: list[Reference] = Field(default_factory=list)


# ---------------------------------------------------------------------------
# Course manifest
# ---------------------------------------------------------------------------

class ModuleEntry(BaseModel):
    """Entry in the course manifest."""

    id: str
    title: str
    description: str
    order: int
    prerequisites: list[str] = Field(default_factory=list)
    directory: str


class CourseManifest(BaseModel):
    """Top-level course definition."""

    title: str
    version: str
    description: str
    modules: list[ModuleEntry]


# ---------------------------------------------------------------------------
# Progress models
# ---------------------------------------------------------------------------

class ExerciseResult(BaseModel):
    """Result of a single exercise attempt."""

    exercise_id: str
    correct: bool
    attempts: int = 1
    last_attempt: datetime = Field(default_factory=datetime.now)


class ModuleProgress(BaseModel):
    """Progress within a single module."""

    module_id: str
    lesson_read: bool = False
    exercise_results: dict[str, ExerciseResult] = Field(default_factory=dict)
    completed: bool = False
    started_at: datetime | None = None
    completed_at: datetime | None = None

    @property
    def score(self) -> float:
        if not self.exercise_results:
            return 0.0
        correct = sum(1 for r in self.exercise_results.values() if r.correct)
        return correct / len(self.exercise_results) * 100

    @property
    def exercises_done(self) -> int:
        return len(self.exercise_results)


class UserProgress(BaseModel):
    """Overall user progress across all modules."""

    modules: dict[str, ModuleProgress] = Field(default_factory=dict)
    current_streak: int = 0
    longest_streak: int = 0
    ai_questions_asked: int = 0
    last_active: datetime | None = None

    def is_module_unlocked(self, module_id: str, prerequisites: list[str]) -> bool:
        if not prerequisites:
            return True
        return all(
            self.modules.get(prereq, ModuleProgress(module_id=prereq)).completed
            for prereq in prerequisites
        )

    def get_module(self, module_id: str) -> ModuleProgress:
        if module_id not in self.modules:
            self.modules[module_id] = ModuleProgress(module_id=module_id)
        return self.modules[module_id]
