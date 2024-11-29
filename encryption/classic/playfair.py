def decrypt(cipherText, key):
    # Converting the Key and given text to Upper case letters.
    key = key.upper()
    cipherText = cipherText.upper()

    # print("[+] The Cipher Text is:", cipherText)
    # print("[+] The Key Text is:", key)

    plainText = ""

    # [1] Create 5X5 table that contains the key and the remaining alphabet letter.
    table = create_5x5_table(cipherText, key)
    # # printing the table in the console screen...
    # print_table(table)

    # [2] Splitting the given cipher text into pairs of letters.
    splittedText = split_text_2s(cipherText)

    # # printing the cipher text after splitting into pairs...
    # print_splitted_text(splittedText)

    # [3] Start decryption by:
    # [3.1] Taking each two letters and identifying their positions in the table
    for pair in splittedText:
        positionOfFirstLetterInTabl = get_letter_position(table, pair[0])
        i1, j1 = positionOfFirstLetterInTabl

        positionOfSecondLetterInTabl = get_letter_position(table, pair[1])
        i2, j2 = positionOfSecondLetterInTabl

        # If the two letters are in the same row
        if i1 == i2:
            i = i1  # To indicate the same row without confusion.

            decreptedPair = ""

            # Take the next left element in the row
            if j1 - 1 < 0:  # Check if this is the first item in the row
                decreptedPair += table[i][4]
            else:  # Take the next left element in the row
                decreptedPair += table[i][j1 - 1]

            if j2 - 1 < 0:  # Check if this is the first item in the row
                decreptedPair += table[i][4]
            else:  # Take the next left element in the row
                decreptedPair += table[i][j2 - 1]

            plainText = check_original_x_case(plainText, decreptedPair)
            # appending this ciphered pair to the main cipher text
            plainText += decreptedPair

        # If the two letters are in the same column
        elif j1 == j2:
            j = j1  # To indicate the same column without confusion.

            decreptedPair = ""

            # Take the next element above in the column
            if i1 - 1 < 0:  # Check if this is the first item in the column
                # take the last element in the column
                decreptedPair += table[4][j]
            else:  # Take the next element above in the column
                decreptedPair += table[i1 - 1][j]

            if i2 - 1 < 0:  # Check if this is the first item in the column
                # take the last element in the column
                decreptedPair += table[4][j]
            else:  # Take the next element above in the column
                decreptedPair += table[i2 - 1][j]

            plainText = check_original_x_case(plainText, decreptedPair)
            # appending this ciphered pair to the main cipher text
            plainText += decreptedPair
        # If the two letters are not in the same row or the same column
        else:
            decreptedPair = ""
            decreptedPair += table[i1][j2]
            decreptedPair += table[i2][j1]

            plainText = check_original_x_case(plainText, decreptedPair)
            plainText += decreptedPair

    # if the last letter of the plain text is 'X' we will assume that this 'X' is
    # resulted from adding it to complete the pair of letters in the encryption phase.
    if plainText.endswith("X"):
        plainText = plainText[:-1]
    # print("[+] The Decrepted Cipher is:", plainText, "\n\n")
    return plainText


def encrypt(plainText, key):
    # Converting the Key and given text to Upper case letters.
    key = key.upper()
    plainText = plainText.upper()

    # print("[+] The Plain Text is:", plainText)
    # print("[+] The Key Text is:", key)

    cipherText = ""

    # [1] Create 5X5 table that contains the key and the remaining alphabet letter.
    table = create_5x5_table(plainText, key)
    # # printing the table in the console screen...
    # print_table(table)

    # [2] Splitting the given plain text into pairs of letters.
    splittedText = split_text_2s(plainText)

    # # printing the plain text after splitting into pairs...
    # print_splitted_text(splittedText)

    # [3] Start encryption by:
    # [3.1] Taking each two letters and identifying their positions in the table
    for pair in splittedText:
        positionOfFirstLetterInTabl = get_letter_position(table, pair[0])
        i1, j1 = positionOfFirstLetterInTabl

        positionOfSecondLetterInTabl = get_letter_position(table, pair[1])
        i2, j2 = positionOfSecondLetterInTabl

        # If the two letters are in the same row
        if i1 == i2:
            i = i1  # To indicate the same row without confusion.

            cipheredPair = ""

            # Take the next right element in the row
            if j1 + 1 > 4:  # Check if this is the last item in the row
                cipheredPair += table[i][0]
            else:  # Take the next right element in the row
                cipheredPair += table[i][j1 + 1]

            if j2 + 1 > 4:  # Check if this is the last item in the row
                cipheredPair += table[i][0]
            else:  # Take the next right element in the row
                cipheredPair += table[i][j2 + 1]

            # appending this ciphered pair to the main cipher text
            cipherText += cipheredPair

        # If the two letters are in the same column
        elif j1 == j2:
            j = j1  # To indicate the same column without confusion.

            cipheredPair = ""

            # Take the next element below in the column
            if i1 + 1 > 4:  # Check if this is the last item in the column
                # take the first element in the column
                cipheredPair += table[0][j]
            else:  # Take the next element below in the column
                cipheredPair += table[i1 + 1][j]

            if i2 + 1 > 4:  # Check if this is the last item in the column
                # take the first element in the column
                cipheredPair += table[0][j]
            else:  # Take the next element below in the column
                cipheredPair += table[i2 + 1][j]

            # appending this ciphered pair to the main cipher text
            cipherText += cipheredPair
        # If the two letters are not in the same row or the same column
        else:
            cipheredPair = ""
            cipheredPair += table[i1][j2]
            cipheredPair += table[i2][j1]

            cipherText += cipheredPair

    # print("[+] The Cipher Text is:", cipherText, "\n\n")

    return cipherText


def handle_i_j_case(text, key):
    # handling the case of 'I' , 'J', as we should consider that if the key contains 'I' or 'J',
    # it should contain the one which is in the given input.
    # if the text to be encrypted/decrepted contains 'J', deal with 'J' in the key table
    # and if it contains 'I' instead, we should deal with 'I' in the key table
    # and all this is because the table is 5X5 and the alphabet letters are 26,
    # so we deal with 'I' or 'J', but NOT BOTH in the same key table.
    if 'I' in text and 'J' in key:
        key = key.replace('J', 'I')
    elif 'J' in text and 'I' in key:
        key = key.replace('I', 'J')
    return key


def create_5x5_table(text, key):
    # [1] Initialize the 5X5 table.
    table = [['' for _ in range(5)] for _ in range(5)]

    # [2.1] Getting the unique letters that exist in the key
    uniqueKeyLetters = get_unique_key_letters(text, key)
    # [2.2] Getting the letters that aren't exist in the key
    nonKeyLetters = get_non_key_letters(text, key)

    # [3] Distribute the key in its first indexes,
    # and the remained empty indexes will be filled with the alphabet that aren't in the key.

    currentkeyIndex = 0  # To track the current index of the key when inserting in the table.
    currentNonkeyIndex = 0  # To track the current index of the remaining alphabet letters when inserting in the table.

    for i in range(5):
        for j in range(5):
            # Check if the key is totally distributed on the table.
            if currentkeyIndex >= len(uniqueKeyLetters):
                # Start distributing the remained alphabet letters
                table[i][j] = nonKeyLetters[currentNonkeyIndex]
                currentNonkeyIndex += 1  # Move to the next character in the remained alphabet letters.
            else:
                # Start distributing the unique key letters.
                table[i][j] = uniqueKeyLetters[currentkeyIndex]
                currentkeyIndex += 1  # Move to the next character in the key

    return table


def get_non_key_letters(text, key):
    nonKeyLetters = []
    alphabet = ord('A')  # Start with 'A'

    for i in range(26):
        alphaLetter = chr(alphabet + i)
        if alphaLetter not in key:
            nonKeyLetters.append(alphaLetter)

    # Handling the 'I' AND 'J' cases in the remaining alphabet letters to be distributed
    key = handle_i_j_case(text, key)

    if 'I' in key:
        # this means that the text might contains 'I' or maybe not,
        # but we are sure that the text does not contain 'J',
        # as we handled it in the function above.
        nonKeyLetters.remove('J')
    elif 'J' in key:
        # this means that the text might contains 'J' or maybe not,
        # but we are sure that the text does not contain 'I',
        # as we handled it in the function above.
        nonKeyLetters.remove('I')
    else:
        # if the key does not contain 'I' or 'J',
        # so we will deal with 'I' by default in the key table and remove 'J'.
        nonKeyLetters.remove('J')

    return nonKeyLetters


def get_unique_key_letters(text, key):
    key = handle_i_j_case(text, key)

    uniqueKeyLetters = []

    for char in key:
        if char not in uniqueKeyLetters:
            uniqueKeyLetters.append(char)
    return uniqueKeyLetters


def print_table(table):
    print("[+] Key Table:\n")
    # Access and print elements of the table
    for row in table:
        print(' '.join(row))
    print()


def print_splitted_text(splittedText):
    print("[+] The Text After Splitting:", ' '.join(splittedText))
    print()


def split_text_2s(text):
    twoCharsList = []
    i = 0
    while i < len(text):
        twoChars = ""
        if i + 1 < len(text):
            if text[i] == text[i + 1]:
                if i + 2 < len(text):
                    twoChars = text[i] + "X"
                    twoCharsList.append(twoChars)

                    twoChars = text[i] + text[i + 2]
                    twoCharsList.append(twoChars)
                    i += 1
                else:
                    twoChars = text[i] + "X"
                    twoCharsList.append(twoChars)

                    twoChars = text[i + 1] + "X"
                    twoCharsList.append(twoChars)
            else:
                twoChars = text[i] + text[i + 1]
                twoCharsList.append(twoChars)
        else:
            twoChars = text[i] + "X"
            twoCharsList.append(twoChars)
        i += 2
    return twoCharsList


def get_letter_position(table, letter):
    for i, row in enumerate(table):
        for j, char in enumerate(row):
            if char == letter:
                return i, j
    return None


def check_original_x_case(text, pair):
    if len(text) > 1:
        if text[-2] == pair[0] and text[-1] == 'X':
            text = text[:-1]
    return text
