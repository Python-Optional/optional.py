[private]
default:
    @just --list

# Run unit tests
test:
    @uv run python -m pytest

# Lint code using ruff
lint:
    @uv run python -m ruff check src tests

# Format code using ruff
format:
    @uv run python -m ruff format src tests

# Check types using mypy
typecheck:
    @uv run python -m mypy src tests

# Check for editorconfig violations using editorconfig-checker
editorconfig:
    @editorconfig-checker
