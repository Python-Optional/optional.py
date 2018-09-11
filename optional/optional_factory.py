from .nothing import _Nothing
from .something import _Something


class OptionalFactory:

    @staticmethod
    def build(from_thing=None):
        return _Nothing() if from_thing is None else _Something(from_thing)