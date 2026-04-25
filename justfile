[default, private]
commands:
    @just --list

# Run unit tests
[group('test')]
test:
    @pdm run python -m pytest

# Lint source code
[parallel, group('dev')]
lint: lint-ruff lint-basedpyright

# Lint code using ruff
[private, group('dev')]
lint-ruff:
    @pdm run python -m ruff check src tests

# Lint code using basedpyright
[private, group('dev')]
lint-basedpyright:
    @pdm run python -m basedpyright src tests

# Format code using ruff
[group('dev')]
format:
    @pdm run python -m ruff format src tests

# Check for editorconfig violations using editorconfig-checker
[group('dev')]
editorconfig:
    @editorconfig-checker
