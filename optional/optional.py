from typing import TypeAlias, TypeVar, overload

from optional.nothing import Nothing
from optional.something import Something

T = TypeVar("T")


Option: TypeAlias = Something[T] | Nothing


class Optional:
    """Entrypoint of optional.py

    Provides static methods to help intelligently create
    both :class:`Something` and :class:`Nothing` values"""

    @staticmethod
    @overload
    def of() -> Nothing: ...

    @staticmethod
    @overload
    def of(thing: None) -> Nothing: ...

    @staticmethod
    @overload
    def of(thing: T) -> Something[T]: ...

    @staticmethod
    def of(thing: T | None = None) -> Option[T]:
        return Nothing() if thing is None else Something(thing)

    @staticmethod
    def empty() -> Nothing:
        return Nothing()
