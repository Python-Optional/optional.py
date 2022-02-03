from abc import abstractmethod

from .compatible_abc import CompatibleABC


class AbstractOptional(CompatibleABC):

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def get_or_default(self, default_value):
        pass

    @abstractmethod
    def get_or_raise(self, raiseable):
        pass

    @abstractmethod
    def if_present(self, consumer):
        pass

    @abstractmethod
    def or_else(self, supplier):
        pass

    @abstractmethod
    def or_else_raise(self, raiseable):
        pass

    @abstractmethod
    def map(self, func):
        pass

    @abstractmethod
    def flat_map(self, func):
        pass

    def is_present(self):
        return not self.is_empty()

    __bool__ = __nonzero__ = is_present
