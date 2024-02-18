from types import NotImplementedType
from typing import Any, Generic, TypeVar

T = TypeVar("T")


class Something(Generic[T]):
    """Represents the presence of a value.

    Rarely instantiated on its own, see :func:`Optional.of`"""

    __match_args__ = ("_value",)

    def __init__(self, value: T) -> None:
        if value is None:
            raise ValueError("Invalid value for Something: None")

        self._value = value

    def __eq__(self, other: Any) -> bool | NotImplementedType:
        if not isinstance(other, Something):
            return NotImplemented

        return self._value == other._value

    def __repr__(self) -> str:
        return f"Optional.of({self._value!r})"

    def __bool__(self) -> bool:
        return True
