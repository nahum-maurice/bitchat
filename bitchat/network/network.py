"""
Written by Nahum Maurice on Thur, December 8, 2022

This the network that contains all the nodes of the system.
It's not a real network in the sense that it does not emphasis on the
connection between nodes, but the goal is to find a way to obtain
consensus when it comes to taking actions on the Book
"""
from __future__ import annotations

from abc import ABCMeta, abstractmethod, abstractproperty
from typing import Optional

from ..errors.single_instance_violation import SingleInstanceViolation
from .node import Node


class NetworkInterface(metaclass=ABCMeta):
    def __init__(self, first: Node) -> None:
        """"""
    @abstractproperty
    def size(self) -> int:
        """"""

    @abstractmethod
    def instance(self) -> Optional[NetworkInterface]:
        """"""

    @abstractmethod
    def elect_master(self, candidate: Node) -> None:
        """"""

    @abstractmethod
    def revoke_master(self) -> None:
        """"""

    @abstractmethod
    def join(self, node: Node, signature: str) -> None:
        """"""

    @abstractmethod
    def __repr__(self) -> str:
        """"""


class Network(NetworkInterface):

    # The unique instance of the network
    __instance: Network | None = None

    # The version of the system
    version: int = 0

    def __init__(self, first: Node) -> None:
        if Network.__instance is not None:
            raise SingleInstanceViolation
        else:
            # TODO: Try to reach other nodes and verify that they don't have
            #       any instances of network. If found, raise the single
            #       instance violation exception. Otherwise, acquire a lock
            #       and prevent other nodes of starting a network with a TTL

            # Each instance of the network has a unique identifier
            self.__id: str = ""

            # The node initiating the creation of the network automatically
            # becomes the master node
            self.__master: Node | None = first

            # All added nodes to the network
            self.__nodes: list[Node] = []

            # TODO: When the process ends, inform other nodes that they can
            #       connect and start connecting to the newly created network,
            #       with the initiating node as a master Node.

    @property
    def size(self) -> int:
        """
        Returns the amount of connected nodes
        """
        return len(self.__nodes)

    @staticmethod
    def instance() -> Optional[Network]:
        """
        This returns the single instance of Network if it exists.
        """
        return Network.__instance

    def elect_master(self, candidate: Node) -> None:
        """
        The process of electing a master should take place only under the
        condition that there is not any master ==> self.__master == None
        """
        if self.__master is not None:
            raise SingleInstanceViolation
        else:
            self.__master = candidate

    def revoke_master(self) -> None:
        """
        To revoke a master, it should be disconnected. Which mean that
        the majority of the nodes should be in difficulty to contact him.
        """
        self.__master = None

    def join(self, node: Node, signature: str) -> None:
        """
        An existing node, to join the network should send a message that is
        signed by its private key. Once verified, the Network creates with
        it a connection.
        """
        # TODO

    def __repr__(self) -> str:
        """
        Returns a string representation of the network
        """
        return f"Network(ID --> {self.__id}, Length --> {len(self.__nodes)})"
