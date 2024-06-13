import unittest
from encoding.hex_encoding import *


plain_text1 = "Saleh is the Artacker"
cipher_text1 = "53616c6568206973207468652041727461636b6572"


plain_text2 = "Hacking i$ FUN!"
cipher_text2 = "4861636b696e672069242046554e21"


class TestHexEncoding(unittest.TestCase):

    def test_encoding1(self):
        cipher_text_out = hex_encode(plain_text1)
        self.assertEqual(cipher_text_out, cipher_text1)

    def test_encoding2(self):
        cipher_text_out = hex_encode(plain_text2)
        self.assertEqual(cipher_text_out, cipher_text2)

    def test_decoding1(self):
        plain_text_out = hex_decode(cipher_text1)
        self.assertEqual(plain_text_out, plain_text1)

    def test_decoding2(self):
        plain_text_out = hex_decode(cipher_text2)
        self.assertEqual(plain_text_out, plain_text2)
