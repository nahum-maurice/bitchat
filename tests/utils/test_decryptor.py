from bitchat.utils.decryptor import Decryptor
from bitchat.utils.encryptor import Encryptor
from bitchat.utils.key_generator import get_keys


def decrypting() -> None:
    public, private = get_keys()
    text = "Hello, world!"
    obj = {"hello": "world"}

    # Encryption
    encrypted_text = Encryptor(data=text, key=public)
    encrypted_obj = Encryptor(data=obj, key=public)

    # Decryption
    decrypted_text = \
        Decryptor(data=encrypted_text.value, key=private).to_string()
    decrypted_obj = \
        Decryptor(data=encrypted_obj.value, key=private).to_object()

    assert type(decrypted_obj) == dict
    assert type(decrypted_text) == str

    assert type(decrypted_obj.__repr__()) == str

    # Correctness
    assert (decrypted_text == text)
    flag = 0
    for i in decrypted_obj:
        if decrypted_obj.get(i) != obj.get(i):
            flag += 1
            break
    assert (flag == 0)


def test_decryptor() -> None:
    decrypting()
