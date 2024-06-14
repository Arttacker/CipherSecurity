import unittest
from encryption.modern.symmetric.stream import *


plain_text1 = "Saleh is the Artacker"
cipher_text1 = "30180e001a530c105506011159220b160411180011"
key1 = "cybersecurity"

plain_text2 = "Hacking i$ FUN!"
cipher_text2 = "200000000000004808474b2f3b2949"
key2 = "hacking"

plain_text3 = "crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}"
cipher_text3 = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
flag_format = "crypto{}"


class TestSteamCipher(unittest.TestCase):

    def test_encryption1(self):
        cipher_text_out = xor_encrypt(plain_text1, key1)
        self.assertEqual(cipher_text_out, cipher_text1)

    def test_encryption2(self):
        cipher_text_out = xor_encrypt(plain_text2, key2)
        self.assertEqual(cipher_text_out, cipher_text2)

    def test_decryption1(self):
        plain_text_out = xor_decrypt(cipher_text1, key1)
        self.assertEqual(plain_text_out, plain_text1)

    def test_decryption2(self):
        plain_text_out = xor_decrypt(cipher_text2, key2)
        self.assertEqual(plain_text_out, plain_text2)

    def test_analyse_with_known_flag_format(self):
        plain_text_out = analyse_with_known_flag_format(cipher_text3, flag_format)
        self.assertEqual(plain_text_out, plain_text3)
