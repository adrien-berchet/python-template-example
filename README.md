[![CI](https://github.com/adrien-berchet/python-template-example/actions/workflows/ci.yml/badge.svg)](https://github.com/adrien-berchet/python-template-example/actions/workflows/ci.yml)
[![Coverage](https://codecov.io/gh/adrien-berchet/python-template-example/branch/main/graph/badge.svg)](https://codecov.io/gh/adrien-berchet/python-template-example)
[![PyPI](https://img.shields.io/pypi/v/python-template-example.svg)](https://pypi.org/project/python-template-example)
[![License](https://img.shields.io/github/license/adrien-berchet/python-template-example)](https://github.com/adrien-berchet/python-template-example/blob/main/LICENSE.txt)


# Python Template Example

A generated project used to validate the Copier template.

This is where you should write a short paragraph that explains what the package
does, how it is intended to be used, and why it exists.

Source | <https://github.com/adrien-berchet/python-template-example>
:--- | :---
Issues | <https://github.com/adrien-berchet/python-template-example/issues>
Documentation | <https://python-template-example.readthedocs.io>



## Installation

```bash
python3 -m pip install python-template-example
```

To install from the repository instead:

```bash
python3 -m pip install git+https://github.com/adrien-berchet/python-template-example.git
```

For local development, a `uv`-based workflow is recommended:

```bash
uv venv
source .venv/bin/activate
uv pip install --group dev --all-extras -e .
```

## Examples

Library usage:

```python
from python_template_example import __version__
from python_template_example.example import add

print(__version__)
print(add(1, 2))
```

CLI usage:

```bash
python-template-example --version
python-template-example -x 1 -y 2
```

<!-- README only content. Anything below this line won't be included in index.md -->

See https://python-template-example.readthedocs.io for more detailed documentation.
