# Base64 characters
BASE64_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def b64_encode(text: str) -> str:
    # Convert each character in the text to its ASCII value, then to a binary string
    binary_string = ''.join(f"{ord(char):08b}" for char in text)

    # Pad the binary string with zeros to make its length a multiple of 6
    padding_length = (6 - len(binary_string) % 6) % 6
    binary_string += '0' * padding_length

    # Split the binary string into 6-bit chunks
    chunks = [binary_string[i:i + 6] for i in range(0, len(binary_string), 6)]

    # Convert each 6-bit chunk to its corresponding Base64 character
    encoded_string = ''.join(BASE64_CHARS[int(chunk, 2)] for chunk in chunks)

    # Calculate the number of padding characters needed
    padding_chars = '=' * ((4 - len(chunks) % 4) % 4)

    return encoded_string + padding_chars


def b64_decode(text: str) -> str:
    # Remove padding characters and count them
    padding = text.count('=')
    text = text.rstrip('=')

    # Convert Base64 characters to binary
    binary_string = ''.join(f"{BASE64_CHARS.index(c):06b}" for c in text)

    # Adjust binary_string length according to padding
    if padding:
        binary_string = binary_string[:-padding * 2]

    # Split the binary string into 8-bit chunks
    byte_chunks = [binary_string[i:i + 8] for i in range(0, len(binary_string), 8)]

    # Convert each 8-bit chunk to the corresponding character
    decoded_string = ''.join(chr(int(chunk, 2)) for chunk in byte_chunks if len(chunk) == 8)

    return decoded_string


"""
These two functions exist in `base64` as `b64encode()` and `b64decode()`
"""