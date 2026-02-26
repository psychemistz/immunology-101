"""Tests for CLI commands."""

from __future__ import annotations

from typer.testing import CliRunner

from immunology101.cli import app

runner = CliRunner()


class TestCLI:
    def test_version(self):
        result = runner.invoke(app, ["version"])
        assert result.exit_code == 0
        assert "0.1.0" in result.output

    def test_validate(self):
        result = runner.invoke(app, ["validate"])
        assert result.exit_code == 0
        assert "valid" in result.output.lower()

    def test_list(self):
        result = runner.invoke(app, ["list"])
        assert result.exit_code == 0
        assert "Cells" in result.output

    def test_progress(self):
        result = runner.invoke(app, ["progress"])
        assert result.exit_code == 0
        assert "Progress" in result.output

    def test_reset_abort(self):
        result = runner.invoke(app, ["reset"], input="n\n")
        assert result.exit_code != 0 or "Cancelled" in result.output or "Aborted" in result.output

    def test_help(self):
        result = runner.invoke(app, ["--help"])
        assert result.exit_code == 0
        assert "Immunology 101" in result.output
