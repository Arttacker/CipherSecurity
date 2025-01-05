import unittest
from encryption.classic.vigenere import *


plain_text1 = "wearediscoveredsaveyourself"
cipher_text_repeat1 = "zicvtwqngrzgvtwavzhcqyglmgj"
cipher_text_auto1 = "zicvtwqngkzeiigasxstslvvwla"
key1 = "deceptive"

plain_text2 = "MICHIGANTECHNOLOGICALUNIVERSITY"
cipher_text_repeat2 = "TWWNPZOAASWNUHZBNWWGSNBVCSLYPMM"
cipher_text_auto2 = "TWWNPZOAFMEOVULBZMEHYIYWBMTSTNL"
key2 = "HOUGHTON"


class TestVigenereCipher(unittest.TestCase):

    def test_repeating_key_encryption1(self):

        cipher_text_out = encrypt_repeating_key(plain_text1, key1)
        self.assertEqual(cipher_text_out.upper(), cipher_text_repeat1.upper())

    def test_repeating_key_encryption2(self):

        cipher_text_out = encrypt_repeating_key(plain_text2, key2)
        self.assertEqual(cipher_text_out.upper(), cipher_text_repeat2.upper())

    def test_repeating_key_decryption1(self):

        plain_text_out = decrypt_repeating_key(cipher_text_repeat1, key1)
        self.assertEqual(plain_text_out.upper(), plain_text1.upper())

    def test_repeating_key_decryption2(self):

        plain_text_out = decrypt_repeating_key(cipher_text_repeat2, key2)
        self.assertEqual(plain_text_out.upper(), plain_text2.upper())

    def test_repeating_key_analyze1(self):

        key = analyze_repeating_key(plain_text1, cipher_text_repeat1)
        self.assertTrue(key1.upper() in key.upper())

    def test_repeating_key_analyze2(self):

        key = analyze_repeating_key(plain_text2, cipher_text_repeat2)
        self.assertTrue(key2.upper() in key.upper())

    def test_auto_key_encryption1(self):

        cipher_text_out = encrypt_auto_key(plain_text1, key1)
        self.assertEqual(cipher_text_out.upper(), cipher_text_auto1.upper())

    def test_auto_key_encryption2(self):

        cipher_text_out = encrypt_auto_key(plain_text2, key2)
        self.assertEqual(cipher_text_out.upper(), cipher_text_auto2.upper())

    def test_auto_key_decryption1(self):

        plain_text_out = decrypt_auto_key(cipher_text_auto1, key1)
        self.assertEqual(plain_text_out.upper(), plain_text1.upper())

    def test_auto_key_decryption2(self):

        plain_text_out = decrypt_auto_key(cipher_text_auto2, key2)
        self.assertEqual(plain_text_out.upper(), plain_text2.upper())

    def test_auto_key_analyze1(self):

        key = analyze_auto_key(plain_text1, cipher_text_auto1)
        self.assertTrue(key1.upper() in key.upper())

    def test_auto_key_analyze2(self):

        key = analyze_auto_key(plain_text2, cipher_text_auto2)
        self.assertTrue(key2.upper() in key.upper())

