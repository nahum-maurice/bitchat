import pytest

from bitchat.book.book import Book


def book_correct() -> None:
    # The single instance of the Book
    Book()
    Book()


def test_book() -> None:
    with pytest.raises("SingleBookInstanceViolation"):
        # Should not allow multiple instances
        book_correct()
