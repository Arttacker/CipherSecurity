def square_and_multiply(number, exponent, modulus):
    """
    Computes fast exponentiation using the Square-and-Multiply algorithm.
    :param number: The base number.
    :param exponent: The exponent.
    :param modulus: The modulus.
    :return: The result of base number raised to the power of exponent modulo modulus.
    """
    # Initialize the result to 1
    result = 1

    # Loop until the exponent becomes 0
    while exponent > 0:
        # If the current bit (LSP) of the exponent is 1
        if exponent % 2 == 1:
            # Multiply the result by the base and take modulus
            result = (result * number) % modulus

        # Square the base and take modulus
        number = (number * number) % modulus

        # Divide the exponent by 2 (right shift) (drop LSP)
        exponent = exponent // 2

    # Return the final result
    return result
