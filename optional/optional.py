from .optional_factory import OptionalFactory


class Optional(object):
    @staticmethod
    def of(thing=None):
        return OptionalFactory.build(thing)

    @staticmethod
    def empty():
        return OptionalFactory.build()

