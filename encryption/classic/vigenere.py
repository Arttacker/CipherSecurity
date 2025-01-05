def analyze_repeating_key(plainText, cipherText):
    plainText = plainText.lower()
    cipherText = cipherText.lower()
    key = ""

    # Determine the key by comparing plaintext and ciphertext
    for i in range(len(plainText)):
        if plainText[i].isalpha():  # Only analyze alphabetic characters
            shift = (ord(cipherText[i]) - ord(plainText[i])) % 26
            key += chr((shift + ord('a')))
        else:
            key += plainText[i]  # Keep non-alphabetic characters unchanged

    return key


def decrypt_repeating_key(encryptedText, key):
    encryptedText = encryptedText.lower()
    key = key.lower()
    encryptedTextLength = len(encryptedText)
    keyLength = len(key)
    newKey = ""

    # Generating the new key by repeating itself
    repeatedWord = encryptedTextLength // keyLength
    newKey += key * repeatedWord
    newKey += key[:encryptedTextLength % keyLength]

    # Decrypting the encrypted text using the new key
    decryptedText = ""
    for i in range(encryptedTextLength):
        char = encryptedText[i]
        if char.isalpha():  # Only decrypt alphabetic characters
            shift = ord(newKey[i]) - ord('a')  # Calculate shift value from the key
            decryptedChar = chr(((ord(char) - ord('a') - shift + 26) % 26) + ord('a'))
            decryptedText += decryptedChar
        else:
            decryptedText += char  # Keep non-alphabetic characters unchanged

    return decryptedText


def encrypt_repeating_key(plainText, key):
    plainText = plainText.lower()
    key = key.lower()
    plainTextLength = len(plainText)
    keyLength = len(key)
    newKey = ""

    # Generating the new key by repeating itself
    repeatedWord = plainTextLength // keyLength
    newKey += key * repeatedWord
    newKey += key[:plainTextLength % keyLength]

    # Encrypting the plaintext using the new key
    encryptedText = ""
    for i in range(plainTextLength):
        char = plainText[i]
        if char.isalpha():  # Only encrypt alphabetic characters
            shift = ord(newKey[i]) - ord('a')  # Calculate shift value from the key
            encryptedChar = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            encryptedText += encryptedChar
        else:
            encryptedText += char  # Keep non-alphabetic characters unchanged

    return encryptedText


def analyze_auto_key(plainText, decryptedText):
    plainText = plainText.lower()
    decryptedText = decryptedText.lower()
    key = ""

    # Determine the key by comparing plaintext and decrypted text
    for i in range(len(plainText)):
        if plainText[i].isalpha():  # Only analyze alphabetic characters
            shift = (ord(decryptedText[i]) - ord(plainText[i])) % 26
            key += chr((shift + ord('a')))
        else:
            key += plainText[i]  # Keep non-alphabetic characters unchanged

    return key


def decrypt_auto_key(encryptedText, key):
    encryptedText = encryptedText.lower()
    key = key.lower()
    encryptedTextLength = len(encryptedText)
    keyLength = len(key)
    newKey = key

    # Decrypting the encrypted text using the new key
    decryptedText = ""
    for i in range(encryptedTextLength):
        char = encryptedText[i]
        if char.isalpha():  # Only decrypt alphabetic characters
            shift = ord(newKey[i]) - ord('a')  # Calculate shift value from the key
            decryptedChar = chr(((ord(char) - ord('a') - shift + 26) % 26) + ord('a'))
            decryptedText += decryptedChar
            newKey += decryptedChar  # Update the new key with decrypted character
        else:
            decryptedText += char  # Keep non-alphabetic characters unchanged

    return decryptedText


def encrypt_auto_key(plainText, key):
    plainText = plainText.lower()
    key = key.lower()
    plainTextLength = len(plainText)
    keyLength = len(key)
    newKey = key + plainText  # Generate new key using autokey technique

    # Encrypting the plaintext using the new key
    encryptedText = ""
    for i in range(plainTextLength):
        char = plainText[i]
        if char.isalpha():  # Only encrypt alphabetic characters
            shift = ord(newKey[i]) - ord('a')  # Calculate shift value from the key
            encryptedChar = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            encryptedText += encryptedChar
        else:
            encryptedText += char  # Keep non-alphabetic characters unchanged

    return encryptedText


if __name__ == '__main__':
    print(encrypt_auto_key("computer", "hello"))
    print(decrypt_auto_key("jsxaivsd", "hello"))
    print(analyze_auto_key("computer", "jsxaivsd"))
