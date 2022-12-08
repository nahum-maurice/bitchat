from bitchat.book.message import Message, MessageHeader

receiver = "0x9238494ffac739347af9de9359abfd24"
sender = "0x9238494ffa8929347af9de9352957d24"


def header_correct() -> MessageHeader:
    header = MessageHeader(
        receiver=receiver,
        sender=sender,
        version="0.1.0",
        timestamp="1670501700620"
    )
    return header


def message_correct() -> Message:
    header = MessageHeader(
        receiver=receiver,
        sender=sender,
        version="0.1.0",
        timestamp="1670501700620"
    )
    data = "0x939429jfds9bigyfksadfvo29fisdvibsf02fi"

    msg = Message(header=header, data=data)
    return msg


def test() -> None:
    header = header_correct()
    msg = message_correct()

    assert (isinstance(header, MessageHeader))
    assert (isinstance(msg, Message))
