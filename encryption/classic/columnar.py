from typing import List
from collections import defaultdict


def analyze(plain_text: str, cipher_text: str) -> List[int]:
    plain_text = plain_text.upper()
    cipher_text = cipher_text.upper()

    if not plain_text or not cipher_text:
        raise ValueError("Input strings cannot be empty")

    n_columns = calculate_columns_number(plain_text, cipher_text)
    if n_columns == 0:
        raise ValueError("Number of columns cannot be zero")

    depth = len(plain_text) // n_columns

    plain_text_table = create_2d_array(plain_text, n_columns, depth, "row-wise")
    cipher_text_table = create_2d_array(cipher_text, n_columns, depth, "col-wise")

    key_gen = list(range(1, n_columns + 1))

    for i in range(1):
        for j in range(n_columns):
            for k in range(n_columns):
                found = False
                if plain_text_table[i][j] == cipher_text_table[i][k]:
                    are_equal = True
                    for l in range(depth):
                        if plain_text_table[l][j] != cipher_text_table[l][k]:
                            are_equal = False
                            break
                    if are_equal:
                        key_gen[j] = k + 1
                        found = True
                if found:
                    break

    return key_gen


def calculate_columns_number(plain_text: str, cipher_text: str) -> int:
    occurrence = defaultdict(int)

    for letter in plain_text:
        occurrence[letter] += 1

    most_freq_col_num = 1  # Set a minimum of 1 column
    freq = defaultdict(int)

    for i in range(1, len(cipher_text)):
        index_before = plain_text.find(cipher_text[i - 1])
        for j in range(occurrence[cipher_text[i - 1]] - 1):
            temp = plain_text.find(cipher_text[i - 1], index_before + 1)
            index_before = temp if temp != -1 else index_before

        occurrence[cipher_text[i]] += 1
        index_present = plain_text.find(cipher_text[i])
        for j in range(occurrence[cipher_text[i]] - 1):
            temp = plain_text.find(cipher_text[i], index_present + 1)
            index_present = temp if temp != -1 else index_present

        distance = index_present - index_before if index_present > index_before else index_before - index_present

        freq[distance] += 1
        most_freq_col_num = max(1, distance) if freq[distance] > freq[most_freq_col_num] else most_freq_col_num

    return most_freq_col_num


def decrypt(cipher_text: str, key: List[int]) -> str:
    n_columns = len(key)
    depth = len(cipher_text) // n_columns

    cipher_text_reordered = list(cipher_text)

    for i in range(n_columns):
        for j in range(depth):
            index = i * depth + j
            cipher_text_reordered[index] = cipher_text[(key[i] - 1) * depth + j]

    plain_text_table = create_2d_array("".join(cipher_text_reordered), n_columns, depth, "col-wise")
    plain_text = ""

    for i in range(depth):
        for j in range(n_columns):
            plain_text += plain_text_table[i][j]

    return plain_text.lower()



def encrypt(plain_text: str, key: List[int]) -> str:
    plain_text = plain_text.upper()

    n_columns = len(key)
    depth = len(plain_text) // n_columns

    if len(plain_text) % n_columns != 0:
        depth += 1
        plain_text = pad_x(plain_text, (n_columns * depth) - len(plain_text))

    plain_text_table = create_2d_array(plain_text, n_columns, depth, "row-wise")
    cipher_text = list(plain_text)

    for i in range(n_columns):
        for j in range(depth):
            cipher_text[(key[i] - 1) * depth + j] = plain_text_table[j][i]

    return "".join(cipher_text)


def pad_x(plain_text: str, count: int) -> str:
    return plain_text + "X" * count


def create_2d_array(text: str, n_columns: int, depth: int, method: str) -> List[List[str]]:
    arr = [["" for _ in range(n_columns)] for _ in range(depth)]

    if method == "row-wise":
        text_pointer = 0
        for i in range(depth):
            for j in range(n_columns):
                arr[i][j] = text[text_pointer]
                text_pointer += 1
    elif method == "col-wise":
        text_pointer = 0
        for i in range(n_columns):
            for j in range(depth):
                arr[j][i] = text[text_pointer]
                text_pointer += 1

    return arr


if __name__ == '__main__':
    pass
