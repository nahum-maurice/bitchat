import pytest

from bitchat.utils.encryptor import Encryptor
from bitchat.utils.key_generator import get_keys


def encryption() -> None:
    text = "Hello world"
    pub, _ = get_keys()
    result = Encryptor(data=text, key=pub)

    assert type(result) == Encryptor
    assert type(result.value) == bytes

    object = {"foo": "bar"}
    result = Encryptor(data=object, key=pub)

    assert type(result) == Encryptor
    assert type(result.value) == bytes

    assert type(result.__repr__()) == str


def none_encryption() -> None:
    pub, _ = get_keys()
    Encryptor(data=None, key=pub)


def test_encryption() -> None:
    encryption()

    with pytest.raises(TypeError):
        none_encryption()
