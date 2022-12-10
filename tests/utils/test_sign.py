from bitchat.utils.key_generator import get_keys
from bitchat.utils.sign import sign_message, verify_message


def sign_msg() -> None:
    msg = "Hello world"
    public_key, private_key = get_keys()
    signature = sign_message(message=msg, private_key=private_key)
    verfied = verify_message(
        message=msg,
        public_key=public_key,
        signature=signature
    )
    assert (verfied)


def test_sign() -> None:
    sign_msg()
