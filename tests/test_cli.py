"""Tests for the python_template_example.cli module."""

from click.testing import CliRunner
from click.testing import Result
from pytest_console_scripts import RunResult
from pytest_console_scripts import ScriptRunner

import python_template_example.cli


def test_cli(cli_runner: CliRunner):
    """Test the CLI."""
    result: Result = cli_runner.invoke(
        python_template_example.cli.main,
        [
            "-x",
            "1",
            "-y",
            "2",
        ],
    )
    assert result.exit_code == 0
    assert result.output == "1 + 2 = 3\n"


def test_entry_point(script_runner: ScriptRunner):
    """Test the entry point."""
    ret: RunResult = script_runner.run(["python-template-example", "--version"])  # pyright: ignore
    assert ret.success
    assert ret.stdout.startswith("python-template-example, version ")
    assert ret.stderr == ""
