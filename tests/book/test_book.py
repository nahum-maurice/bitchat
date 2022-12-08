from typing import Optional

import pytest

from bitchat.book.book import Book, SingleBookInstanceViolation
from bitchat.book.message import Message, MessageHeader


def one_instance() -> None:
    first_node = "0x9238494ffac739347af9de9359abfd24"
    # The single authorized instance of the Book
    book = Book(first_node=first_node)

    representation = book.__repr__()
    assert (type(representation) == str)


def second_instance() -> None:
    first_node = "0x9238494ffac739347af9de9359abfd24"
    # Attemps to create a second Book
    Book(first_node=first_node)


def adding_message() -> None:
    receiver = "0x9238494ffac739347af9de9359abfd24"
    sender = "0x9238494ffa8929347af9de9352957d24"

    msg_header: MessageHeader = MessageHeader(
        receiver=receiver,
        sender=sender,
        version="0.1.0",
        timestamp="1670501700620"
    )
    data = "0x939429jfds9bigyfksadfvo29fisdvibsf02fi"
    msg = Message(header=msg_header, data=data)

    # Getting the single instance
    book: Optional[Book] = Book.instance()
    if (book is not None):
        book.add_message(msg)
        assert (len(book.messages) == 1)


def test_book() -> None:
    one_instance()

    with pytest.raises(SingleBookInstanceViolation):
        # Should not allow multiple instances
        second_instance()

    adding_message()
