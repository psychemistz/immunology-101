"""Rich-based terminal UI rendering."""

from __future__ import annotations

from typing import Dict, List, Optional

from rich.columns import Columns
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from immunology101.models import Exercise, ExerciseType, Module, UserProgress

console = Console()


def render_welcome() -> None:
    """Display the course welcome banner."""
    console.print()
    console.print(
        Panel(
            "[bold cyan]Immunology 101[/bold cyan]\n"
            "[dim]Interactive immunology for bioinformaticians[/dim]\n\n"
            "Type [bold]q[/bold] to quit, [bold]h[/bold] for hint, "
            "[bold]s[/bold] to skip, [bold]?[/bold] for AI explanation",
            title="[bold]Welcome[/bold]",
            border_style="cyan",
            padding=(1, 2),
        )
    )
    console.print()


def render_lesson(content: str) -> None:
    """Render a lesson's markdown content."""
    console.print()
    console.print(Markdown(content))
    console.print()
    console.print("[dim]Press Enter to continue to exercises...[/dim]")


def render_module_list(modules: List[Module], progress: UserProgress) -> None:
    """Render a table of all modules with progress status."""
    table = Table(title="Course Modules", border_style="cyan")
    table.add_column("#", style="dim", width=4)
    table.add_column("Module", style="bold")
    table.add_column("Status", width=12)
    table.add_column("Score", width=8, justify="right")

    for mod in modules:
        mod_prog = progress.modules.get(mod.id)
        unlocked = progress.is_module_unlocked(mod.id, mod.prerequisites)

        if mod_prog and mod_prog.completed:
            status = "[green]Complete[/green]"
            score = f"{mod_prog.score:.0f}%"
        elif mod_prog and mod_prog.started_at:
            status = "[yellow]In Progress[/yellow]"
            score = f"{mod_prog.score:.0f}%"
        elif unlocked:
            status = "[blue]Available[/blue]"
            score = "—"
        else:
            status = "[dim]Locked[/dim]"
            score = "—"

        table.add_row(f"{mod.order:02d}", mod.title, status, score)

    console.print()
    console.print(table)
    console.print()


def render_progress_dashboard(progress: UserProgress, total_modules: int) -> None:
    """Render a progress dashboard."""
    completed = sum(1 for m in progress.modules.values() if m.completed)
    total_exercises = sum(m.exercises_done for m in progress.modules.values())
    total_correct = sum(
        sum(1 for r in m.exercise_results.values() if r.correct)
        for m in progress.modules.values()
    )

    table = Table(title="Your Progress", border_style="cyan", show_header=False)
    table.add_column("Metric", style="bold")
    table.add_column("Value", justify="right")

    table.add_row("Modules completed", f"{completed}/{total_modules}")
    table.add_row("Exercises answered", str(total_exercises))
    table.add_row("Correct answers", str(total_correct))
    table.add_row("Current streak", f"{progress.current_streak}")
    table.add_row("Longest streak", f"{progress.longest_streak}")
    table.add_row("AI questions asked", str(progress.ai_questions_asked))
    if progress.last_active:
        table.add_row("Last active", progress.last_active.strftime("%Y-%m-%d %H:%M"))

    console.print()
    console.print(table)
    console.print()


def render_exercise(exercise: Exercise, index: int, total: int) -> None:
    """Render an exercise prompt."""
    header = f"Exercise {index}/{total} — {exercise.type.value.replace('_', ' ').title()}"
    difficulty_color = {"easy": "green", "medium": "yellow", "hard": "red"}
    diff = f"[{difficulty_color[exercise.difficulty.value]}]{exercise.difficulty.value}[/]"

    console.print()
    console.print(Panel(f"[bold]{header}[/bold]  {diff}", border_style="yellow"))
    console.print()
    console.print(exercise.question)
    console.print()

    if exercise.type == ExerciseType.MULTIPLE_CHOICE and exercise.choices:
        for choice in exercise.choices:
            console.print(f"  {choice}")
        console.print()
        console.print("[dim]Enter your choice (e.g., A):[/dim]")

    elif exercise.type == ExerciseType.MATCHING:
        _render_matching_prompt(exercise)

    elif exercise.type == ExerciseType.FILL_IN_THE_BLANK:
        console.print("[dim]Type your answer:[/dim]")

    elif exercise.type == ExerciseType.ORDERING and exercise.choices:
        console.print("[dim]Items to order:[/dim]")
        for i, item in enumerate(exercise.choices, 1):
            console.print(f"  {i}. {item}")
        console.print()
        console.print("[dim]Enter the correct order as numbers (e.g., 3,1,4,2,5,6):[/dim]")

    elif exercise.type == ExerciseType.CASE_STUDY:
        console.print("[dim]Type your analysis:[/dim]")


def _render_matching_prompt(exercise: Exercise) -> None:
    """Render matching exercise items."""
    table = Table(show_header=True, border_style="dim")
    table.add_column("#", style="dim", width=3)
    table.add_column("Left (match FROM)", style="bold")
    table.add_column("#", style="dim", width=3)
    table.add_column("Right (match TO)")

    left = exercise.left_items or []
    right = exercise.right_items or []
    max_len = max(len(left), len(right))

    for i in range(max_len):
        l_num = str(i + 1) if i < len(left) else ""
        l_item = left[i] if i < len(left) else ""
        r_letter = chr(65 + i) if i < len(right) else ""
        r_item = right[i] if i < len(right) else ""
        table.add_row(l_num, l_item, r_letter, r_item)

    console.print(table)
    console.print()
    console.print("[dim]Enter matches as: 1A,2C,3B,4D[/dim]")


def render_feedback(correct: bool, feedback: str) -> None:
    """Render grading feedback."""
    if correct:
        console.print(Panel(f"[bold green]✓[/bold green] {feedback}", border_style="green"))
    else:
        console.print(Panel(f"[bold red]✗[/bold red] {feedback}", border_style="red"))


def render_explanation(explanation: str) -> None:
    """Render an exercise explanation."""
    console.print(Panel(explanation, title="[bold]Explanation[/bold]", border_style="blue"))


def render_hint(hint: str) -> None:
    """Render an exercise hint."""
    console.print(Panel(hint, title="[bold]Hint[/bold]", border_style="yellow"))


def render_ai_response(response: str) -> None:
    """Render an AI-generated response."""
    console.print()
    console.print(Panel(Markdown(response), title="[bold magenta]AI Tutor[/bold magenta]", border_style="magenta"))


def render_error(message: str) -> None:
    """Render an error message."""
    console.print(f"[bold red]Error:[/bold red] {message}")


def render_info(message: str) -> None:
    """Render an info message."""
    console.print(f"[cyan]{message}[/cyan]")


def render_module_complete(module: Module, score: float) -> None:
    """Render module completion summary."""
    console.print()
    console.print(
        Panel(
            f"[bold green]Module Complete![/bold green]\n\n"
            f"[bold]{module.title}[/bold]\n"
            f"Score: {score:.0f}%",
            border_style="green",
            padding=(1, 2),
        )
    )
    console.print()
