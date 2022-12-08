import pytest

from bitchat.book.book import Book, SingleBookInstanceViolation


def book_correct() -> None:
    # The single instance of the Book
    s = Book()
    t = Book()
    print(s)
    print(t)


def test_book() -> None:
    with pytest.raises(SingleBookInstanceViolation):
        # Should not allow multiple instances
        book_correct()
