from abc import ABCMeta
from dataclasses import dataclass


@dataclass
class MessageHeaderInterface(metaclass=ABCMeta):
    receiver: str
    sender: str
    version: str
    timestamp: str


@dataclass
class MessageInterface(metaclass=ABCMeta):
    header: MessageHeaderInterface
    data: str
