from .nothing import Nothing
from .something import Something


class Optional(object):
    @classmethod
    def of(cls, thing=None):
        return Nothing(cls) if thing is None else Something(thing, cls)

    @classmethod
    def empty(cls):
        return Nothing(cls)
