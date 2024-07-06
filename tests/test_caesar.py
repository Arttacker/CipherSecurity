import unittest
from encryption.classic.caesar import encrypt, decrypt, analyze_known_plaintext_attack


plain_text1 = "meetmeaftertheparty"
cipher_text1 = "phhwphdiwhuwkhsduwb"
key1 = 3

plain_text2 = "defendtheeastwallofthecastle"
cipher_text2 = "defendtheeastwallofthecastle"
key2 = 0

plain_text3 = "defendtheeastwallofthecastle"
cipher_text3 = "bcdclbrfccyqruyjjmdrfcayqrjc"
key3 = 24


plain_text4 = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
cipher_text4 = "WKHTXLFNEURZQIRAMXPSVRYHUWKHODCBGRJ"
key4 = 3


class TestCaesarCipher(unittest.TestCase):
    def test_encryption1(self):

        cipher_text_out = encrypt(plain_text1, key1)
        self.assertEqual(cipher_text_out.upper(), cipher_text1.upper())

    def test_encryption2(self):

        cipher_text_out = encrypt(plain_text2, key2)
        self.assertEqual(cipher_text_out.upper(), cipher_text2.upper())

    def test_encryption3(self):

        cipher_text_out = encrypt(plain_text3, key3)
        self.assertEqual(cipher_text_out.upper(), cipher_text3.upper())

    def test_encryption4(self):

        cipher_text_out = encrypt(plain_text4, key4)
        self.assertEqual(cipher_text_out.upper(), cipher_text4.upper())

    def test_decryption1(self):

        plain_text_out = decrypt(cipher_text1, key1)
        self.assertEqual(plain_text_out.upper(), plain_text1.upper())

    def test_decryption2(self):

        plain_text_out = decrypt(cipher_text2, key2)
        self.assertEqual(plain_text_out.upper(), plain_text2.upper())

    def test_decryption3(self):

        plain_text_out = decrypt(cipher_text3, key3)
        self.assertEqual(plain_text_out.upper(), plain_text3.upper())

    def test_decryption4(self):

        plain_text_out = decrypt(cipher_text4, key4)
        self.assertEqual(plain_text_out.upper(), plain_text4.upper())

    def test_analysis1(self):
        key = analyze_known_plaintext_attack(plain_text1, cipher_text1)
        self.assertEqual(key, key1)

    def test_analysis2(self):
        key = analyze_known_plaintext_attack(plain_text2, cipher_text2)
        self.assertEqual(key, key2)

    def test_analysis3(self):
        key = analyze_known_plaintext_attack(plain_text3, cipher_text3)
        self.assertEqual(key, key3)

    def test_analysis4(self):
        key = analyze_known_plaintext_attack(plain_text4, cipher_text4)
        self.assertEqual(key, key4)

