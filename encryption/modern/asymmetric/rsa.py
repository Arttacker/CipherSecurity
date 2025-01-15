from math_algorithms.euclidean import mod_inv
from math_algorithms.square_mult import square_and_multiply


def encrypt(p, q, m, e):
    cipher_text = 0

    # [1] Compute n = p x q
    n = p * q

    # [2] Encrypt the Message by using the Square-And-Multiply algorithm for getting the power under modulo n
    cipher_text = square_and_multiply(m, e, n)

    return cipher_text


def decrypt(p, q, c, e):
    plain_text = 0

    # [1] Compute n = p x q
    n = p * q

    # [2] Compute phi(n) = (p - 1)(q - 1)
    phi_n = (p - 1) * (q - 1)

    # [3] Compute d (private key) and this is the inverse of e
    # Using the Extended Euclidean Algorithm to get the inverse(e) under modulo phi(n)
    d = mod_inv(e, phi_n)

    # [4] Decrypt the Message by using the Square-And-Multiply algorithm for getting the power under modulo n
    plain_text = square_and_multiply(c, d, n)

    return plain_text