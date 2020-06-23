from .nothing import Nothing
from .something import Something
from typing import Any, Union


class Optional(object):
    @classmethod
    def of(cls, thing=None):
        # type: (Any) -> Union['Something', 'Nothing']
        return Nothing(cls) if thing is None else Something(thing, cls)

    @classmethod
    def empty(cls):
        # type: () -> 'Nothing'
        return Nothing(cls)
