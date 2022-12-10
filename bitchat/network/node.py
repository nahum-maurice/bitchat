"""
Written by Nahum Maurice on Thur, December 8, 2022

This the network that contains all the nodes of the system.
It's not a real network in the sense that it does not emphasis on the
connection between nodes, but the goal is to find a way to obtain
consensus when it comes to taking actions on the Book
"""
from rsa import PrivateKey, PublicKey

from ..book.book import Book
from ..interfaces.node import NodeInterface
from ..utils.key_generator import get_keys


class Node(NodeInterface):
    """
    A node is a connection point to the network. It can be seen
    as a user that joined.
    """

    def __init__(self) -> None:
        """
        Setup the initial values for a node
        """

        # If not found, generate new keys and save them for further use
        public, private = get_keys()

        with open("private.pem", "wb") as f:
            f.write(private.save_pkcs1("PEM"))

        with open("public.pem", "wb") as f:
            f.write(public.save_pkcs1("PEM"))

        self.__private_key: PrivateKey = private
        self.__public_key: PublicKey = public
        self.__createdAt: str = ""

    @property
    def pub(self) -> str:
        return str(self.__public_key)

    def save(self) -> None:
        """
        When created, the user should commit himself to the Network. This
        means adding his public key to the list of public keys available on
        the network.
        """
        # TODO

    def send_message(self, message: str, book: Book) -> None:  # type: ignore[override]
        """
        This serves to send message in the network by the node. To send a
        message in the network, the node should encrypt the message with
        the public key of the receiver, and add it to the pool of waiting
        messages, where the master node will commmit to the Book.
        """
        # TODO

    def scan_messages(self, book: Book) -> None:  # type: ignore[override]
        """
        This allows the node to scan all the messages in the Book, and to
        reconstitute his messages by successfully verify the messages, which
        means by decrypting them. If a message is decrypted by the user,
        using his private key, that means that the message was encrypted
        with his public key, therefore, the message was addressed to him.
        """
        # TODO

    def __repr__(self) -> str:
        return f"Node(Public Key: {self.__public_key}"
