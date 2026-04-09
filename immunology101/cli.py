"""Typer CLI for Immunology 101."""

from __future__ import annotations

import typer

from immunology101 import __version__

app = typer.Typer(
    name="imm101",
    help="Immunology 101 — Interactive terminal-based immunology course.",
    no_args_is_help=True,
)


@app.command()
def start(module: str | None = typer.Argument(None, help="Module ID to jump to")) -> None:
    """Launch the interactive course."""
    from immunology101.app import run_course

    run_course(module_id=module)


@app.command(name="list")
def list_modules() -> None:
    """List all modules and their status."""
    from immunology101.loader import load_all_modules
    from immunology101.progress import load_progress
    from immunology101.renderer import render_module_list

    modules = load_all_modules()
    progress = load_progress()
    render_module_list(modules, progress)


@app.command()
def progress() -> None:
    """Show your progress dashboard."""
    from immunology101.loader import load_all_modules
    from immunology101.progress import load_progress
    from immunology101.renderer import render_progress_dashboard

    modules = load_all_modules()
    prog = load_progress()
    render_progress_dashboard(prog, total_modules=len(modules))


@app.command()
def reset() -> None:
    """Reset all progress."""
    from immunology101.progress import reset_progress
    from immunology101.renderer import render_info

    confirm = typer.confirm("This will delete all saved progress. Continue?")
    if confirm:
        reset_progress()
        render_info("Progress reset.")
    else:
        render_info("Cancelled.")


@app.command()
def validate() -> None:
    """Validate course content files."""
    from immunology101.loader import validate_content
    from immunology101.renderer import console, render_error, render_info

    errors = validate_content()
    if errors:
        console.print(f"[bold red]Found {len(errors)} error(s):[/bold red]")
        for err in errors:
            render_error(err)
        raise typer.Exit(code=1)
    else:
        render_info("All content files are valid.")


@app.command()
def version() -> None:
    """Show version."""
    from immunology101.renderer import console

    console.print(f"immunology-101 v{__version__}")


if __name__ == "__main__":
    app()
