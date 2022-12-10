from abc import ABCMeta, abstractmethod, abstractproperty

from .book import BookInterface


class NodeInterface(metaclass=ABCMeta):

    def __init__(self) -> None:
        """"""

    @abstractproperty
    def pub(self) -> str:
        """"""

    @abstractmethod
    def save(self) -> None:
        """"""

    @abstractmethod
    def send_message(self, message: str, book: 'BookInterface') -> None:
        """"""

    @abstractmethod
    def scan_messages(self, book: 'BookInterface') -> None:
        """"""

    @abstractmethod
    def __repr__(self) -> str:
        """"""
