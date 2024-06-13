def hex_encode(text: str) -> str:
    return "".join(f"{ord(c):02x}" for c in text)


def hex_decode(text: str) -> str:
    return bytes.fromhex(text).decode()