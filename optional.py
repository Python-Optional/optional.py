

class Optional:

    def __init__(self, thing):
        self._thing = thing
        self._presence_checked = False

    @staticmethod
    def of(thing):
        if thing is None:
            return Optional.empty()
        return Optional(thing)

    @staticmethod
    def empty():
        return Optional(None)

    def __eq__(self, other):
        if not isinstance(other, Optional):
            return False

        if self.is_empty() and other.is_empty():
            return True

        if self.is_empty() or other.is_empty():
            return False

        return other.get() == self.get()

    def __neq__(self, other):
        return not self == other

    def is_present(self):
        self._presence_checked = True
        return self._thing is not None

    def is_empty(self):
        return not self.is_present()

    def get(self):
        if not self._presence_checked:
            raise OptionalAccessWithoutCheckingPresenceException(
                "You cannot access the contents of an optional without first checking for its presence.")

        if self._thing is None:
            raise OptionalAccessOfEmptyException("You cannot call get on an empty optional")

        return self._thing

    def map(self, func):
        if self.is_empty():
            return Optional.empty()
        return Optional.of(func(self.get()))

    def flat_map(self, func):
        if self.is_empty():
            return Optional.empty()

        res = func(self.get())
        if not isinstance(res, Optional):
            raise FlatMapFunctionDoesNotReturnOptionalException("Mapping function to flat_map must return Optional.")

        return res

    def if_present(self, consumer):
        if self._thing is not None:
            consumer(self._thing)
        return Optional._NotPresent()

    class _NotPresent:
        
        def or_else(self, procedure):
            procedure()


class FlatMapFunctionDoesNotReturnOptionalException(Exception):
    pass


class OptionalAccessWithoutCheckingPresenceException(Exception):
    pass


class OptionalAccessOfEmptyException(Exception):
    pass