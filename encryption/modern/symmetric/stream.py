from pwn import xor


def xor_encrypt(message, key):
    """
    Encrypts the message using XOR cipher with the given key.

    Args:
    - message (str): The message to be encrypted.
    - key (str): The key used for encryption.

    Returns:
    - str: The encrypted message in the form of hex string.
    """
    # Perform the XOR operation
    result = xor(message.encode(), key.encode()).hex()

    return result


def xor_decrypt(ciphertext, key):
    """
    Decrypts the message using XOR cipher with the given key.

    Args:
    - message (str): The message to be decrypted.
    - key (str): The key used for decryption.

    Returns:
    - str: The decrypted message in the form of normal string.
    """
    # Perform the XOR operation
    result = xor(bytes.fromhex(ciphertext), key.encode())

    return result.decode()


def analyse_with_known_flag_format(ciphertext, flag_format="flag{}"):
    """
        Cracks given ciphertext and construct the key, leveraging known parts of the plaintext (flag)
        Args:
        - ciphertext (str): The ciphertext to be decrypted.
        - flag_format (str): The known part of the plaintext (flag).

        Returns:
        - str: The decrypted message in the form of normal string.
    """
    # As we know part of the flag we can get the key by XoRing this known format with their corresponding in the cipher

    # Getting the corresponding ciphertext part to the first flag part
    first_cipher_part = ciphertext[:len(flag_format[:-1])*2]  # we are multiplying by 2 as each char is represented in two hex digits

    # Getting the corresponding ciphertext part to the second flag part
    second_cipher_part = ciphertext[-2:]

    # Concatenate the two parts that we have selected from the ciphertext
    selected_ciphertext = first_cipher_part + second_cipher_part

    key = xor(bytes.fromhex(selected_ciphertext), flag_format.encode()).decode()

    plaintext = xor_decrypt(ciphertext, key)
    return plaintext
