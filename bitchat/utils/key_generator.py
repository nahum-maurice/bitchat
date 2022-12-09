"""
Written by Nahum Maurice on Fri, December 9, 2022

This contains a function that generates public and private
keys when they are non-existent and load them otherwise
"""
import rsa
from rsa import PrivateKey, PublicKey


def get_keys() -> tuple[PublicKey, PrivateKey]:
    """
    Generates the public and private keys using RSA.
    """
    public_key: PublicKey | None = None
    private_key: PrivateKey | None = None

    # Attempt to find saved values
    try:
        with open("public.pem", "rb") as f:
            public_key = rsa.PublicKey.load_pkcs1(f.read())

        with open("private.pem", "rb") as f:
            private_key = rsa.PrivateKey.load_pkcs1(f.read())
    except FileNotFoundError:
        # Key generation with RSA algorith
        public_key, private_key = rsa.newkeys(512)

        # Save these for future needs
        with open("private.pem", "wb") as f:
            f.write(private_key.save_pkcs1("PEM"))
        with open("public.pem", "wb") as f:
            f.write(public_key.save_pkcs1("PEM"))

    return public_key, private_key
