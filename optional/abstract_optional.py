from abc import abstractmethod

from .compatible_abc import CompatibleABC


class AbstractOptional(CompatibleABC):

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
    def or_else_raise(self, raiseable):
        pass

    @abstractmethod
    def map(self, func):
        pass

    @abstractmethod
    def flat_map(self, func):
        pass
