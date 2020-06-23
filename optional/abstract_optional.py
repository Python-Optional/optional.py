from abc import abstractmethod
from .compatible_abc import CompatibleABC
from typing import TypeVar, Generic, Callable, Union, NoReturn


T = TypeVar('T')


class AbstractOptional(CompatibleABC, Generic[T]):

    @abstractmethod
    def is_empty(self):
        # type: () -> bool
        pass

    @abstractmethod
    def get(self):
        # type: () -> Union[T, NoReturn]
        pass

    @abstractmethod
    def get_or_default(self, default_value):
        # type: (T) -> T
        pass

    @abstractmethod
    def get_or_raise(self, exception):
        # type: (type) -> Union[T, NoReturn]
        pass

    @abstractmethod
    def if_present(self, consumer):
        # type: (Callable) -> 'AbstractOptional'
        pass

    @abstractmethod
    def or_else(self, procedure):
        # type: (Callable) -> 'AbstractOptional'
        pass

    @abstractmethod
    def or_else_raise(self, raiseable):
        # type: (Callable) -> Union['AbstractOptional', NoReturn]
        pass

    @abstractmethod
    def map(self, func):
        # type: (Callable) -> 'AbstractOptional'
        pass

    @abstractmethod
    def flat_map(self, func):
        # type: (Callable) -> 'AbstractOptional'
        pass

    def is_present(self):
        # type: () -> bool
        return not self.is_empty()

    __bool__ = __nonzero__ = is_present
