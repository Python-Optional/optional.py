from .nothing import Nothing
from .something import Something


class OptionalFactory:

    @staticmethod
    def build(from_thing=None):
        return Nothing() if from_thing is None else Something(from_thing)
