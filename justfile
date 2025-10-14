[default, private]
commands:
    @just --list

# Run unit tests
test:
    @uv run python -m pytest

# Lint source code
[parallel]
lint: lint-ruff lint-basedpyright

# Lint code using ruff
[private]
lint-ruff:
    @uv run python -m ruff check src tests

# Lint code using basedpyright
[private]
lint-basedpyright:
    @uv run python -m basedpyright src tests

# Format code using ruff
format:
    @uv run python -m ruff format src tests

# Check for editorconfig violations using editorconfig-checker
editorconfig:
    @editorconfig-checker
