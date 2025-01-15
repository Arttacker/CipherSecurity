import unittest
from encryption.modern.asymmetric.rsa import encrypt, decrypt


class TestRSA(unittest.TestCase):

    def test_encryption1(self):

        cipher_text_out = encrypt(11, 17, 88, 7)
        self.assertEqual(cipher_text_out, 11)

    def test_encryption2(self):

        cipher_text_out = encrypt(13, 19, 65, 5)
        self.assertEqual(cipher_text_out, 221)

    def test_encryption3(self):

        cipher_text_out = encrypt(61, 53, 70, 7)
        self.assertEqual(cipher_text_out, 2338)

    def test_encryption4(self):

        cipher_text_out = encrypt(257, 337, 18537, 17)
        self.assertEqual(cipher_text_out, 12448)

    def test_decryption1(self):

        plain_text_out = decrypt(11, 17, 11, 7)
        self.assertEqual(plain_text_out, 88)

    def test_decryption2(self):

        plain_text_out = decrypt(13, 19, 221, 5)
        self.assertEqual(plain_text_out, 65)

    def test_decryption3(self):

        plain_text_out = decrypt(61, 53, 2338, 7)
        self.assertEqual(plain_text_out, 70)

    def test_decryption4(self):

        plain_text_out = decrypt(257, 337, 12448, 17)
        self.assertEqual(plain_text_out, 18537)
