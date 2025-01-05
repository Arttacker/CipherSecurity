def analyze(plain_text, cipher_text):
    suitable_key = 2  # Initialize the best key with a default value
    min_key = 2  # Minimum key value to start with
    max_key = len(cipher_text) // 2  # Maximum key value (half the length of the ciphertext)

    # Iterate through possible key values
    for key in range(min_key, max_key + 1):
        # Encrypt the plaintext using the current key
        encrypted_text = encrypt(plain_text, key)

        # Check if the encrypted text matches the provided ciphertext
        if encrypted_text == cipher_text:
            # If a match is found, set the best key and break out of the loop
            suitable_key = key
            break

    # Return the best key found during analysis
    return suitable_key


def decrypt(cipher_text, key):
    # Convert the cipher text to lowercase for consistency
    cipher_text = cipher_text.lower()

    # Initialize a StringBuilder to store the plain text
    plain_text = ""

    # Calculate the length of each part of the cipher text when dividing it into segments based on the key
    p_t_length = calculate_p_t_length(cipher_text, key)

    # Create a 2D array to represent the cipher text table using the specified method (col-wise in this case)
    cipher_text_table = create_2d_array(cipher_text, p_t_length, key, "col-wise")

    # Copy the characters from the cipher text table into the plain text StringBuilder, column by column
    plain_text = copy_characters_table(cipher_text_table, key, p_t_length, "col-wise")

    # Return the plain text
    return plain_text


def encrypt(plain_text, key):
    # Convert the plaintext to uppercase for consistency
    plain_text = plain_text.upper()

    # Initialize a StringBuilder to store the ciphertext
    cipher_text = ""

    # Calculate the length of each part of the plaintext when dividing it into segments based on the key
    p_t_length = calculate_p_t_length(plain_text, key)

    # Create a 2D array to represent the plaintext table using the specified method (row-wise in this case)
    plain_text_table = create_2d_array(plain_text, p_t_length, key, "row-wise")

    # Copy the characters row by row from the plaintext table into the ciphertext StringBuilder
    cipher_text = copy_characters_table(plain_text_table, key, p_t_length, "row-wise")

    # Return the ciphertext
    return cipher_text


def calculate_p_t_length(text, key):
    # Calculate the length of each part of the plaintext when dividing it into segments based on the key
    segment_length = len(text) // key

    # If the division has a remainder, indicating that the length of each segment is not evenly divisible by the key
    if len(text) % key != 0:
        # Increment the segment length by 1 to accommodate the remaining characters
        segment_length += 1

    # Return the calculated segment length
    return segment_length


def create_2d_array(text, n_columns, depth, method):
    arr = [[' ' for _ in range(n_columns)] for _ in range(depth)]

    if method == "row-wise":
        text_pointer = 0
        for col in range(n_columns):
            for row in range(depth):
                if text_pointer < len(text):
                    arr[row][col] = text[text_pointer]
                    text_pointer += 1
    elif method == "col-wise":
        text_pointer = 0
        for row in range(depth):
            for col in range(n_columns):
                if text_pointer < len(text):
                    arr[row][col] = text[text_pointer]
                    text_pointer += 1

    return arr


def copy_characters_table(arr, depth, n_columns, method):
    if method == "row-wise":
        cipher_text = ""
        for row in range(depth):
            for col in range(n_columns):
                if arr[row][col] != ' ':
                    cipher_text += arr[row][col]
        return cipher_text
    elif method == "col-wise":
        plain_text = ""
        for col in range(n_columns):
            for row in range(depth):
                if arr[row][col] != ' ':
                    plain_text += arr[row][col]
        return plain_text

