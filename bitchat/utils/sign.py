"""
Written by Nahum Maurice on Sat, December 10, 2022

This provides two functions for signing and verify the signature of
as string message using asymmetric encryption.
"""
import rsa


def sign_message(
    message: str,
    private_key: rsa.PrivateKey,
    hash_algorithm: str = "SHA-256"
) -> bytes:
    """
    Sign a message with the private key.
    """
    signature: bytes = rsa.sign(message.encode(), private_key, hash_algorithm)

    return signature


def verify_message(
    message: str,
    public_key: rsa.PublicKey,
    signature: bytes,
    hash_algorithm: str = "SHA-256"
) -> bool:
    """
    Verify a signed message with the public key
    """
    result: str = rsa.verify(message.encode(), signature, public_key)

    return result == hash_algorithm
