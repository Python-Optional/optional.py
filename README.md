# PyOptional
An Implementation of the Optional Object for Python

## Why

There is a difference between `None` as Empty and `None` as the result for an Error.  A common bad practice is to
return `None` to indicate the absence of something.  For example:
```python
thing = stuff.getSomeThing().getAnotherThing()
```
What will happen if the result from getSomeThing returns None?  We will get an `AttributeError: 'NoneType' object has
no attribute 'getAnotherThing'`.

To give some historical context, Tony Hoare—one of the giants of computer science—wrote, "I call it my billion-dollar
mistake. It was the invention of the null reference in 1965. I couldn't resist the temptation to put in a null
reference, simply because it was so easy to implement."

What can you do to prevent these kinds of checks?  You can write defensively:
```python
something = stuff.getSomeThing()
if something is not Null:
    thing = something.getAnotherThing()
```
However if we add to our chain you can imagine how the nesting of defensive checks gets ugly quickly. There is plenty
of information out there on why coding defensively is not a great idea, which is beyond the scope of this README.

Ultimately, these defensive checks are annoying and obfuscate our actual business logic (decreasing the readability).
Furthermore it is an error prone process, because it is easy to forget to do the null checks everywhere.

So we present you with an optional object as an alternative.

## Usage

1. You can set it to empty instead of None:
    ```python
    from optional import Optional
    ...
    return Optional.empty()
    ```
    instead of:
    ```python
    return None
    ```

2. You can set it to have content otherwise:
    ```python
    from optional import Optional
    ...
    return Optional.of("thing")
    ```
    instead of:
    ```python
    return "thing"
    ```

3. You can check if its present:
    ```python
    thing = some_func_returning_an_optional()
    if thing.is_present():
    ```
    instead of:
    ```python
    if thing is not None:
    ```

4. You can check if its empty:
    ```python
    thing = some_func_returning_an_optional()
    if thing.is_empty():
    ```
    instead of:
    ```python
    if thing is None:
    ```

5. You can get the value:
    ```python
    thing = some_func_returning_an_optional()
    ...
    print(thing.get())
    ```
    instead of:
    ```python
    print(thing)
    ```

6. But you **can't** get the value without first checking for presence:
    ```python
    thing = some_func_returning_an_optional()
    print(thing.get()) # **will raise an exception**
    
    ```
    but:
    ```python
    thing = some_func_returning_an_optional()
    if thing.is_present(): # could use is_empty() as alternative
        print(thing.get()) # **does not throw**
    ```
    instead of:
    ```python
    if thing is not None:
        print(thing)
    ```

7. You **can't** get the value if its empty:
    ```python
    thing = some_func_returning_an_optional()
    if thing.is_empty():
        print(thing.get()) # **will raise an exception**
    ```
    instead of:
    ```python
    if thing is None:
        print(None) # very odd
    ```

8. **Best Usage:** You can chain on presence:
    ```python
    thing = some_func_returning_an_optional()
    thing.if_present(lambda thing: print(thing))
    ```
    instead of:
    ```python
    if thing is not None:
        print(thing)
    ```

9. **Best Usage:** You can chain on non presence:
    ```python
    thing = some_func_returning_an_optional()
    thing.if_present(lambda thing: print(thing)).or_else(lambda _: print("PANTS!")
    ```
    instead of:
    ```python
    if thing is not None:
        print(thing)
    else:
        print("PANTS!")
    ```


















