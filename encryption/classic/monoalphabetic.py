import random


def generate_random_key():
    """
    Generates a random monoalphabetic substitution key.

    Returns:
    dict: A dictionary representing the substitution key.
    """
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    shuffled_alphabet = alphabet.copy()
    random.shuffle(shuffled_alphabet)
    key = {alphabet[i]: shuffled_alphabet[i] for i in range(26)}
    return key


def encrypt(plaintext, key):
    """
    Encrypts the plaintext using a monoalphabetic substitution cipher with the given key.

    Args:
    plaintext (str): The plaintext to be encrypted.
    key (dict): The substitution key.

    Returns:
    str: The encrypted ciphertext.
    """
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.islower():
                encrypted_char = key[char]
            else:
                encrypted_char = key[char.lower()].upper()
        else:
            encrypted_char = char
        ciphertext += encrypted_char
    return ciphertext


def decrypt(ciphertext, key):
    """
    Decrypts the ciphertext encrypted with a monoalphabetic substitution cipher using the given key.

    Args:
    ciphertext (str): The ciphertext to be decrypted.
    key (dict): The substitution key.

    Returns:
    str: The decrypted plaintext.
    """
    reverse_key = {v: k for k, v in key.items()}
    return encrypt(ciphertext, reverse_key)


def frequency_analysis_single(ciphertext):
    """
    Performs frequency analysis on the ciphertext to deduce the substitution key.

    Args:
    ciphertext (str): The ciphertext to be analyzed.

    Returns:
    dict: A dictionary representing the most likely mapping of letters in the ciphertext to letters in the plaintext.
    """
    frequency_dict = {}
    for char in ciphertext:
        if char.isalpha():
            char = char.lower()
            frequency_dict[char] = frequency_dict.get(char, 0) + 1

    # Sort letters by frequency
    sorted_freq = sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)

    # Map the most frequent letters to most common English letters
    mapping = {}
    common_letters = 'etaoinshrdlcumwfgypbvkjxqz'
    for i in range(len(sorted_freq)):
        mapping[sorted_freq[i][0]] = common_letters[i]

    return mapping


def frequency_analysis_double(ciphertext):
    """
    Performs frequency analysis on the ciphertext to deduce the substitution key based on double-letters.

    Args:
    ciphertext (str): The ciphertext to be analyzed.

    Returns:
    dict: A dictionary representing the most likely mapping of double-letters in the ciphertext to letters in the plaintext.
    """
    frequency_dict = {}
    for i in range(len(ciphertext) - 1):
        double_letter = ciphertext[i:i + 2].lower()
        if double_letter.isalpha():
            frequency_dict[double_letter] = frequency_dict.get(double_letter, 0) + 1

    sorted_freq = sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)
    common_double_letters = ['th', 'he', 'in', 'er', 'an', 're', 'es', 'on', 'st', 'nt', 'en', 'at', 'ed', 'nd', 'to',
                             'or', 'ea', 'ti', 'ar', 'te', 'ng', 'al', 'it', 'as', 'is', 'ha', 'et', 'se', 'ou', 'of',
                             'le', 'sa', 've', 'ro', 'ra', 'ri', 'hi', 'ne', 'me', 'de', 'co', 'si', 'll', 'ta', 'li',
                             'ur', 'fo', 'ot', 'el', 'ac', 'pe', 'ct', 'we', 'ca', 'ut']

    # Determine the length of the mapping based on the shorter list
    min_length = min(len(sorted_freq), len(common_double_letters))

    # Map pairs based on the shorter list
    mapping = {}
    for i in range(min_length):
        mapping[sorted_freq[i][0]] = common_double_letters[i]
    return mapping


def frequency_analysis_triple(ciphertext):
    """
    Performs frequency analysis on the ciphertext to deduce the substitution key based on triple-letters.

    Args:
    ciphertext (str): The ciphertext to be analyzed.

    Returns:
    dict: A dictionary representing the most likely mapping of triple-letters in the ciphertext to letters in the plaintext.
    """
    frequency_dict = {}
    for i in range(len(ciphertext) - 2):
        triple_letter = ciphertext[i:i + 3].lower()
        if triple_letter.isalpha():
            frequency_dict[triple_letter] = frequency_dict.get(triple_letter, 0) + 1

    sorted_freq = sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)
    common_triple_letters = ['the', 'and', 'tha', 'ent', 'ion', 'tio', 'for', 'nde', 'has', 'nce', 'edt', 'tis', 'oft',
                             'sth', 'men', 'tht', 'sto', 'itd', 'hey', 'oth', 'ser', 'led', 'his', 'ter', 'wth', 'sth',
                             'oth', 'sth', 'ing', 'hat', 'ent', 'ion', 'ere', 'onf', 'nce', 'hal', 'nth', 'was', 'eth',
                             'ofa', 'ers', 'ith', 'thi', 'ath', 'fth', 'ion', 'tth', 'sio', 'ted', 'ser', 'rth']

    # Determine the length of the mapping based on the shorter list
    min_length = min(len(sorted_freq), len(common_triple_letters))

    # Map triples based on the shorter list
    mapping = {}
    for i in range(min_length):
        mapping[sorted_freq[i][0]] = common_triple_letters[i]

    return mapping


def decrypt_with_single_mapping(ciphertext, mapping):
    """
    Decrypts the ciphertext using the given mapping.

    Args:
    ciphertext (str): The ciphertext to be decrypted.
    mapping (dict): The mapping of letters in the ciphertext to letters in the plaintext.

    Returns:
    str: The decrypted plaintext.
    """
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            char_lower = char.lower()
            decrypted_char = mapping.get(char_lower, char_lower)
            if char.isupper():
                decrypted_char = decrypted_char.upper()
        else:
            decrypted_char = char
        decrypted_text += decrypted_char

    return decrypted_text


def decrypt_with_double_mapping(ciphertext, mapping):
    """
    Decrypts the ciphertext using the given mapping of double letters mapped to another double letters.

    Args:
    ciphertext (str): The ciphertext to be decrypted.
    mapping (dict): The mapping of double-letters in the ciphertext to letters in the plaintext.

    Returns:
    str: The decrypted plaintext.
    """
    decrypted_text = ciphertext.lower()  # Convert ciphertext to lowercase for case-insensitive comparison

    # Replace each double-letter pair with its corresponding mapping from the dictionary
    for double_letter, replacement in mapping.items():
        decrypted_text = decrypted_text.replace(double_letter, replacement)

    # Convert decrypted text to uppercase where necessary
    decrypted_text = ''.join(replacement.upper() if original.isupper() else replacement for original, replacement in
                             zip(ciphertext, decrypted_text))

    return decrypted_text


def decrypt_with_triple_mapping(ciphertext, mapping):
    """
    Decrypts the ciphertext using the given mapping of triple letters mapped to another triple letters.

    Args:
    ciphertext (str): The ciphertext to be decrypted.
    mapping (dict): The mapping of triple-letters in the ciphertext to letters in the plaintext.

    Returns:
    str: The decrypted plaintext.
    """
    decrypted_text = ciphertext.lower()  # Convert ciphertext to lowercase for case-insensitive comparison

    # Replace each triple-letter sequence with its corresponding mapping from the dictionary
    for triple_letter, replacement in mapping.items():
        decrypted_text = decrypted_text.replace(triple_letter, replacement)

    # Convert decrypted text to uppercase where necessary
    decrypted_text = ''.join(replacement.upper() if original.isupper() else replacement for original, replacement in
                             zip(ciphertext, decrypted_text))

    return decrypted_text


def known_plaintext_attack(plaintext, ciphertext):
    """
    Performs a known plaintext attack on a monoalphabetic substitution cipher to deduce the substitution key.

    Args:
    plaintext (str): The known plaintext.
    ciphertext (str): The corresponding ciphertext.

    Returns:
    dict: A dictionary representing the inferred mapping of letters in the ciphertext to letters in the plaintext.
    """
    mapping = {}
    for plain_char, cipher_char in zip(plaintext, ciphertext):
        if plain_char.isalpha() and cipher_char.isalpha():
            plain_char = plain_char.lower()
            cipher_char = cipher_char.lower()
            mapping[cipher_char] = plain_char

    return mapping


########################################################
#     Also Use Grammarly For Better Cracking 😈🧠
########################################################
