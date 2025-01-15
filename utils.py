def ascii_alpha_to_ord(text: str) -> str:
    """Convert input string to number representation."""
    return "".join(str(ord(c)) for c in text)


def ascii_alpha_to_binary(text):
    """Convert input string to binary representation."""
    return ''.join([f"{ord(c):08b}" for c in text])


