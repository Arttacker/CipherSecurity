from math_algorithms.square_mult import square_and_multiply


def get_shared_key(p, alpha, a, b):
    shared_key = []

    A = square_and_multiply(alpha, a, p)
    B = square_and_multiply(alpha, b, p)

    KAB1 = square_and_multiply(B, a, p)
    KAB2 = square_and_multiply(A, b, p)

    shared_key.append(KAB1)
    shared_key.append(KAB2)

    return shared_key