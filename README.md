# py-starter

A minimal, modern Python starter: [uv](https://docs.astral.sh/uv/) for env + packaging,
[Ruff](https://docs.astral.sh/ruff/) for lint + format, `pytest` for tests, `mypy` (strict)
for types. `src/` layout.

## Requirements

- [uv](https://docs.astral.sh/uv/) (`.python-version` pins **3.14**; uv fetches it if needed)

## Setup

```bash
uv sync          # create .venv and install the project + dev tools
```

## Commands

| Command                      | What it does                          |
| ---------------------------- | ------------------------------------- |
| `uv run py-starter`          | Run the app (entry point)             |
| `uv run python -m py_starter`| Run the app via module                |
| `uv run pytest`              | Run tests                             |
| `uv run pytest --cov=py_starter` | Run tests with coverage           |
| `uv run mypy`                | Type-check (strict)                   |
| `uv run ruff check`          | Lint                                  |
| `uv run ruff check --fix`    | Lint and auto-fix                     |
| `uv run ruff format`         | Format                                |

## Layout

```
src/py_starter/
  __init__.py
  __main__.py      # entry point (python -m py_starter)
  math_utils.py    # example module
tests/
  test_math_utils.py
```
