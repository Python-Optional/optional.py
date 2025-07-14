default:
    @just --list

test:
    @poetry run python -m pytest

lint:
    @poetry run python -m ruff check optional tests

format:
    @poetry run python -m ruff format optional tests

typecheck:
    @poetry run python -m mypy optional tests

editorconfig:
    @editorconfig-checker
