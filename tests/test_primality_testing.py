import unittest
from math_algorithms.primality_testing import *


class TestPrimeFunctions(unittest.TestCase):
    def test_is_prime(self):
        # Test small non-prime numbers
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(-10))

        # Test small prime numbers
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))

        # Test small non-prime even and odd numbers
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))

        # Test some known prime numbers
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13))
        self.assertTrue(is_prime(17))
        self.assertTrue(is_prime(19))

        # Test some known non-prime numbers
        self.assertFalse(is_prime(15))
        self.assertFalse(is_prime(21))
        self.assertFalse(is_prime(25))
        self.assertFalse(is_prime(27))
        self.assertFalse(is_prime(35))

        # Test large prime number
        self.assertTrue(is_prime(7919))  # 7919 is a known prime

        # Test large non-prime number
        self.assertFalse(is_prime(8000))  # 8000 is not a prime