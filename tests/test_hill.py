import unittest
from encryption.classic.hill import encrypt, decrypt, analyze_2_by_2_key_text, analyze_3_by_3_key_text

plain_text1 = "fvcfcqtob"
cipher_text1 = "hgrzeudvq"
key1 = "bkaaubcpc"

plain_text2 = "paymoremoney"
cipher_text2 = "tqssypkoqviw"
key2 = "dcif"

cipher_text3 = "lnshdlewmtrw"
key3 = "rrfvsvcct"

invalid_plain_text = "lkdi"
invalid_cipher_text = "sdek"


class TestHillCipher(unittest.TestCase):

    def test_encryption1(self):

        cipher_text_out = encrypt(plain_text1, key1)
        self.assertEqual(cipher_text_out.upper(), cipher_text1.upper())

    def test_encryption2(self):

        cipher_text_out = encrypt(plain_text2, key2)
        self.assertEqual(cipher_text_out.upper(), cipher_text2.upper())

    def test_encryption3(self):

        cipher_text_out = encrypt(plain_text2, key3)
        self.assertEqual(cipher_text_out.upper(), cipher_text3.upper())

    def test_decryption1(self):

        plain_text_out = decrypt(cipher_text1, key1)
        self.assertEqual(plain_text_out.upper(), plain_text1.upper())

    def test_decryption2(self):

        plain_text_out = decrypt(cipher_text2, key2)
        self.assertEqual(plain_text_out.upper(), plain_text2.upper())

    def test_decryption3(self):

        plain_text_out = decrypt(cipher_text3, key3)
        self.assertEqual(plain_text_out.upper(), plain_text2.upper())

    def test_analyze_2_by_2_key_text(self):

        analyzed_key = analyze_2_by_2_key_text(plain_text2, cipher_text2)
        self.assertEqual(analyzed_key.upper(), key2.upper())

    def test_analyze_3_by_3_key_text(self):

        analyzed_key = analyze_3_by_3_key_text(plain_text1, cipher_text1)
        self.assertEqual(analyzed_key.upper(), key1.upper())

    def test_invalid_analysis1(self):
        with self.assertRaises(Exception):
            key = analyze_2_by_2_key_text(invalid_plain_text, invalid_cipher_text)
        self.assertEqual(" ", " ")

    def test_invalid_analysis2(self):
        with self.assertRaises(Exception):
            key = analyze_3_by_3_key_text(invalid_plain_text, invalid_cipher_text)


if __name__ == '__main__':
    unittest.main()
