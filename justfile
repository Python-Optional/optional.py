[default, private]
commands:
    @just --list

# Run unit tests
test:
    @poetry run python -m pytest

# Lint source code
[parallel]
lint: lint-ruff lint-basedpyright

# Lint code using ruff
[private]
lint-ruff:
    @poetry run python -m ruff check optional tests

# Lint code using basedpyright
[private]
lint-basedpyright:
    @poetry run python -m basedpyright optional tests

# Format code using ruff
format:
    @poetry run python -m ruff format optional tests

# Check for editorconfig violations using editorconfig-checker
editorconfig:
    @editorconfig-checker
