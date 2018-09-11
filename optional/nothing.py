from .abstract_optional import _AbstractOptional
from .exceptions import OptionalAccessOfEmptyException


class _Nothing(_AbstractOptional):
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

    def map(self, func):
        return self

    def flat_map(self, func):
        return self

    def __eq__(self, other):
        return isinstance(other, _Nothing)

    def __repr__(self):
        return 'Optional.empty()'
