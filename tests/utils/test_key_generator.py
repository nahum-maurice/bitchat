from bitchat.utils.key_generator import get_keys


def keys_generation() -> None:
    pub, private = get_keys()

    assert pub is not None
    assert private is not None


def test_key_generator() -> None:
    keys_generation()
