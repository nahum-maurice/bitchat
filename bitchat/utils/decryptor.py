"""
Written by Nahum Maurice on Fri, December 9, 2022

This is a class of decrytor functions that provides method
for decrypting different types of data
"""
from __future__ import annotations

import base64
import json
from typing import Union

import rsa


class Decryptor:
    """
    An asymmetric decryptor using private key. It contains methods
    that can chain to return values as string or object (including
    list).
    """

    def __init__(self, data: bytes | None, key: rsa.PrivateKey) -> None:
        """
        Decrypts a raw bytes encrypted message but returns it
        in the form of bytes.
        """
        self.__result: bytes = bytes(0)
        if (type(data) == bytes):
            decrypted: bytes = rsa.decrypt(data, key)
            self.__result = decrypted

    def to_string(self) -> str:
        """
        Decodes to string.
        """
        data_bytes = base64.b64decode(self.__result)
        ascii_msg = data_bytes.decode("ascii")
        return ascii_msg

    def to_object(self) -> Union[list, dict]:
        """
        Decodes to object or list.
        """
        data_bytes = base64.b64decode(self.__result)
        ascii_msg = data_bytes.decode("ascii")
        ascii_msg = ascii_msg.replace("'", "\"")
        result: dict | list = json.loads(ascii_msg)
        return result

    def __repr__(self) -> str:
        """
        Returns the value of the decrypted result.
        """
        return str(self.__result)
