import unittest
from math_algorithms.quadratic_residue import *


class TestSqrtModFunctions(unittest.TestCase):
    def test_sqrt_mod_sympy(self):
        self.assertTrue(sqrt_mod_sympy(4, 7) in [2, 5])
        self.assertTrue(sqrt_mod_sympy(10, 13) in [6, 7])
        self.assertTrue(sqrt_mod_sympy(5, 11) in [4, 7])
        self.assertIsNone(sqrt_mod_sympy(14, 29))

    def test_legendre_symbol(self):
        self.assertEqual(legendre_symbol(4, 7), 1)
        self.assertEqual(legendre_symbol(14, 29), -1)
        self.assertEqual(legendre_symbol(0, 13), 0)

    def test_sqrt_mod_tonelli_shanks(self):
        self.assertTrue(sqrt_mod_tonelli_shanks(4, 7) in [2, 5])
        self.assertTrue(sqrt_mod_tonelli_shanks(10, 13) in [6, 7])
        self.assertTrue(sqrt_mod_tonelli_shanks(5, 11) in [4, 7])
        self.assertIsNone(sqrt_mod_tonelli_shanks(14, 29))

    def test_sqrt_mod_fermat_little(self):
        self.assertTrue(sqrt_mod_fermat_little(4, 7) in [2, 5])
        self.assertTrue(sqrt_mod_fermat_little(5, 11) in [4, 7])
        self.assertIsNone(sqrt_mod_fermat_little(5, 15))

    def test_sqrt_mod_general(self):
        self.assertEqual(sqrt_mod_general(4, 7), (2, 5))
        self.assertEqual(sqrt_mod_general(10, 13), (7, 6))
        self.assertEqual(sqrt_mod_general(5, 11), (4, 7))
        self.assertEqual(sqrt_mod_general(0, 13), (None, None))
