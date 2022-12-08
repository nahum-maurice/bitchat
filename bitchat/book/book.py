"""
Written by Nahum Maurice on Thur, December 8, 2022

This is the data structure that contains all messages. It's public, and is
shared by all the nodes in the network.
"""
from __future__ import annotations

from abc import ABCMeta, abstractmethod, abstractproperty
from typing import Optional

from ..errors.singleBookInstanceViolation import SingleBookInstanceViolation
from .message import Message


class BookInterface(metaclass=ABCMeta):

    def __init__(self) -> None:
        """"""

    @abstractmethod
    def instance(self) -> Optional[BookInterface]:
        """"""

    @abstractproperty
    def messages(self) -> list[Message]:
        """"""

    @abstractmethod
    def __repr__(self) -> str:
        """"""

    @abstractmethod
    def add_message(self, message: Message) -> None:
        """"""


class Book(BookInterface):

    # One single instance of the class
    __instance = None

    # The algorithm version
    __version = 0

    def __init__(self, first_node: str) -> None:
        # There should always be one instance of the book and this instance
        # should be the one shared by every node, but only be modifiable by
        # the master node. Therefore, this class follows the pattern of
        # Singleton
        if Book.__instance is not None:
            raise SingleBookInstanceViolation

        # The ID (__id) of a book is its primary identifier. It is used to
        # keep track of the different instances of the Book that handles
        # the transactions / communication.
        self.__id: str = ""

        # Each book should have a message0, the equivalent of the Genesis
        # Block for blockchain architecture. It should be generated by the
        # book uppon creation.
        self.__message0: str = ""

        # Each book is initiated by the first node connecting to the network.
        # This should be the address of the node.
        self.__first_node: str = first_node

        # Each book contains a list of messages, these are encrypted message
        # with addresses
        self.__messages: list[Message] = []

        # Assigning __instance to the newly created one
        Book.__instance = self

    def __repr__(self) -> str:
        messages = ""
        for message in self.__messages:
            messages += f"\nIndex --> {self.__messages.index(message)} | " + \
                f"Timestamp --> {message.header.timestamp} | receiver " + \
                f"--> {message.header.receiver}"

        return f"Book(ID: {self.__id}, First Node: {self.__first_node} " + \
               f"Lenght: {len(self.__messages)})" + \
               f"\nMessages: {messages}"

    def add_message(self, message: Message) -> None:
        self.__messages.append(message)

    @staticmethod
    def instance() -> Optional[Book]:
        return Book.__instance

    @property
    def messages(self) -> list[Message]:
        return self.__messages
