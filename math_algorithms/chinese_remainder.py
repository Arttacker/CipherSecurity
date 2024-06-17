from functools import reduce
from math_algorithms.euclidean import mod_inv


def crt(a: list, n: list) -> int:
    """
    Solve the Chinese Remainder Theorem problem.

    :param n: List of pairwise coprime integers.
    :param a: List of remainders when the solution is divided by the corresponding integers in n.
    :return: The smallest non-negative solution x such that x ≡ a[i] (mod n[i]) for each i.
    """
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mod_inv(p, n_i) * p
    return sum % prod
