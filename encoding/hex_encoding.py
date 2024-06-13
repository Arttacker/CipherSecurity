def hex_encode(text: str) -> str:
    """
    encode a given string into its hex representation.
    """
    return "".join(f"{ord(c):02x}" for c in text)


def hex_decode(text: str) -> str:
    """
    decode a given string of hex encoded text to its ascii alphabet format.
    """
    return bytes.fromhex(text).decode()