def encrypt(plaintext, shift):
    """
    Encrypts the plaintext using the Caesar Cipher with the given shift.

    Args:
    plaintext (str): The plaintext to be encrypted.
    shift (int): The number of positions each letter should be shifted in the alphabet.

    Returns:
    str: The encrypted ciphertext.
    """
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():  # Check if the character is a letter
            shift_amount = shift % 26  # Ensure the shift is within the range of the alphabet
            if char.islower():
                encrypted_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                encrypted_char = chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
        else:
            encrypted_char = char  # Keep non-alphabetic characters unchanged
        ciphertext += encrypted_char
    return ciphertext


def decrypt(ciphertext, shift):
    """
    Decrypts the ciphertext encrypted with the Caesar Cipher using the given shift.

    Args:
    ciphertext (str): The ciphertext to be decrypted.
    shift (int): The number of positions each letter was shifted in the alphabet.

    Returns:
    str: The decrypted plaintext.
    """
    return encrypt(ciphertext, -shift)


def analyze_brute_force(ciphertext):
    """
    Brute-force attack to decrypt a Caesar Cipher ciphertext.

    Args:
    ciphertext (str): The ciphertext to be decrypted.

    Returns:
    dict: A dictionary containing possible decrypted plaintexts with corresponding shift values.
    """
    possible_plaintexts = {}
    for shift in range(26):
        decrypted_text = decrypt(ciphertext, shift)
        possible_plaintexts[shift] = decrypted_text
    return possible_plaintexts


def analyze_known_plaintext_attack(plaintext, ciphertext):
    """
    Determines the Caesar cipher shift used to encrypt the plaintext to the given ciphertext pair.
    """
    key = None
    for i in range(26):
        decrypted_text = decrypt(ciphertext, i)
        if decrypted_text == plaintext:
            key = i
            break
    return key
