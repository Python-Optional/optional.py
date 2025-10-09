from types import NotImplementedType
from typing import Generic, TypeVar, final

from typing_extensions import override

T = TypeVar("T")


@final
class Something(Generic[T]):
    """Represents the presence of a value.

    Rarely instantiated on its own, see :func:`Optional.of`"""

    __match_args__ = ("_value",)

    def __init__(self, value: T) -> None:
        if value is None:
            raise ValueError("Invalid value for Something: None")

        self._value = value

    @override
    def __eq__(self, other: object) -> bool | NotImplementedType:
        if not isinstance(other, Something):
            return NotImplemented

        return self._value == other._value  # pyright: ignore[reportUnknownVariableType, reportUnknownMemberType]

    @override
    def __repr__(self) -> str:
        return f"Optional.of({self._value!r})"

    def __bool__(self) -> bool:
        return True
