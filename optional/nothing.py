from .abstract_optional import AbstractOptional
from .exceptions import OptionalAccessOfEmptyException
from typing import TypeVar, Generic, Callable, NoReturn


T = TypeVar('T')


class Nothing(AbstractOptional, Generic[T]):

    def __init__(self, optional):
        # type: ('AbstractOptional') -> None
        self.__optional = optional

    def is_empty(self):
        # type: () -> bool
        return True

    def get(self):
        # type: () -> NoReturn
        raise OptionalAccessOfEmptyException(
            "You cannot call get on an empty optional"
        )

    def get_or_default(self, default_value):
        # type: (T) -> T
        return default_value

    def get_or_raise(self, raiseable):
        # type: (type) -> NoReturn
        raise raiseable

    def if_present(self, consumer):
        # type: (Callable) -> 'AbstractOptional'
        return self

    def or_else(self, supplier):
        # type: (Callable) -> 'AbstractOptional'
        return self.__optional.of(supplier())

    def or_else_raise(self, raiseable):
        # type: (type) -> NoReturn
        raise raiseable

    def map(self, func):
        # type: (Callable) -> 'AbstractOptional'
        return self

    def flat_map(self, func):
        # type: (Callable) -> 'AbstractOptional'
        return self

    def __eq__(self, other):
        # type: ('AbstractOptional') -> bool
        return isinstance(other, Nothing)

    def __repr__(self):
        # type: () -> str
        return 'Optional.empty()'
