import unittest
from encoding.big_endian_encoding import *


plain_text1 = "Saleh is the Artacker"
cipher_text1 = 121860825317489624041701948990587167270395720721778


plain_text2 = "crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}"
cipher_text2 = 11515195063862318899931685488813747395775516287289682636499965282714637259206269


class TestBigEndianEncoding(unittest.TestCase):

    def test_encoding1(self):
        cipher_text_out = big_endian_encode(plain_text1)
        self.assertEqual(cipher_text_out, cipher_text1)

    def test_encoding2(self):
        cipher_text_out = big_endian_encode(plain_text2)
        self.assertEqual(cipher_text_out, cipher_text2)

    def test_decoding1(self):
        plain_text_out = big_endian_decode(cipher_text1)
        self.assertEqual(plain_text_out, plain_text1)

    def test_decoding2(self):
        plain_text_out = big_endian_decode(cipher_text2)
        self.assertEqual(plain_text_out, plain_text2)
