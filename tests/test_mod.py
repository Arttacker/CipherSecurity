import unittest
from math_algorithms.mod import mod_


class TestModFunction(unittest.TestCase):
    def test_mod_positive(self):
        # Test positive a and b
        self.assertEqual(mod_(10, 3), 1)
        self.assertEqual(mod_(10, 5), 0)
        self.assertEqual(mod_(10, 7), 3)

    def test_mod_negative_a(self):
        # Test negative a and positive b
        self.assertEqual(mod_(-10, 3), 2)
        self.assertEqual(mod_(-10, 5), 0)
        self.assertEqual(mod_(-10, 7), 4)

    def test_mod_edge_cases(self):
        # Test when a or b is zero
        self.assertEqual(mod_(0, 3), 0)
        self.assertEqual(mod_(3, 3), 0)
        self.assertEqual(mod_(5, 1), 0)

    def test_mod_large_numbers(self):
        # Test with large numbers
        self.assertEqual(mod_(123456789, 123), 90)
        self.assertEqual(mod_(-987654321, 123), 9)

    def test_mod_special_cases(self):
        # Test special cases
        self.assertEqual(mod_(-1, 1), 0)
        self.assertEqual(mod_(-1, 2), 1)
        self.assertEqual(mod_(-2, 2), 0)