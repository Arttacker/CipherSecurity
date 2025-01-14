s_box = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

inv_s_box = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
)

rcon = (
    [0x01, 0x00, 0x00, 0x00], [0x02, 0x00, 0x00, 0x00],
    [0x04, 0x00, 0x00, 0x00], [0x08, 0x00, 0x00, 0x00],
    [0x10, 0x00, 0x00, 0x00], [0x20, 0x00, 0x00, 0x00],
    [0x40, 0x00, 0x00, 0x00], [0x80, 0x00, 0x00, 0x00],
    [0x1b, 0x00, 0x00, 0x00], [0x36, 0x00, 0x00, 0x00]
)


def hex_to_matrix(hex_str):
    # Remove any leading '0x' if present
    if hex_str.startswith("0x"):
        hex_str = hex_str[2:]

    # Ensure the string length is even for proper byte representation
    if len(hex_str) % 2 != 0:
        hex_str = "0" + hex_str

    # Pad the hex string with zeroes if it's less than 32 characters
    hex_str = hex_str.ljust(32, '0')

    # Convert the hex string into a list of bytes
    hex_bytes = [int(hex_str[i:i + 2], 16) for i in range(0, len(hex_str), 2)]

    # Create a 4x4 matrix
    matrix = []
    for i in range(0, 16, 4):
        matrix.append(hex_bytes[i:i + 4])

    return matrix


def matrix_to_hex(matrix):
    # Flatten the 2D matrix into a single list
    flat_list = [item for sublist in matrix for item in sublist]

    # Convert each decimal value to a 2-digit hexadecimal string
    hex_str = ''.join(f'{value:02x}' for value in flat_list)

    return hex_str


def split_hex_string(hex_str):
    # Remove any leading '0x' if present
    if hex_str.startswith("0x"):
        hex_str = hex_str[2:]

    # Ensure the string length is even for proper byte representation
    if len(hex_str) % 2 != 0:
        hex_str = "0" + hex_str

    # Split the hex string into substrings of 32 characters (16 bytes) each
    substrings = [hex_str[i:i + 32] for i in range(0, len(hex_str), 32)]

    return substrings


def transpose_state(s):
    """ Transposes a given 4x4 state """
    return [[s[j][i] for j in range(4)] for i in range(4)]


def add_round_key(s, k):
    c = []
    # XoRing each row in the state with the corresponding row in the key
    ciphered_row = []
    for i in range(4):
        for j in range(4):
            ciphered_row.append(s[i][j] ^ k[i][j])
        c.append(ciphered_row)
        ciphered_row = []
    return c


def convert_state_to_hex(s):
    new_state = [['' for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            new_state[i][j] = hex(s[i][j])[2:]
    return new_state


def sub_bytes(s, sbox):
    new_state = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            new_state[i][j] = sbox[s[i][j]]
    return new_state


def shift_rows(s):
    new_state = [[0 for _ in range(4)] for _ in range(4)]
    new_state[0] = s[0]  # First row remains unchanged
    new_state[1] = s[1][1:] + s[1][:1]  # Shift second row left by 1
    new_state[2] = s[2][2:] + s[2][:2]  # Shift third row left by 2
    new_state[3] = s[3][3:] + s[3][:3]  # Shift fourth row left by 3
    return new_state


def inv_shift_rows(s):
    new_state = [[0 for _ in range(4)] for _ in range(4)]
    new_state[0] = s[0]  # First row remains unchanged
    new_state[1] = s[1][-1:] + s[1][:-1]  # Shift second row right by 1
    new_state[2] = s[2][-2:] + s[2][:-2]  # Shift third row right by 2
    new_state[3] = s[3][-3:] + s[3][:-3]  # Shift fourth row right by 3
    return new_state


def gmul(a, b):
    """Function to perform Galois Field multiplication of two bytes"""
    p = 0
    hi_bit_set = 0
    for _ in range(8):
        if b & 1:
            p ^= a
        hi_bit_set = a & 0x80
        a <<= 1
        if hi_bit_set:
            a ^= 0x1b  # 0x1b is the irreducible polynomial used in AES
        b >>= 1
    return p & 0xFF


def mix_columns(s):
    # AES mix_columns matrix
    mix_col_matrix = [
        [0x02, 0x03, 0x01, 0x01],
        [0x01, 0x02, 0x03, 0x01],
        [0x01, 0x01, 0x02, 0x03],
        [0x03, 0x01, 0x01, 0x02]
    ]

    # Create a new state matrix to store the result
    new_state = [[0 for _ in range(4)] for _ in range(4)]

    # Perform matrix multiplication
    for c in range(4):
        for r in range(4):
            new_state[r][c] = (
                    gmul(mix_col_matrix[r][0], s[0][c]) ^
                    gmul(mix_col_matrix[r][1], s[1][c]) ^
                    gmul(mix_col_matrix[r][2], s[2][c]) ^
                    gmul(mix_col_matrix[r][3], s[3][c])
            )

    return new_state


def inv_mix_columns(s):
    # AES inv_mix_columns matrix
    inv_mix_col_matrix = [
        [0x0e, 0x0b, 0x0d, 0x09],
        [0x09, 0x0e, 0x0b, 0x0d],
        [0x0d, 0x09, 0x0e, 0x0b],
        [0x0b, 0x0d, 0x09, 0x0e]
    ]

    # Create a new state matrix to store the result
    new_state = [[0 for _ in range(4)] for _ in range(4)]

    # Perform matrix multiplication
    for c in range(4):
        for r in range(4):
            new_state[r][c] = (
                    gmul(inv_mix_col_matrix[r][0], s[0][c]) ^
                    gmul(inv_mix_col_matrix[r][1], s[1][c]) ^
                    gmul(inv_mix_col_matrix[r][2], s[2][c]) ^
                    gmul(inv_mix_col_matrix[r][3], s[3][c])
            )

    return new_state


def sub_word(word, sbox):
    return [sbox[b] for b in word]


def rot_word(word):
    return word[1:] + word[:1]


def key_expansion(key, sbox):
    key = transpose_state(key)
    key_schedule = [[0] * 4 for _ in range(44)]

    for r in range(4):
        for c in range(4):
            key_schedule[r][c] = key[r][c]

    for r in range(4, 44):
        temp = key_schedule[r - 1].copy()
        if r % 4 == 0:
            temp = sub_word(rot_word(temp), sbox)
            temp[0] ^= rcon[r // 4 - 1][0]
        for c in range(4):
            key_schedule[r][c] = key_schedule[r - 4][c] ^ temp[c]

    return [transpose_state(key_schedule[i:i + 4]) for i in range(0, len(key_schedule), 4)]


def encrypt_ordinals_state(state, key):
    """Takes state and key as 2d Matrixes of ordinals and returns the ciphered state as a 2d Matrixes of ordinals"""
    round_keys = key_expansion(key, sbox=s_box)
    state = add_round_key(state, round_keys[0])

    for round in range(1, 10):
        state = sub_bytes(state, sbox=s_box)
        state = shift_rows(state)
        state = mix_columns(state)
        state = add_round_key(state, round_keys[round])

    state = sub_bytes(state, sbox=s_box)
    state = shift_rows(state)
    state = add_round_key(state, round_keys[10])

    return state


def decrypt_ordinals_state(state, key):
    """Takes state and key as 2d Matrixes of ordinals and returns the decrypted state as a 2d Matrix of ordinals"""
    round_keys = key_expansion(key, sbox=s_box)
    state = add_round_key(state, round_keys[10])

    for round in range(10 - 1, 0, -1):
        state = inv_shift_rows(state)
        state = sub_bytes(state, sbox=inv_s_box)
        state = add_round_key(state, round_keys[round])
        state = inv_mix_columns(state)

    state = inv_shift_rows(state)
    state = sub_bytes(state, sbox=inv_s_box)
    state = add_round_key(state, round_keys[0])

    return state


def encrypt(plaintext, key):
    """Takes plaintext and key as stings in hexadecimal and returns the ciphertext in hexadecimal"""
    ciphertext = ''
    states = split_hex_string(plaintext)
    # Convert hex key to a 2d matrix of ordinals
    key = hex_to_matrix(key)
    # for each state convert it to a 2d matrix and encrypt it and appending the result to the ciphertext
    for state in states:
        state = hex_to_matrix(state)
        ciphertext += matrix_to_hex(encrypt_ordinals_state(state, key))
    return "0x" + ciphertext


def decrypt(ciphertext, key):
    """Takes ciphertext and key as stings in hexadecimal and returns the plaintext in hexadecimal"""
    plaintext = ''
    states = split_hex_string(ciphertext)
    # Convert hex key to a 2d matrix of ordinals
    key = hex_to_matrix(key)
    # for each state convert it to a 2d matrix and decrypt it and appending the result to the plaintext
    for state in states:
        state = hex_to_matrix(state)
        plaintext += matrix_to_hex(decrypt_ordinals_state(state, key))
    return "0x" + plaintext
