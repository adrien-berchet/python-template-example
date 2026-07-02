"""Module entry point for python-template-example."""

from .cli import main


def run(args: list[str] | None = None) -> None:
    """Run the command line interface."""
    main(args=args, prog_name="python-template-example")


if __name__ == "__main__":  # pragma: no cover
    run()
