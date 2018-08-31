# PyOptional
An Implementation of the Optional Object for Python

## Why

There is a difference between `None` as Empty and `None` as the result for an Error.  A common bad practice is to
return `None` to indicate the absence of something.  This can cause issues.

For example:
```python
thing = stuff.getSomeThing().getAnotherThing()
```
What will happen if the result from getSomeThing returns `None`?  We will get an `AttributeError: 'NoneType' object has
no attribute 'getAnotherThing'`.

What can you do to prevent these kinds of exceptions?  You can write defensively:
```python
something = stuff.getSomeThing()
if something is not None:
    thing = something.getAnotherThing()
```
However, if we add to our chain, you can imagine how the nesting of defensive checks gets ugly quickly. There is plenty
of information out there on why defensive coding is not a great idea, which is beyond the scope of this README.

Ultimately, these defensive checks are annoying and obfuscate our actual business logic (decreasing the readability).
Furthermore it is an error prone process, because it is easy to forget to do the checks everywhere.

So we present you with an **Optional** object as an alternative.

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

8. **__Best Usage:__** You can chain on presence:
    ```python
    thing = some_func_returning_an_optional()
    thing.if_present(lambda thing: print(thing))
    ```
    instead of:
    ```python
    if thing is not None:
        print(thing)
    ```

9. **__Best Usage:__** You can chain on non presence:
    ```python
    thing = some_func_returning_an_optional()
    thing.if_present(lambda thing: print(thing)).or_else(lambda _: print("PANTS!"))
    ```
    instead of:
    ```python
    if thing is not None:
        print(thing)
    else:
        print("PANTS!")
    ```

10. **__Best Usage:__** You can map a function:
    ```python
    def mapping_func(thing):
        return thing + "PANTS"
    
    thing_to_map = Optional.of("thing")
    mapped_thing = thing_to_map.map(mapping_func) # returns Optional.of("thingPANTS")
    ```
    Note that if the mapping function returns `None` then the map call will return `Optional.empty()`. Also
    if you call `map` on an empty optional it will return `Optional.empty()`.
    
11. **__Best Usage:__** You can flat map a function which returns an Optional.
    ```python
    def flat_mapping_func(thing):
        return Optional.of(thing + "PANTS")
    
    thing_to_map = Optional.of("thing")
    mapped_thing = thing_to_map.map(mapping_func) # returns Optional.of("thingPANTS")
    ```
    Note that this does not return an Optional of an Optional.  __Use this for mapping functions which return optionals.__ 
    If the mapping function you use with this does not return an Optional, calling `flat_map` will raise a
    `FlatMapFunctionDoesNotReturnOptionalException`.














