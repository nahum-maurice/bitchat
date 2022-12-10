from abc import ABCMeta, abstractmethod, abstractproperty
from typing import Optional

from .node import NodeInterface


class NetworkInterface(metaclass=ABCMeta):

    def __init__(self, first: 'NodeInterface') -> None:
        """"""
    @abstractproperty
    def size(self) -> int:
        """"""

    @abstractmethod
    def instance(self) -> Optional['NetworkInterface']:
        """"""

    @abstractmethod
    def elect_master(self, candidate: 'NodeInterface') -> None:
        """"""

    @abstractmethod
    def revoke_master(self) -> None:
        """"""

    @abstractmethod
    def join(self, node: 'NodeInterface', signature: str) -> None:
        """"""

    @abstractmethod
    def __repr__(self) -> str:
        """"""
