from sympy import sqrt_mod


def sqrt_mod_sympy(a, p):
    """
    Compute the square root of 'a' modulo 'p' using the sympy library.

    Parameters:
    a (int): The integer for which the square root is to be found.
    p (int): A prime number.

    Returns:
    int: The square root of 'a' modulo 'p' , or None if no solution exists.
    """
    return sqrt_mod(a, p)


def legendre_symbol(a, p):
    """
    Compute the Legendre symbol (a/p).

    Parameters:
    a (int): The integer.
    p (int): A prime number.

    Returns:
    int: 1 if 'a' is a quadratic residue modulo 'p',
        -1 if 'a' is a non-quadratic residue modulo 'p',
         0 if 'a' is divisible by 'p'.
    """

    ls = pow(a, (p - 1) // 2, p)
    return -1 if ls == p - 1 else ls


def sqrt_mod_tonelli_shanks(a, p):
    """
    Compute the square root of 'a' modulo 'p' using the Tonelli-Shanks algorithm.

    Parameters:
    a (int): The integer for which the square root is to be found.
    p (int): A prime number.

    Returns:
    int: The square root of 'a' modulo 'p', or 0 if no solution exists.
    """
    # Base cases
    if legendre_symbol(a, p) != 1 or a == 0 or p == 2:
        return None
    elif p % 4 == 3:
        return pow(a, (p + 1) // 4, p)

    # Initialize variables
    s = p - 1
    e = 0
    while s % 2 == 0:
        s //= 2
        e += 1

    n = 2
    while legendre_symbol(n, p) != -1:
        n += 1

    # Main loop of the algorithm
    x = pow(a, (s + 1) // 2, p)
    b = pow(a, s, p)
    g = pow(n, s, p)
    r = e

    while True:
        t = b
        m = 0
        for m in range(r):
            if t == 1:
                break
            t = pow(t, 2, p)

        if m == 0:
            return x

        gs = pow(g, 2 ** (r - m - 1), p)
        g = (gs * gs) % p
        x = (x * gs) % p
        b = (b * g) % p
        r = m


def sqrt_mod_fermat_little(a, p):
    """
        Find the square root of a modulo prime p.
        Assumes p = 3 mod 4.
        """
    if legendre_symbol(a, p) != 1:
        return None  # No square root exists

    # Using Fermat's little theorem: a^((p+1)/4) (mod p)
    return pow(a, (p + 1) // 4, p)


def sqrt_mod_bruteforce(a, p):
    """
    Compute the square root of 'n' modulo 'p' if it exists using brute-forcing
    Parameters:
    n (int): The integer for which the square root is to be found.
    p (int): A prime number.

    Returns:
    list or None: A list containing the two square roots of 'n' modulo 'p' if they exist, otherwise None.
    """
    if legendre_symbol(a, p) != 1:
        return None
    else:
        result = []
        for i in range(1, p):
            if i**2 % p == a:
                result.append(i)
    return result


def sqrt_mod_general(a, p):
    """
    Compute both square roots of 'a' modulo prime 'p'.

    Parameters:
    a (int): The integer for which the square roots are to be found.
    p (int): A prime number.

    Returns:
    tuple: A tuple containing the two square roots of 'a' modulo 'p', or (None, None) if no solution exists.
    """
    if legendre_symbol(a, p) != 1 or a == 0 or p == 2:
        return None, None
    else:
        if p % 4 == 3:
            first_root = sqrt_mod_fermat_little(a, p)
            second_root = p - first_root
            return first_root, second_root
        else:
            first_root = sqrt_mod_tonelli_shanks(a, p)
            second_root = p - first_root
            return first_root, second_root
