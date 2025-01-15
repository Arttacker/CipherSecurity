import unittest
from encryption.modern.asymmetric.elgamal import encrypt, decrypt


class TestRSA(unittest.TestCase):

    def test_encryption1(self):

        cipher_out = encrypt(7187, 4842, 4464, 19, 19)
        self.assertTrue(cipher_out[0] == 2781 and cipher_out[1] == 437)

    def test_encryption2(self):

        cipher_out = encrypt(6323, 4736, 2231, 58, 111)
        self.assertTrue(cipher_out[0] == 6066 and cipher_out[1] == 899)

    def test_decryption1(self):

        plain_text_out = decrypt(2781, 437, 191, 7187)
        self.assertEqual(plain_text_out, 19)

    def test_decryption2(self):

        plain_text_out = decrypt(6066, 899, 118, 6323)
        self.assertEqual(plain_text_out, 111)


