from .nothing import Nothing
from .something import Something


class Optional(object):
    @classmethod
    def of(cls, thing=None):
        return Nothing() if thing is None else Something(thing, cls)

    @staticmethod
    def empty():
        return Nothing()
