"""Load and validate course content from YAML/markdown files."""

from __future__ import annotations

from pathlib import Path
from typing import List

import yaml

from immunology101.models import (
    CourseManifest,
    Exercise,
    Module,
    ModuleEntry,
    Reference,
)

CONTENT_DIR = Path(__file__).parent / "content"


def _read_yaml(path: Path) -> dict:
    """Read and parse a YAML file."""
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def _read_text(path: Path) -> str:
    """Read a text file."""
    with open(path, encoding="utf-8") as f:
        return f.read()


def load_manifest(content_dir: Path | None = None) -> CourseManifest:
    """Load the course manifest from course.yaml."""
    content_dir = content_dir or CONTENT_DIR
    data = _read_yaml(content_dir / "course.yaml")
    return CourseManifest(**data)


def load_exercises(module_dir: Path) -> List[Exercise]:
    """Load exercises from a module's exercises.yaml."""
    path = module_dir / "exercises.yaml"
    if not path.exists():
        return []
    data = _read_yaml(path)
    return [Exercise(**ex) for ex in data.get("exercises", [])]


def load_references(module_dir: Path) -> List[Reference]:
    """Load references from a module's references.yaml."""
    path = module_dir / "references.yaml"
    if not path.exists():
        return []
    data = _read_yaml(path)
    return [Reference(**ref) for ref in data.get("references", [])]


def load_lesson(module_dir: Path) -> str:
    """Load lesson markdown content."""
    path = module_dir / "lesson.md"
    if not path.exists():
        return ""
    return _read_text(path)


def load_module(entry: ModuleEntry, content_dir: Path | None = None) -> Module:
    """Load a complete module from disk."""
    content_dir = content_dir or CONTENT_DIR
    module_dir = content_dir / entry.directory

    return Module(
        id=entry.id,
        title=entry.title,
        description=entry.description,
        order=entry.order,
        prerequisites=entry.prerequisites,
        lesson_content=load_lesson(module_dir),
        exercises=load_exercises(module_dir),
        references=load_references(module_dir),
    )


def load_all_modules(content_dir: Path | None = None) -> List[Module]:
    """Load all modules defined in the course manifest."""
    content_dir = content_dir or CONTENT_DIR
    manifest = load_manifest(content_dir)
    return [load_module(entry, content_dir) for entry in manifest.modules]


def validate_content(content_dir: Path | None = None) -> List[str]:
    """Validate all content files. Returns a list of error messages (empty = valid)."""
    content_dir = content_dir or CONTENT_DIR
    errors: List[str] = []

    # Check manifest
    manifest_path = content_dir / "course.yaml"
    if not manifest_path.exists():
        errors.append(f"Missing course manifest: {manifest_path}")
        return errors

    try:
        manifest = load_manifest(content_dir)
    except Exception as e:
        errors.append(f"Invalid course manifest: {e}")
        return errors

    # Check each module
    for entry in manifest.modules:
        module_dir = content_dir / entry.directory
        if not module_dir.exists():
            errors.append(f"Module directory missing: {module_dir}")
            continue

        if not (module_dir / "lesson.md").exists():
            errors.append(f"Missing lesson.md in {entry.id}")

        if not (module_dir / "exercises.yaml").exists():
            errors.append(f"Missing exercises.yaml in {entry.id}")
        else:
            try:
                exercises = load_exercises(module_dir)
                if not exercises:
                    errors.append(f"No exercises found in {entry.id}")
            except Exception as e:
                errors.append(f"Invalid exercises in {entry.id}: {e}")

        # references.yaml is optional but validate if present
        refs_path = module_dir / "references.yaml"
        if refs_path.exists():
            try:
                load_references(module_dir)
            except Exception as e:
                errors.append(f"Invalid references in {entry.id}: {e}")

    return errors
