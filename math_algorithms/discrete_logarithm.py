import math


def baby_step_giant_step(g, h, p):
    # Baby step
    m = math.ceil(math.sqrt(p))
    baby_steps = {}
    for j in range(m):
        baby_steps[pow(g, j, p)] = j

    # Precompute g^(-m) mod p
    g_m = pow(g, m * (p - 2), p)  # Using Fermat's Little Theorem for modular inverse

    # Giant step
    for i in range(m):
        y = (h * pow(g_m, i, p)) % p
        if y in baby_steps:
            return i * m + baby_steps[y]

    return None  # Logarithm not found


if __name__ == '__main__':
    # Example usage
    g = 5
    h = 3
    p = 23
    x = baby_step_giant_step(g, h, p)
    print(f"The discrete logarithm of {h} base {g} mod {p} is {x}")
