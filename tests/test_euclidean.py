import unittest
from math_algorithms.euclidean import gcd, extended_euclidean, mod_inv


class TestEuclideanAlgorithms(unittest.TestCase):

    def setUp(self):
        self.gcd_test_cases = [
            (12, 8, 4),
            (7, 17, 1),
            (84651167678, 46451131, 1),
            (52920, 66528, 1512)
        ]

        self.extended_euclidean_test_cases = [
            (26513, 32321, (1, 10245, -8404))
        ]

        self.mod_inverse_test_cases = [
            (8, 11, 7),
            (123456789, 12365, 3729),
            (13245687, 135469, 38164)
        ]

    def test_gcd(self):
        for a, b, expected in self.gcd_test_cases:
            with self.subTest(a=a, b=b, expected=expected):
                self.assertEqual(gcd(a, b), expected)

    def test_extended_euclidean(self):
        for a, b, expected in self.extended_euclidean_test_cases:
            with self.subTest(a=a, b=b, expected=expected):
                self.assertEqual(extended_euclidean(a, b), expected)

    def test_mod_inverse(self):
        for a, b, expected in self.mod_inverse_test_cases:
            with self.subTest(a=a, b=b, expected=expected):
                self.assertEqual(mod_inv(a, b), expected)
