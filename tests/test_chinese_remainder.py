import unittest
from math_algorithms.chinese_remainder import crt


class TestChineseRemainderTheorem(unittest.TestCase):

    def test_basic_case(self):
        n = [3, 5, 7]
        a = [2, 3, 2]
        self.assertEqual(crt(a, n), 23)

    def test_single_congruence(self):
        n = [7]
        a = [5]
        self.assertEqual(crt(a, n), 5)

    def test_large_numbers(self):
        n = [101, 103, 107]
        a = [1, 2, 3]
        self.assertEqual(crt(a, n), 1066258)

    def test_non_coprime_moduli(self):
        n = [6, 8, 10]
        a = [4, 7, 9]
        with self.assertRaises(ValueError):
            crt(a, n)

    def test_no_solution_case(self):
        n = [2, 3, 5]
        a = [1, 2, 3]
        self.assertEqual(crt(a, n), 23)

    def test_zero_modulus(self):
        n = [3, 0, 7]
        a = [2, 3, 2]
        with self.assertRaises(ValueError):
            crt(a, n)