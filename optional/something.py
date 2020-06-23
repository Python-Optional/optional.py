from .abstract_optional import AbstractOptional
from .exceptions import FlatMapFunctionDoesNotReturnOptionalException
from typing import TypeVar, Generic, Callable


T = TypeVar('T')


class Something(AbstractOptional, Generic[T]):
    def __init__(self, value, optional):
        # type: (T, 'AbstractOptional') -> None
        if value is None:
            raise ValueError('Invalid value for Something: None')

        self.__value = value
        self.__optional = optional

    def is_empty(self):
        # type: () -> bool
        return False

    def get(self):
        # type: () -> T
        return self.__value

    def get_or_default(self, default_value):
        # type: (T) -> T
        return self.get()

    def get_or_raise(self, raiseable):
        # type: (type) -> T
        return self.get()

    def if_present(self, consumer):
        # type: (Callable) -> 'AbstractOptional'
        consumer(self.get())
        return self

    def or_else(self, supplier):
        # type: (Callable) -> 'AbstractOptional'
        return self

    def or_else_raise(self, raiseable):
        # type: (type) -> 'AbstractOptional'
        return self

    def map(self, func):
        # type: (Callable) -> 'AbstractOptional'
        return self.__optional.of(func(self.get()))

    def flat_map(self, func):
        # type: (Callable) -> 'AbstractOptional'
        res = func(self.get())
        if not isinstance(res, AbstractOptional):
            raise FlatMapFunctionDoesNotReturnOptionalException(
                "Mapping function to flat_map must return Optional."
            )

        return res

    def __eq__(self, other):
        # type: ('AbstractOptional') -> bool
        return isinstance(other, Something) and self.get() == other.get()

    def __repr__(self):
        # type: () -> str
        return 'Optional.of({!r})'.format(self.get())
