[private]
default:
    @just --list

# Run unit tests
test:
    @poetry run python -m pytest

# Lint code using ruff
lint:
    @poetry run python -m ruff check optional tests

# Format code using ruff
format:
    @poetry run python -m ruff format optional tests

# Check types using mypy
typecheck:
    @poetry run python -m mypy optional tests

# Check for editorconfig violations using editorconfig-checker
editorconfig:
    @editorconfig-checker
