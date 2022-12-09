"""
Written by Nahum Maurice on Fri, December 9, 2022

This is a class of encryptor functions that provides method
for encrypting different types of data
"""
from __future__ import annotations

import base64
from typing import Optional

import rsa


class Encryptor:
    """
    An encryptor for objects, string and list by first encode
    in byte using Base 64, then asymmetric encrypting using
    public key.
    """

    def encryptor(self, data: bytes | None, key: rsa.PublicKey) -> bytes:
        """
        Makes the encryption using RSA with public key
        """
        if type(data) == bytes:
            encrypted_message = rsa.encrypt(data, key)

            return encrypted_message
        return bytes(0)

    def __init__(self, data: str | dict | list | None, key: rsa.PublicKey) \
            -> None:
        """
        Encrypts a string, an object or list.
        """
        self.__result: bytes | None = None

        if type(data) == dict or type(data) == list:
            # Takes a dict or a list and returns it in the form of bytes.
            string_obj = str(data)
            ascii_string = string_obj.encode("ascii")
            byte_encoded = base64.b64encode(ascii_string)
            result = self.encryptor(byte_encoded, key)
            self.__result = result
        elif type(data) == str:
            # Takes a string and returns it in the form of bytes.
            ascii_string = str(data).encode("ascii")
            result = self.encryptor(base64.b64encode(ascii_string), key)
            self.__result = result
        else:
            raise TypeError("Unsupported type")

    @property
    def value(self) -> Optional[bytes]:
        return self.__result

    def __repr__(self) -> str:
        """
        Returns the value of the encrypted result.
        """
        return str(self.__result)
