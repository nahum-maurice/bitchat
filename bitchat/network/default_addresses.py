"""
Written by Nahum Maurice on Wed, December 21, 2022

Here are specified the addresses that are by default up. These should be
statically defined and should not go down. They are the nodes that
each new node that are trying to connect should contact.
"""
from .data_structures import Address


# TODO Should be replaced by actual addresses
DEFAULT_ADDRESSES = (
    Address("0.0.0.0", 0),
)
