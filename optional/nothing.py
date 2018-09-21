from .abstract_optional import AbstractOptional
from .exceptions import OptionalAccessOfEmptyException


class Nothing(AbstractOptional):
    def is_present(self):
        return False

    def get(self):
        raise OptionalAccessOfEmptyException(
            "You cannot call get on an empty optional"
        )

    def if_present(self, consumer):
        return self

    def or_else(self, procedure):
        return procedure()

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
