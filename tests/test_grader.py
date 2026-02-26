"""Tests for answer grading."""

from __future__ import annotations

from immunology101.grader import grade


class TestMultipleChoice:
    def test_correct(self, mc_exercise):
        correct, _ = grade(mc_exercise, "B")
        assert correct

    def test_correct_lowercase(self, mc_exercise):
        correct, _ = grade(mc_exercise, "b")
        assert correct

    def test_correct_with_paren(self, mc_exercise):
        correct, _ = grade(mc_exercise, "B)")
        assert correct

    def test_incorrect(self, mc_exercise):
        correct, _ = grade(mc_exercise, "A")
        assert not correct


class TestMatching:
    def test_correct(self, matching_exercise):
        correct, _ = grade(matching_exercise, {"Cat": "Meow", "Dog": "Bark"})
        assert correct

    def test_incorrect(self, matching_exercise):
        correct, _ = grade(matching_exercise, {"Cat": "Bark", "Dog": "Meow"})
        assert not correct

    def test_invalid_input(self, matching_exercise):
        correct, _ = grade(matching_exercise, "not a dict")
        assert not correct


class TestFillInBlank:
    def test_exact(self, fill_exercise):
        correct, _ = grade(fill_exercise, "mitochondria")
        assert correct

    def test_case_insensitive(self, fill_exercise):
        correct, _ = grade(fill_exercise, "Mitochondria")
        assert correct

    def test_fuzzy(self, fill_exercise):
        correct, _ = grade(fill_exercise, "mitocondria")
        assert correct

    def test_wrong(self, fill_exercise):
        correct, _ = grade(fill_exercise, "ribosome")
        assert not correct


class TestOrdering:
    def test_correct(self, ordering_exercise):
        correct, _ = grade(
            ordering_exercise, ["Cell", "Tissue", "Organ", "Organism"]
        )
        assert correct

    def test_wrong_order(self, ordering_exercise):
        correct, _ = grade(
            ordering_exercise, ["Organism", "Organ", "Tissue", "Cell"]
        )
        assert not correct

    def test_wrong_count(self, ordering_exercise):
        correct, _ = grade(ordering_exercise, ["Cell"])
        assert not correct

    def test_invalid_input(self, ordering_exercise):
        correct, _ = grade(ordering_exercise, "not a list")
        assert not correct


class TestCaseStudy:
    def test_enough_keywords(self, case_exercise):
        correct, _ = grade(case_exercise, "The cell has a membrane and nucleus.")
        assert correct

    def test_not_enough_keywords(self, case_exercise):
        correct, _ = grade(case_exercise, "The cell is round.")
        assert not correct
