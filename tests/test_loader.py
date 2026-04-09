"""Tests for content loader."""

from __future__ import annotations

from immunology101.loader import (
    load_all_modules,
    load_exercises,
    load_lesson,
    load_manifest,
    load_references,
    validate_content,
)


class TestLoadManifest:
    def test_load_manifest(self, content_dir):
        manifest = load_manifest(content_dir)
        assert manifest.title == "Immunology 101"
        assert len(manifest.modules) >= 1
        assert manifest.modules[0].id == "01_cells_of_immunity"

    def test_manifest_has_version(self, content_dir):
        manifest = load_manifest(content_dir)
        assert manifest.version == "0.1.0"


class TestLoadModule:
    def test_load_exercises(self, content_dir):
        module_dir = content_dir / "01_cells_of_immunity"
        exercises = load_exercises(module_dir)
        assert len(exercises) >= 6
        assert exercises[0].id == "01_mc_innate_vs_adaptive"

    def test_load_lesson(self, content_dir):
        module_dir = content_dir / "01_cells_of_immunity"
        content = load_lesson(module_dir)
        assert "Cells of the Immune System" in content

    def test_load_references(self, content_dir):
        module_dir = content_dir / "01_cells_of_immunity"
        refs = load_references(module_dir)
        assert len(refs) >= 1

    def test_missing_exercises(self, tmp_path):
        assert load_exercises(tmp_path) == []

    def test_missing_lesson(self, tmp_path):
        assert load_lesson(tmp_path) == ""


class TestLoadAllModules:
    def test_load_all(self, content_dir):
        modules = load_all_modules(content_dir)
        assert len(modules) >= 1
        mod = modules[0]
        assert mod.id == "01_cells_of_immunity"
        assert len(mod.exercises) >= 6
        assert mod.lesson_content != ""


class TestValidation:
    def test_valid_content(self, content_dir):
        errors = validate_content(content_dir)
        assert errors == []

    def test_missing_manifest(self, tmp_path):
        errors = validate_content(tmp_path)
        assert len(errors) == 1
        assert "Missing course manifest" in errors[0]
