from .abstract_optional import AbstractOptional
from .exceptions import OptionalAccessOfEmptyException


class Nothing(AbstractOptional):

    def __init__(self, optional):
        self.__optional = optional

    def is_empty(self):
        return True

    def get(self):
        raise OptionalAccessOfEmptyException(
            "You cannot call get on an empty optional"
        )

    def get_or_default(self, default_value):
        return default_value

    def get_or_raise(self, raiseable):
        raise raiseable

    def if_present(self, consumer):
        return self

    def or_else(self, supplier):
        return self.__optional.of(supplier())

    def or_else_raise(self, raiseable):
        raise raiseable

    def map(self, func):
        return self

    def flat_map(self, func):
        return self

    def __eq__(self, other):
        return isinstance(other, Nothing)

    def __repr__(self):
        return 'Optional.empty()'
