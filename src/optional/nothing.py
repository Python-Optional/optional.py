from types import NotImplementedType
from typing import final

from typing_extensions import override


@final
class Nothing:
    """Represents the absence of a value.

    Rarely instantiated on its own, see :func:`Optional.empty`"""

    @override
    def __eq__(self, other: object) -> bool | NotImplementedType:
        if not isinstance(other, Nothing):
            return NotImplemented

        return True

    @override
    def __repr__(self) -> str:
        return "Optional.empty()"

    def __bool__(self) -> bool:
        return False
