from math_algorithms.euclidean import mod_inv
from math_algorithms.square_mult import square_and_multiply


def encrypt(p, alpha, beta, i, m):
    cipher_text = []

    # [1] Compute the Ephemeral key (KE) = alpha^i mod p
    KE = square_and_multiply(alpha, i, p)

    # [2] Compute the Masking key (KM) = beta^i mod p
    KM = square_and_multiply(beta, i, p)

    # [3] Encrypting the message
    cipher = (KM * m) % p

    cipher_text.append(KE)
    cipher_text.append(cipher)

    return cipher_text


def decrypt(KE, c, d, p):
    plain_text = 0

    # [1] Compute the Masking key (KM) = (KE)^d mod p
    KM = square_and_multiply(KE, d, p)

    # [2] Compute the inverse of KM
    KM_inverse = mod_inv(KM, p)

    # [3] Decrypting the ciphertext with the KM_Inverse
    plain_text = (c * KM_inverse) % p

    return plain_text


