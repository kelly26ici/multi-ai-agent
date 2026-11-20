"""Every lesson parses and imports at module level."""

# =========================================================================
# IMPORTS
# =========================================================================

import ast
import importlib.util
from pathlib import Path

LESSONS_DIR = Path(__file__).resolve().parents[1] / "lessons"


def test_lesson_files_exist() -> None:
    """The lessons directory holds the numbered files."""
    lessons = sorted(LESSONS_DIR.glob("*.py"))
    assert [p.name for p in lessons] == [
        "01_models.py",
        "02_tools.py",
        "03_middleware.py",
        "04_rag.py",
        "05_agents.py",
        "06_hitl.py",
        "07_memory.py",
        "08_evaluation.py",
    ]


def test_lessons_parse() -> None:
    """Every lesson compiles to valid Python."""
    for lesson in LESSONS_DIR.glob("*.py"):
        ast.parse(lesson.read_text(encoding="utf-8"), filename=str(lesson))


def test_lessons_import() -> None:
    """Every lesson's module-level code runs without side effects."""
    for lesson in LESSONS_DIR.glob("*.py"):
        spec = importlib.util.spec_from_file_location(lesson.stem, lesson)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
