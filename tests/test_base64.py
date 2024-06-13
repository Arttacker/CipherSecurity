import unittest
from encoding.base64_encoding import *


plain_text1 = "Saleh is the Artacker"
cipher_text1 = "U2FsZWggaXMgdGhlIEFydGFja2Vy"


plain_text2 = "Base 64 is great for web apps"
cipher_text2 = "QmFzZSA2NCBpcyBncmVhdCBmb3Igd2ViIGFwcHM="


class TestBase64Encoding(unittest.TestCase):

    def test_encoding1(self):
        cipher_text_out = b64_encode(plain_text1)
        self.assertEqual(cipher_text_out, cipher_text1)

    def test_encoding2(self):
        cipher_text_out = b64_encode(plain_text2)
        self.assertEqual(cipher_text_out, cipher_text2)

    def test_decoding1(self):
        plain_text_out = b64_decode(cipher_text1)
        self.assertEqual(plain_text_out, plain_text1)

    def test_decoding2(self):
        plain_text_out = b64_decode(cipher_text2)
        self.assertEqual(plain_text_out, plain_text2)
