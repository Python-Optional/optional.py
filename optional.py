

class Optional:

    def __init__(self, thing):
        self._thing = thing
        self._presence_checked = False

    @staticmethod
    def of(thing):
        return Optional(thing)

    @staticmethod
    def empty():
        return Optional(None)

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

    def if_present(self, consumer):
        if self._thing is not None:
            consumer(self._thing)
        return Optional._NotPresent()

    class _NotPresent:
        
        def or_else(self, procedure):
            procedure()


class OptionalAccessWithoutCheckingPresenceException(Exception):
    pass


class OptionalAccessOfEmptyException(Exception):
    pass