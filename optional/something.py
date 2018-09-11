from .abstract_optional import AbstractOptional
import optional
from .exceptions import FlatMapFunctionDoesNotReturnOptionalException


class Something(AbstractOptional):
    def __init__(self, value):
        self.__value = value

    def is_present(self):
        return True

    def get(self):
        return self.__value

    def if_present(self, consumer):
        consumer(self.get())
        return self

    def or_else(self, procedure):
        return self

    def map(self, func):
        return optional.Optional.of(func(self.get()))

    def flat_map(self, func):
        res = func(self.get())
        if not isinstance(res, AbstractOptional):
            raise FlatMapFunctionDoesNotReturnOptionalException(
                "Mapping function to flat_map must return Optional."
            )

        return res

    def __eq__(self, other):
        return isinstance(other, Something) and self.get() == other.get()

    def __repr__(self):
        return 'Optional.of({})'.format(self.get())