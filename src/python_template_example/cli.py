"""Command Line Interface for the python_template_example package."""

import click

import python_template_example.example


@click.command("python-template-example")
@click.version_option()
@click.option(
    "-x",
    "--x_value",
    required=True,
    type=int,
    help="The value of X.",
)
@click.option(
    "-y",
    "--y_value",
    required=True,
    type=int,
    help="The value of Y.",
)
def main(x_value: int, y_value: int) -> None:
    """Add the values of X and Y."""
    click.echo(f"{x_value} + {y_value} = {python_template_example.example.add(x_value, y_value)}")
