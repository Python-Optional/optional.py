from types import NotImplementedType
from typing import Any


class Nothing:
    """Represents the absence of a value.

    Rarely instantiated on its own, see :func:`Optional.empty`"""

    def __eq__(self, other: Any) -> bool | NotImplementedType:
        if not isinstance(other, Nothing):
            return NotImplemented

        return True

    def __repr__(self) -> str:
        return "Optional.empty()"

    def __bool__(self) -> bool:
        return False
