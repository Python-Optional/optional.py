# Optional.py

[![Build Status](https://img.shields.io/pypi/v/optional.py.svg)](https://pypi.org/project/optional.py/)
[![test](https://github.com/Python-Optional/optional.py/actions/workflows/test.yaml/badge.svg)](https://github.com/Python-Optional/optional.py/actions/workflows/test.yaml)
[![lint](https://github.com/Python-Optional/optional.py/actions/workflows/lint.yaml/badge.svg)](https://github.com/Python-Optional/optional.py/actions/workflows/lint.yaml)
[![typecheck](https://github.com/Python-Optional/optional.py/actions/workflows/typecheck.yaml/badge.svg)](https://github.com/Python-Optional/optional.py/actions/workflows/typecheck.yaml)
[![format](https://github.com/Python-Optional/optional.py/actions/workflows/format.yaml/badge.svg)](https://github.com/Python-Optional/optional.py/actions/workflows/format.yaml)
[![editorconfig](https://github.com/Python-Optional/optional.py/actions/workflows/editorconfig.yaml/badge.svg)](https://github.com/Python-Optional/optional.py/actions/workflows/editorconfig.yaml)
[![License](https://img.shields.io/pypi/l/optional.py.svg)](https://pypi.org/project/optional.py/)
[![Python Versions](https://img.shields.io/pypi/pyversions/optional.py.svg)](https://pypi.org/project/optional.py/)
[![Contributors](https://img.shields.io/github/contributors/cbefus/optional.py.svg)](https://pypi.org/project/optional.py/)
[![Open Source Love](https://badges.frapsoft.com/os/v2/open-source.png?v=103)](https://github.com/open-source)
[![Downloads](https://pepy.tech/badge/optional-py)](https://pepy.tech/project/optional-py)

An Implementation of the Optional Object for Python

## Why

There is a difference between `None` as Empty and `None` as the result for an
Error. A common bad practice is to return `None` to indicate the absence of
something. Doing this introduces ambiguity into you code.

For example:

```python
thing = stuff.getSomeThing().getAnotherThing()
```

What will happen if the result from getSomeThing returns `None`? We will get an
`AttributeError: 'NoneType' object has no attribute 'getAnotherThing'`.

What can you do to prevent these kinds of exceptions? You can write defensively:

```python
something = stuff.getSomeThing()
if something is not None:
    thing = something.getAnotherThing()
```

However, if we add to our chain, you can imagine how the nesting of defensive
checks adds up quickly. These defensive checks obfuscate our actual business
logic, decreasing readability. Furthermore, defensive checking is an error prone
process, because it is easy to forget to check a required condition.

So we present you with an **Optional** object as an alternative.

## Install

**Compatible with Python 3.10 and up!**

```bash
pip install optional.py
```

## Usage

1. You can import it using:

   ```python
   from optional import Nothing, Option, Optional, Something
   ```

2. You can set it to empty:

   instead of: :scream_cat:

   ```python
   return None
   ```

   you can do: :smile_cat:

   ```python
   return Optional.empty()
   ```

   or

   ```python
   return Optional.of()
   ```

3. You can set it to have content:

   instead of: :scream_cat:

   ```python
   return "thing"
   ```

   you can do: :smile_cat:

   ```python
   return Optional.of("thing")
   ```

4. You can check if its present:

   instead of: :scream_cat:

   ```python
   if thing is not None:
   ```

   you can do: :smile_cat:

   ```python
   thing = some_func_returning_an_optional()
   if thing:
   ```

5. You can check if its empty:

   instead of: :scream_cat:

   ```python
   if thing is None:
   ```

   you can do: :smile_cat:

   ```python
   thing = some_func_returning_an_optional()
   if not thing:
   ```

6. You can match against the result and destructure the value:

   instead of: :scream_cat:

   ```python
   print(thing)
   ```

   you can do: :smirk_cat:

   ```python
   match some_func_returning_an_optional():
       case Something(thing):
           print(thing)
   ```

7. You can match against an empty optional, but **can't** destructure the value:

   instead of: :crying_cat_face:

   ```python
   if thing is None:
       print(None) # very odd
   ```

   you can do: :smirk_cat:

   ```python
   match some_func_returning_an_optional()
       case Nothing():
           print("We didn't get a thing!")
   ```

8. You can compare two optionals: :smile_cat:

   ```python
   Optional.empty() == Optional.empty() # True
   Optional.of("thing") == Optional.of("thing") # True
   Optional.of("thing") == Optional.empty() # False
   Optional.of("thing") == Optional.of("PANTS") # False
   ```

## Tests

There is complete test coverage and they pass in all Python versions 3.10 and up.

### Running Unit Tests

First, install `poetry` using the instructions located [here](https://python-poetry.org/docs/#installation).

Then, install the requirements using:

```bash
poetry install
```

You can run the tests (with coverage) using:

```bash
poetry run pytest
```
