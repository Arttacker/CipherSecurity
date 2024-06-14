def extended_euclidean(a, b):
    """
    Computes the extended Euclidean algorithm to find the greatest common divisor (gcd)
    and the coefficients x and y satisfying ax + by = gcd(a, b).
    :param a: The first integer.
    :param b: The second integer.
    :return: A tuple containing the gcd of a and b, and the coefficients x and y.
    """
    # Base cases
    if b == 0:
        return a, 1, 0

    # Recursive call
    gcd, x1, y1 = extended_euclidean(b, a % b)

    # Update values
    x = y1
    y = x1 - (a // b) * y1

    return gcd, x, y


def gcd(a, b):
    """
    Computes the greatest common divisor (gcd) of two integers a and b.
    :param a: The first integer.
    :param b: The second integer.
    :return: The gcd of a and b.
    """
    return extended_euclidean(a, b)[0]


def mod_inv(a, b):
    """
    Computes the modular inverse of an integer a under modulo b.
    :param a: The integer.
    :param b: The modulo.
    :return: The modular inverse of a under modulo b.
    :raises ValueError: If the modular inverse does not exist.
    """
    gcd, u, v = extended_euclidean(a, b)
    if gcd != 1:
        raise ValueError(f"The modular inverse of {a} under modulo {b} does not exist.")
    return u % b
