import unittest
from encoding.leet_encoding import *


plain_text1 = "Saleh is the Artacker"
plain_text11 = "Saleh ls the Artacker"
simple_cipher_text1 = "5413H 15 7H3 4r74CK3r"
complex_cipher_text1 = r"5413# !5 7#3 4|274<|<3|2"


plain_text2 = "take care of the cipherwar"
plain_text22 = "take care of the clpherwar"
simple_cipher_text2 = "74K3 C4r3 0F 7H3 C1PH3rW4r"
complex_cipher_text2 = r"74|<3 <4|23 0|= 7#3 <!|*#3|2\^/4|2"


class TestLeetEncoding(unittest.TestCase):

    def test_simple_encoding1(self):
        cipher_text_out = simple_leet_encode(plain_text1)
        self.assertEqual(cipher_text_out.upper(), simple_cipher_text1.upper())

    def test_simple_encoding2(self):
        cipher_text_out = simple_leet_encode(plain_text2)
        self.assertEqual(cipher_text_out.upper(), simple_cipher_text2.upper())

    def test_simple_decoding1(self):
        plain_text_out = simple_leet_decode(simple_cipher_text1)
        self.assertTrue(plain_text_out.upper() == plain_text1.upper()
                        or plain_text_out.upper() == plain_text11.upper())

    def test_simple_decoding2(self):
        plain_text_out = simple_leet_decode(simple_cipher_text2)
        self.assertTrue(plain_text_out.upper() == plain_text2.upper()
                        or plain_text_out.upper() == plain_text22.upper())

    def test_complex_encoding1(self):
        cipher_text_out = complex_leet_encode(plain_text1)
        self.assertEqual(cipher_text_out, complex_cipher_text1)

    def test_complex_encoding2(self):
        cipher_text_out = complex_leet_encode(plain_text2)
        self.assertEqual(cipher_text_out, complex_cipher_text2)

    def test_complex_decoding1(self):
        plain_text_out = complex_leet_decode(complex_cipher_text1)
        self.assertEqual(plain_text_out, plain_text1.upper())

    def test_complex_decoding2(self):
        plain_text_out = complex_leet_decode(complex_cipher_text2)
        self.assertEqual(plain_text_out, plain_text2.upper())