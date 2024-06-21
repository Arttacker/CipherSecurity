initial_permutation_table = [
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7,
    56, 48, 40, 32, 24, 16, 8, 0,
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6
]

permuted_choice1_table = [
    56, 48, 40, 32, 24, 16, 8,
    0, 57, 49, 41, 33, 25, 17,
    9, 1, 58, 50, 42, 34, 26,
    18, 10, 2, 59, 51, 43, 35,
    62, 54, 46, 38, 30, 22, 14,
    6, 61, 53, 45, 37, 29, 21,
    13, 5, 60, 52, 44, 36, 28,
    20, 12, 4, 27, 19, 11, 3
]

permuted_choice2_table = [
    13, 16, 10, 23, 0, 4,
    2, 27, 14, 5, 20, 9,
    22, 18, 11, 3, 25, 7,
    15, 6, 26, 19, 12, 1,
    40, 51, 30, 36, 46, 54,
    29, 39, 50, 44, 32, 47,
    43, 48, 38, 55, 33, 52,
    45, 41, 49, 35, 28, 31
]

expansion_table = [31, 0, 1, 2, 3, 4, 3, 4, 5, 6, 7, 8, 7, 8, 9, 10, 11, 12, 11, 12, 13, 14, 15, 16, 15, 16, 17, 18, 19,
                   20, 19, 20, 21, 22, 23, 24, 23, 24, 25, 26, 27, 28, 27, 28, 29, 30, 31, 0]

s_box1 = [
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
    [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]

s_box2 = [
    [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
    [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
    [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
    [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]

s_box3 = [
    [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
    [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
    [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
    [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]]

s_box4 = [
    [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
    [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
    [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
    [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]]

s_box5 = [
    [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
    [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
    [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
    [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]]

s_box6 = [
    [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
    [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
    [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
    [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]]

s_box7 = [
    [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
    [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
    [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
    [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]]

s_box8 = [
    [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
    [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
    [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
    [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]

permutation_box = [15, 6, 19, 20, 28, 11, 27, 16, 0, 14, 22, 25, 4, 17, 30, 9, 1, 7, 23, 13, 31, 26, 2, 8, 18, 12, 29, 5,
                   21, 10, 3, 24]

final_permutation_table = [39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
                           36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17,
                           57, 25, 32, 0, 40, 8, 48, 16, 56, 24]


def encrypt(plaintext, key):
    """
        Encrypts the given plaintext using the DES algorithm with the provided Hex key.

        Args:
            plaintext (str): The plaintext to be encrypted.
            key (str): The key used for encryption.

        Returns:
            str: The ciphertext obtained after encryption (in hexadecimal representation).
        """
    ciphertext = ''
    hex_plaintext = convert_text_to_hex(plaintext)
    hex_key = convert_text_to_hex(key)
    hex_key = divide_hex_into_blocks(hex_key)[0]
    hex_64_bits_blocks = divide_hex_into_blocks(hex_plaintext)

    for block in hex_64_bits_blocks:
        ciphertext += encrypt_hex_block(block, hex_key).replace('0x', '')

    return ciphertext


def decrypt(ciphertext, key):
    """
        Decrypts the given Hex ciphertext using the DES algorithm with the provided Hex key.

        Args:
            ciphertext (str): The ciphertext to be decrypted.
            key (str): The key used for decryption.

        Returns:
            str: The plaintext obtained after decryption (in hexadecimal representation).
        """
    plaintext = ''

    hex_key = convert_text_to_hex(key)
    hex_key = divide_hex_into_blocks(hex_key)[0]
    hex_64_bits_blocks = divide_hex_into_blocks(ciphertext)

    for block in hex_64_bits_blocks:
        plaintext += decrypt_hex_block(block, hex_key).replace('0x', '')

    return plaintext


def encrypt_hex_block(plaintext, key):
    """
    Encrypts the given Hex plaintext using the DES algorithm with the provided Hex key.

    Args:
            plaintext (str): The plaintext of the block to be encrypted.
            key (str): The key used for encryption.

        Returns:
            str: The ciphertext obtained after encryption (in hexadecimal representation).
    """
    # [0] Convert Hex To binary
    binary_plain = convert_hex_to_binary(plaintext)
    binary_key = convert_hex_to_binary(key)

    # [1] Initial Permutation
    permuted = initial_permutation(binary_plain)

    # [2] Prepare the 16 round_keys
    round_keys = generate_round_keys(binary_key)

    # [3] Apply the 16 rounds with the 16 keys
    # This is the input for each round, at the first round, the PC-1 is the input, then the output.txt of a round is the input for the next one.
    round_input = permuted
    round_output = ""
    for roundKey in round_keys:
        round_output = round(round_input, roundKey)
        round_input = round_output

    # Catching the output.txt after the 16 rounds.
    output_of16_rounds = round_output

    # [4] Swap the two 32-bit blocks of the output.txt
    L_output = output_of16_rounds[:32]
    R_output = output_of16_rounds[32:]

    swapped = R_output + L_output

    # [5] Apply the final permutation
    ciphered_block = final_permutation(swapped)

    return "0x" + convert_binary_to_hex(ciphered_block)


def decrypt_hex_block(ciphertext, key):
    """
    Decrypts the given Hex ciphertext using the DES algorithm with the provided Hex key.

    Args:
            ciphertext (str): The ciphertext to be decrypted.
            key (str): The key used for decryption.

        Returns:
            str: The plaintext obtained after decryption (in hexadecimal representation).
    """
    # [0] Convert To binary
    binary_cipher = convert_hex_to_binary(ciphertext)
    binary_key = convert_hex_to_binary(key)

    # [1] Initial Permutation
    permuted = initial_permutation(binary_cipher)

    # [2] Prepare the 16 round_keys
    round_keys = generate_round_keys(binary_key)

    # [3] Apply the 16 rounds with the 16 keys [BUT] in the INVERSE order !
    # This is the input for each round, at the first round, the PC-1 is the input, then the output.txt of a round is the input for the next one.
    round_input = permuted
    round_output = ""
    for i in range(15, -1, -1):
        round_output = round(round_input, round_keys[i])
        # Setting the input for the next round, which is the previous round output.txt.
        round_input = round_output

    # Catching the output.txt after the 16 rounds.
    output_of16_rounds = round_output

    # [4] Swap the two 32-bit blocks of the output.txt
    L_output = output_of16_rounds[:32]
    R_output = output_of16_rounds[32:]

    swapped = R_output + L_output

    # [5] Apply the final permutation
    ciphered_block = final_permutation(swapped)

    return "0x" + convert_binary_to_hex(ciphered_block)


def convert_text_to_hex(text):
    result_hex = ''
    for c in text:
        result_hex += str(hex(ord(c))[2:])

    return result_hex


def convert_hex_to_text(hexa):
    hexa = hexa.replace('0x', '')
    result_text = ''
    for i in range(0, len(hexa), 2):  # Provide start, stop, and step parameters
        result_text += chr(int(hexa[i:i+2], 16))  # Convert each pair of hex digits to their corresponding ASCII character

    return result_text


def divide_hex_into_blocks(hex_string):
    block_size = 64  # 64 bits
    hex_per_block = block_size // 4  # Each hex character represents 4 bits

    blocks = []
    for i in range(0, len(hex_string), hex_per_block):
        block = hex_string[i:i + hex_per_block].ljust(hex_per_block, '0')  # Pad with zeros if needed
        blocks.append(block)

    return blocks


def convert_hex_to_binary(hex_string):
    """
    Converts a hexadecimal string to a binary string.

    Args:
        hex_string (str): The hexadecimal string to be converted.

    Returns:
        str: The binary representation of the hexadecimal string.
    """

    # Remove the '0x' prefix if present
    if hex_string[0:2] in ['0x', '0X']:
        hex_string = hex_string[2:]

    binary_string = ''

    for digit in hex_string:
        # Map each digit to its binary representation
        binary = bin(int(digit, 16))[2:]

        # Ensure that each digit is represented in 4-bits
        binary = binary.zfill(4)
        binary_string += binary

    # Ensure that the returned binary string is divisible by 64
    if len(binary_string) % 64 != 0:
        zeros_to_be_padded = 64 - (len(binary_string) % 64)
        binary_string += '0' * zeros_to_be_padded

    return binary_string


def convert_binary_to_hex(binary_string):
    """
    Converts a binary string to a hexadecimal string.

    Args:
        binary_string (str): The binary string to be converted.

    Returns:
        str: The hexadecimal representation of the binary string.
    """

    hex_string = ''

    # Map each 4-bit chunk to its hex representation
    for i in range(0, len(binary_string), 4):
        hex_digit = format(int(binary_string[i:i + 4], 2), 'X')
        hex_string += hex_digit

    return hex_string


def XoR(binary1, binary2):
    """
    Performs a bitwise XOR operation between two binary strings.

    Args:
        binary1 (str): The first binary string.
        binary2 (str): The second binary string.

    Returns:
        str: The result of the bitwise XOR operation.
    """

    xor_result = ''

    for bit1, bit2 in zip(binary1, binary2):
        xor_result += '0' if bit1 == bit2 else '1'

    return xor_result


def initial_permutation(plain64_bit):
    """
    The first step applied to the plainText while encryption, Performs the initial permutation step on the given block.

    Args:
        plain64_bit (str): The 64-bit block of data to be permuted.

    Returns:
        str: The 64-bit block after the initial permutation.
    """

    permuted = ''

    for i in range(64):
        permuted += plain64_bit[initial_permutation_table[i]]

    return permuted


def permuted_choice1(key64_bit):
    """
    Performs the Permuted Choice 1 (PC-1) step on the given 64-bit key.

    Args:
        key64_bit (str): The 64-bit key to be permuted.

    Returns:
        str: The 56-bit key after the PC-1 step.
    """
    permuted_choice1 = ''
    for i in range(56):
        permuted_choice1 += key64_bit[permuted_choice1_table[i]]
    return permuted_choice1


def left_circular_shift(key28_bit, round_num):
    """
    Performs the left circular shift (LS) on a 28-bit key segment based on the round number.

    Args:
        key28_bit (str): The 28-bit key segment to be shifted.
        round_num (int): The round number for which the shift is being performed.

    Returns:
        str: The 28-bit key segment after the left circular shift.
    """
    rounds_to_shift_one_pos = [1, 2, 9, 16]
    if round_num in rounds_to_shift_one_pos:
        # Perform the left circular shift with one position
        shifted = key28_bit[1:] + key28_bit[0]
    else:
        # Perform the left circular shift with two positions
        shifted = key28_bit[2:] + key28_bit[:2]

    return shifted


def permuted_choice2(key56_bit, permuted_choice2_table):
    """
    Performs the Permuted Choice 2 (PC-2) step on the given 56-bit key.

    Args:
    - key56Bit (str): The 56-bit key to be permuted.
    - permutedChoice2Table (list): The permutation table for Permuted Choice 2.

    Returns:
    - str: The 48-bit round key after the Permuted Choice 2 step.
    """
    round_key = ''
    for i in range(48):
        round_key += key56_bit[permuted_choice2_table[i]]
    return round_key


def generate_round_keys(key64_bit):
    """
    Generates a list of round keys for use in the Data Encryption Standard (DES) algorithm based on the given 64-bit key.
    """
    # [1] Permuted Choice 1 (PC-1)
    permuted = permuted_choice1(key64_bit)

    # [2] Split the permuted key into C & D parts 28-bit each
    C = permuted[:28]
    D = permuted[28:]

    # [3] Create a list to store all the generated roundkeys
    round_keys = []

    # [4] Apply the left circular shift and  PC-2 on each 28-bit key segment pair, for all the rounds
    for i in range(1, 17):
        # Left Circular Shift
        C_shifted = left_circular_shift(C, i)
        D_shifted = left_circular_shift(D, i)

        # Concatenate the C_shifted and D_shifted
        shifted = C_shifted + D_shifted

        # Apply the PC-2 to get the permuted and selected 48-bit key
        roundKey = permuted_choice2(shifted, permuted_choice2_table)
        round_keys.append(roundKey)

        # Updating the C and D for generating the next round key
        C = C_shifted
        D = D_shifted

    return round_keys


def expand(input32_bit):
    """
    Expands a 32-bit input to a 48-bit output.txt using the expansion table specified by the Data Encryption Standard (DES) algorithm.
    """
    result48_bit = ""
    for i in range(48):
        result48_bit += input32_bit[expansion_table[i]]
    return result48_bit


def s_box(input6_bit, sbox_number):
    """
    Performs substitution using the specified S-box based on the given 6-bit input and S-box number.
    """
    # Get the row number
    row = input6_bit[0] + input6_bit[-1]
    row_num = int(row, 2)

    # Get the column number
    col = input6_bit[1:5]
    col_num = int(col, 2)

    # Index in the suitable S-box
    if sbox_number == 1:
        return format(s_box1[row_num][col_num], '04b')
    elif sbox_number == 2:
        return format(s_box2[row_num][col_num], '04b')
    elif sbox_number == 3:
        return format(s_box3[row_num][col_num], '04b')
    elif sbox_number == 4:
        return format(s_box4[row_num][col_num], '04b')
    elif sbox_number == 5:
        return format(s_box5[row_num][col_num], '04b')
    elif sbox_number == 6:
        return format(s_box6[row_num][col_num], '04b')
    elif sbox_number == 7:
        return format(s_box7[row_num][col_num], '04b')
    elif sbox_number == 8:
        return format(s_box8[row_num][col_num], '04b')
    else:
        return ""


def function_permutation(input):
    """
    Permutes the 32-bit output.txt coming from the s-box.
    """
    permuted = ""
    for i in range(32):
        permuted += input[permutation_box[i]]
    return permuted


def F_function(right32_bit, round_key):
    """
    Applies the core function of a single round on the given 32-bit right side using the provided 48-bit round key.
    """
    result = ""
    # [1] Expansion of 32-bit right side to be 48-bit
    expanded_R = expand(right32_bit)

    # [2] XOR the 48-bit roundKey with the expanded right side and ensure that the output.txt is 48-bit
    xor_result = XoR(expanded_R, round_key).zfill(48)

    # [3] S-boxes
    s_box_result = ""
    for i in range(0, len(xor_result), 6):
        s_box_result += s_box(xor_result[i:i + 6], (i // 6) + 1)

    # [4] Permutation
    result = function_permutation(s_box_result)

    return result


def round(block64_bit, round_key):
    """
    Performs a single round on the given 64-bit plaintext using the provided round key.
    """
    output = ""

    # [1] Split the input into Left & Right parts, 32-bit each
    L = block64_bit[:32]
    R = block64_bit[32:]

    # [2] Apply the function with the right side and the roundKey
    function_result = F_function(R, round_key)

    # [3] XOR the result with the left side and ensure that the result is 32-bit
    new_r = XoR(L, function_result).zfill(32)

    output += R
    output += new_r

    return output


def final_permutation(input):
    """
    Performs the final permutation on the input according to the Data Encryption Standard (DES) algorithm.
    """
    permuted = ""
    for i in range(64):
        permuted += input[final_permutation_table[i]]
    return permuted
