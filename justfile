[default, private]
commands:
    @just --list

# Run unit tests
[group('test')]
test:
    @uv run python -m pytest

# Lint source code
[parallel, group('dev')]
lint: lint-ruff lint-basedpyright

# Lint code using ruff
[private, group('dev')]
lint-ruff:
    @uv run python -m ruff check src tests

# Lint code using basedpyright
[private, group('dev')]
lint-basedpyright:
    @uv run python -m basedpyright src tests

# Format code using ruff
[group('dev')]
format:
    @uv run python -m ruff format src tests

# Check for editorconfig violations using editorconfig-checker
[group('dev')]
editorconfig:
    @editorconfig-checker
