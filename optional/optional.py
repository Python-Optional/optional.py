from abc import abstractmethod

from .compatible_abc import CompatibleABC


class Optional(object):
    @staticmethod
    def of(thing):
        return _Nothing() if thing is None else _Something(thing)

    @staticmethod
    def empty():
        return _Nothing()


class _AbstractOptional(CompatibleABC):

    @abstractmethod
    def is_present(self):
        pass

    def is_empty(self):
        return not self.is_present()

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def if_present(self, consumer):
        pass

    @abstractmethod
    def or_else(self, procedure):
        pass

    @abstractmethod
    def map(self, func):
        pass

    @abstractmethod
    def flat_map(self, func):
        pass


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


class _Something(_AbstractOptional):
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
        return Optional.of(func(self.get()))

    def flat_map(self, func):
        res = func(self.get())
        if not isinstance(res, _AbstractOptional):
            raise FlatMapFunctionDoesNotReturnOptionalException(
                "Mapping function to flat_map must return Optional."
            )

        return res

    def __eq__(self, other):
        return isinstance(other, _Something) and self.get() == other.get()

    def __repr__(self):
        return 'Optional.of({})'.format(self.get())


class OptionalAccessOfEmptyException(Exception):
    pass


class FlatMapFunctionDoesNotReturnOptionalException(Exception):
    pass
