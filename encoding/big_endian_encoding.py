from encoding.hex_encoding import *


def big_endian_encode(text: str) -> int:
    """
    encode a given text to its numeric representation using big-endian encoding
    """
    # converting the string to its hex representation
    hex_text = hex_encode(text)
    # converting this hex representation to the base-10 representation
    return int(hex_text, 16)


def big_endian_decode(long: int) -> str:
    """
    decode a given long number to its alphabet representation using big-endian encoding
    """
    # converting the long number to its hex representation
    hex_text = hex(long)
    # converting this hex representation to the ascii representation
    return hex_decode(str(hex_text)[2:])


"""
These two functions exist in `Crypto.Util.number` as `bytes_to_long()` and `long_to_bytes()`
"""