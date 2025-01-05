import unittest
from encryption.classic.railfence import encrypt, decrypt, analyze


plain_text1 = "meetmeaftertheparty"
cipher_text1 = "mematrhpryetefeteat"
key1 = 2

plain_text2 = "meetmeafterthepartyxx"
cipher_tex2 = "mtaehayemfrerxeettptx"
key2 = 3

plain_text3 = "nothingisasitseems"
cipher_tex3 = "NTIGSSTEMOHNIAISES".lower()
key3 = 2


class TestRailFenceCipher(unittest.TestCase):
    def test_encryption1(self):

        cipher_text_out = encrypt(plain_text1, key1)
        self.assertEqual(cipher_text_out.upper(), cipher_text1.upper())

    def test_encryption2(self):

        cipher_text_out = encrypt(plain_text2, key2)
        self.assertEqual(cipher_text_out.upper(), cipher_tex2.upper())

    def test_encryption3(self):

        cipher_text_out = encrypt(plain_text3, key3)
        self.assertEqual(cipher_text_out.upper(), cipher_tex3.upper())

    def test_decryption1(self):

        plain_text_out = decrypt(cipher_text1, key1)
        self.assertEqual(plain_text_out.upper(), plain_text1.upper())

    def test_decryption2(self):

        plain_text_out = decrypt(cipher_tex2, key2)
        self.assertEqual(plain_text_out.upper(), plain_text2.upper())

    def test_decryption3(self):

        plain_text_out = decrypt(cipher_tex3, key3)
        self.assertEqual(plain_text_out.upper(), plain_text3.upper())

    def test_analyze1(self):

        key = analyze(plain_text1, cipher_text1)
        self.assertEqual(key, key1)

    def test_analyze2(self):

        key = analyze(plain_text3, cipher_tex3)
        self.assertEqual(key, key3)
