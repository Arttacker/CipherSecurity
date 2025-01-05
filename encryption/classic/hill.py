import string
from math_algorithms import euclidean

ALPHABET = string.ascii_uppercase


def encrypt(plain_text, key):
    encoded_plain_text = encode_text(plain_text, ALPHABET)
    encoded_key = encode_text(key, ALPHABET)

    cipher_text = encrypt_matrix(encoded_plain_text, encoded_key)
    return decode_text(cipher_text, ALPHABET)


def decrypt(cipher_text, key):
    encoded_cipher_text = encode_text(cipher_text, ALPHABET)
    encoded_key = encode_text(key, ALPHABET)

    plain_text = decrypt_matrix(encoded_cipher_text, encoded_key)
    return decode_text(plain_text, ALPHABET)


def analyze_2_by_2_key_text(plain_text, cipher_text):
    encoded_plain_text = encode_text(plain_text, ALPHABET)
    encoded_cipher_text = encode_text(cipher_text, ALPHABET)

    key = analyze_2_by_2_key_matrix(encoded_plain_text, encoded_cipher_text)
    return decode_text(key, ALPHABET)


def analyze_3_by_3_key_text(plain_3, cipher_3):
    encoded_plain_text = encode_text(plain_3, ALPHABET)
    encoded_cipher_text = encode_text(cipher_3, ALPHABET)

    key = analyze_3_by_3_key_matrix(encoded_plain_text, encoded_cipher_text)
    return decode_text(key, ALPHABET)


def encrypt_matrix(plain_text, key):
    cipher_text = []

    # [1] Calculate the key dimensions
    # Assuming the Key is NxN matrix given in the form of a list of integers
    N = int(len(key) ** 0.5)

    # [2] C = P*K mod 26
    cipher_text = matrix_matrix_multiplication_mod26(plain_text, key, N)

    return cipher_text


def decrypt_matrix(cipher_text, key):
    if not is_key_valid(key):
        raise Exception("InvalidKeyException")

    plain_text = []

    # [1] Calculate the key dimensions
    # Assuming the Key is NxN matrix given in the form of a list of integers
    N = int(len(key) ** 0.5)

    # [2] Calculating the inverse matrix of the key
    key_inverse = inverse_nxn(key)

    # [3] P = C*K^-1 mod 26
    plain_text = matrix_matrix_multiplication_mod26(cipher_text, key_inverse, N)

    return plain_text


def analyze_2_by_2_key_matrix(plain_text, cipher_text):
    # In the case of key is 2X2 we can try all the combinations of keys
    # and try to encrypt the plain text with it,
    # if we get the same cipher text, then that is the key used in the encryption process
    for a in range(26):
        for b in range(26):
            for c in range(26):
                for d in range(26):
                    # Generating a key for a new combination each iteration
                    key = [a, b, c, d]
                    # Encrypting the plain text with this key
                    encrypted = encrypt_matrix(plain_text, key)
                    # Compare the encrypted text using the new key with the original cipher
                    if encrypted == cipher_text:
                        return key
    # If no matching key is found, raise an exception
    raise Exception("InvalidAnalysisException")


def analyze_3_by_3_key_matrix(plain_3, cipher_3):
    key = []

    # This function is responsible for analyzing Hill cipher generated through a 3x3 Key matrix

    # We know that:
    # C = P * K      --> 1
    # P = C * C^-1   --> 2

    # We have P and C so to get K:
    # K = C * P^-1

    # [1] Getting the inverse for the plainText Matrix
    plain_text_inverse = inverse_nxn(plain_3)

    key = matrix_matrix_multiplication_mod26(transpose(cipher_3), plain_text_inverse, 3)

    return key


def is_key_valid(key):
    # Main logic of IsKeyValid function
    N = len(key) ** 0.5
    if len(key) % N != 0:  # The key is not a square matrix
        return False

    gcd = euclidean.gcd(det_nxn(key), 26)
    if gcd != 1:  # not relatively prime with 26
        return False

    return True


def mod26(number):
    if number >= 0:
        return number % 26
    else:
        return (number % 26) + 26


def encode_text(text, alphabet):
    text = text.upper()
    encoded_alphabet = []

    for letter in text:
        encoded_alphabet.append(alphabet.index(letter))

    return encoded_alphabet


def decode_text(encoded_text, alphabet):
    decoded_alphabet = ""

    for number in encoded_text:
        decoded_alphabet += alphabet[mod26(number)]

    return decoded_alphabet


def transpose(matrix):
    N = int(len(matrix) ** 0.5)  # Calculate the size of the square matrix
    transpose = []
    for i in range(N):
        for j in range(N):
            transpose.append(matrix[i + j * N])

    return transpose


def matrix_vector_multiplication(letters_vector, key):
    result = []
    N = len(letters_vector)
    # Applying multiplication of 1xN encoded letters vector with NxN key matrix
    # C = P*K mod 26, so the task of this function is to return (P*K)
    for i in range(N):
        value_to_be_added = 0
        for j in range(N):
            if i == 0:  # if this is the first iteration
                value_to_be_added += (letters_vector[j] * key[j])
            else:
                value_to_be_added += (letters_vector[j] * key[j + (i * N)])
        result.append(value_to_be_added)
    return result


def matrix_matrix_multiplication_mod26(matrix1, matrix2, N):
    # Check that these two matrices can be multiplied together
    # Getting the dimensions of matrix2, that matrix2 is a square matrix of MXM dimensions
    # We need to verify that N = M
    M = int(len(matrix2) ** 0.5)
    if N != M:
        raise Exception("These Two Matrices Cannot Be Multiplied Together")

    # Result should be (matrix1 * matrix2) mod 26
    result = []

    # For each N elements as a 1xN vector in the matrix1, apply matrix multiplication between them and matrix2.
    index = 0  # To track the index of matrix1.
    for i in range(0, len(matrix1), N):
        vector = matrix1[i:i + N]

        multiplication_result = matrix_vector_multiplication(vector, matrix2)
        for number in multiplication_result:
            result.append(mod26(number))

    return result


def matrix_matrix_multiplication(matrix1, matrix2, N):
    # Check that these two matrices can be multiplied together
    # Getting the dimensions of matrix2, that matrix2 is a square matrix of MXM dimensions
    # We need to verify that N = M
    M = int(len(matrix2) ** 0.5)
    if N != M:
        raise Exception("These Two Matrices Cannot Be Multiplied Together")

    # Result should be (matrix1 * matrix2)
    result = []

    # For each N elements as a 1xN vector in the matrix1, apply matrix multiplication between them and matrix2.
    index = 0  # To track the index of matrix1.
    for i in range(0, len(matrix1), N):
        vector = matrix1[i:i + N]

        multiplication_result = matrix_vector_multiplication(vector, matrix2)
        for number in multiplication_result:
            result.append(number)

    return result


def scalar_product(matrix, multiplier):
    # Multiply each element in the list with the multiplier
    for i in range(len(matrix)):
        matrix[i] = mod26(matrix[i] * multiplier)

    return matrix


def det_2x2(matrix):
    # Let matrix A = |a b|
    #                |c d|
    # The determinant of A is given by the formula: det(A) = ad - bc
    return (matrix[0] * matrix[3]) - (matrix[1] * matrix[2])


def inverse_2x2(matrix):
    # Let matrix A = |a b|
    #                |c d|
    # The inverse of A is given by the formula: 1/det(A) |d -b|
    #                                                    |-c a|

    # getting the determinant
    det = det_2x2(matrix)
    inverse = []

    # checking that the matrix is inversible
    if det != 0:
        inverse = [matrix[3] // det, -matrix[1] // det, -matrix[2] // det, matrix[0] // det]
    else:
        raise ValueError("The given matrix is irreversable.")

    return inverse


def minor(matrix, index):
    N = int(len(matrix) ** 0.5)  # Calculate the size of the square matrix
    sub_matrix = []

    # This function takes an NXN matrix and an index for the element that we need to cancel its row and column
    # and returns the remaining elements (minor) as a submatrix.
    for i in range(len(matrix)):
        # Check if this column should be neglected
        if i // N == index // N or i % N == index % N:
            continue
        sub_matrix.append(matrix[i])

    return sub_matrix


def det_nxn(matrix):
    # This functions is a recursive function that is responsible for
    # calculating the determinant of an NXN matrix.

    N = int(len(matrix) ** 0.5)  # Calculate the size of the square matrix

    # Base Case is when the matrix is a 2X2 matrix
    if N == 2:
        return det_2x2(matrix)

    det = 0
    sign = True  # will be used to handle changing the sign each iteration
    # True : +ve , False : -ve

    for i in range(0, len(matrix), N):
        if sign:
            det += matrix[i] * det_nxn(minor(matrix, i))
        else:
            det -= matrix[i] * det_nxn(minor(matrix, i))

        sign = not sign  # Change the sign each iteration, to be used in the next one.

    return det


def duplicate_2_columns_and_2_rows(matrix):
    # This function is responsible for duplicating two columns and rows in a given matrix
    # to use them in calculating the Adjoint of it.

    # [1] Duplicating the first two columns of a given matrix and putting them to the right of it
    duplicated = []

    # Assuming that it is an NXN matrix
    N = int(len(matrix) ** 0.5)

    # We need to duplicate the first two columns
    first_2_columns = matrix[:2 * N]

    # Append the first two columns to the end of the matrix
    matrix.extend(first_2_columns)

    # Add the duplicated elements to the 'duplicated' list
    duplicated.extend(matrix)

    # [2] Duplicating the first two rows of a given matrix and putting them to the bottom of it

    # The size of the matrix after duplicating it should be:
    dimension_of_duplicated_matrix = N + 2

    for i in range(dimension_of_duplicated_matrix):
        insertion_index = N + i * dimension_of_duplicated_matrix
        values_to_be_inserted_index = insertion_index - N
        duplicated.insert(insertion_index, duplicated[values_to_be_inserted_index])
        duplicated.insert(insertion_index + 1, duplicated[values_to_be_inserted_index + 1])

    return duplicated


def adjoint(matrix):
    # This function calculates the adjoint of a given matrix
    # [1] Duplicate first two columns and rows of the given matrix
    matrix = duplicate_2_columns_and_2_rows(matrix)

    # [2] Remove the first column and row from the duplicated matrix
    matrix = minor(matrix, 0)

    # Getting the dimension of the resulting matrix
    N = int(len(matrix) ** 0.5)

    # [3] Calculating the adjoint using the matrix after the two previous operations
    adjoint_matrix = []

    # Applying 2X2 determinant calculation on each 4 elements in the matrix
    for i in range(N - 1):
        for j in range(N - 1):
            index00 = i + (j * N)
            index01 = i + ((j + 1) * N)
            minor_determinant = [matrix[index00], matrix[index00 + 1], matrix[index01], matrix[index01 + 1]]

            adjoint_matrix.append(mod26(det_2x2(minor_determinant)))

    return adjoint_matrix


def inverse_nxn(matrix):
    inverse = []

    # Calculating the inverse of the given matrix,
    # which is defined by: inverse(K) = 1/det(K) * adj(K)

    # Calculate the matrix dimensions
    # Assuming the matrix is NxN matrix given in the form of a list of integers
    N = int(len(matrix) ** 0.5)

    # Check if the given matrix is a 2X2 matrix
    if N == 2:
        return inverse_2x2(matrix)

    # [1] Calculating the modulus 26 for the determinant of K
    det = mod26(det_nxn(matrix))

    # [2] Calculating the inverse of the determinant under mod 26 using the Extended Euclidean Algorithm
    inverse_det = euclidean.mod_inv(det, 26)

    # [3] Calculating the Adjoint of K
    adjoint_matrix = adjoint(matrix)

    # [4] Finally multiplying the inverse of the determinant with the adjoint matrix to get the inverse of the key
    inverse = scalar_product(adjoint_matrix, inverse_det)

    return inverse
