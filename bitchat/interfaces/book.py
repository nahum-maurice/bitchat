from abc import ABCMeta, abstractmethod, abstractproperty

from .message import MessageInterface


class BookInterface(metaclass=ABCMeta):

    def __init__(self) -> None:
        """"""

    @abstractmethod
    def instance(self) -> 'BookInterface' | None:
        """"""

    @abstractproperty
    def messages(self) -> list[MessageInterface]:
        """"""

    @abstractmethod
    def __repr__(self) -> str:
        """"""

    @abstractmethod
    def add_message(self, message: 'MessageInterface') -> None:
        """"""
