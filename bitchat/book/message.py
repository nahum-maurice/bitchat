"""
Written by Nahum Maurice on Thur, December 8, 2022

This is the data structure that contains a message. A message is in fact
a map containing the message data and some meta data
"""
from dataclasses import dataclass

from ..interfaces.message import MessageHeaderInterface, MessageInterface


@dataclass
class MessageHeader(MessageHeaderInterface):

    # The receiver public address, encrypted with his public key.
    receiver: str

    # The sender public address, encrypted with the public key of
    # the receiver
    sender: str

    # The version of the algorithm with which the message was sent.
    version: str

    # The sending time of the message
    timestamp: str


@dataclass
class Message(MessageInterface):

    # Contains both encrypted and non-encrypted meta data, essentially
    # all identifiable data are encrypted.
    header: MessageHeader

    # The content of the message, encrypted with the public key of the
    # receiver
    data: str
