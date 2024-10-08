import unittest
from encryption.classic.columnar import encrypt, decrypt, analyze

mainPlain1 = "attackpostponeduntiltwoam"
mainPlain2 = "attackpostponeduntiltwoamxxx"
mainPlain3 = "computerscience"
mainPlain4 = "computersciencex"
newPlain = "defendtheeastwallofthecastleee"

mainCipher1 = "ttnaaptmtsuoaodwcoiknlpet"
mainCipher2 = "ttnaaptmtsuoaodwcoixknlxpetx"
mainCipher3 = "ctipscoeemrnuce"
mainCipher4 = "cusnpremeieotcc"
mainCipher5 = "cusnprexmeieotcc"
newCipher = "nalceehwttdttfseeleedsoaefeahl"

mainkey = [4, 3, 1, 2, 5, 6, 7]
mainkey1 = [1, 3, 4, 2, 5]
mainkey2 = [1, 4, 3, 2]
newKey = [3, 2, 6, 4, 1, 5]


class TestColumnarCipher(unittest.TestCase):

    def test_encryption1(self):
        cipher_text_out = encrypt(mainPlain1, mainkey)
        self.assertIn(cipher_text_out.upper(), [mainCipher1.upper(), mainCipher2.upper()])

    def test_encryption2(self):
        cipher_text_out = encrypt(mainPlain3, mainkey1)
        self.assertIn(cipher_text_out.upper(), [mainCipher3.upper()])

    def test_encryption3(self):
        cipher_text_out = encrypt(mainPlain3, mainkey2)
        self.assertIn(cipher_text_out.upper(), [mainCipher4.upper(), mainCipher5.upper()])

    def test_encryption4(self):
        cipher_text_out = encrypt(newPlain, newKey)
        self.assertEqual(cipher_text_out.upper(), newCipher.upper())

    def test_decryption1(self):
        plain_text_out1 = decrypt(mainCipher1, mainkey)
        plain_text_out2 = decrypt(mainCipher2, mainkey)
        self.assertTrue(
            (plain_text_out1.upper() == mainPlain1.upper()) or (plain_text_out2.upper() == mainPlain2.upper()))

    def test_decryption2(self):
        plain_text_out = decrypt(mainCipher3, mainkey1)
        self.assertEqual(plain_text_out.upper(), mainPlain3.upper())

    def test_decryption3(self):
        plain_text_out1 = decrypt(mainCipher4, mainkey2)
        plain_text_out2 = decrypt(mainCipher5, mainkey2)
        self.assertTrue(
            (plain_text_out1.upper() == mainPlain3.upper()) or (plain_text_out2.upper() == mainPlain4.upper()))

    def test_decryption4(self):
        plain_text_out = decrypt(newCipher, newKey)

        self.assertEqual(plain_text_out.upper(), newPlain.upper())

    def test_analyze1(self):
        key1 = analyze(mainPlain1, mainCipher1)
        key2 = analyze(mainPlain2, mainCipher2)
        self.assertTrue((key1 == mainkey) or (key2 == mainkey))

    def test_analyze2(self):
        key = analyze(mainPlain3, mainCipher3)
        self.assertEqual(key, mainkey1)

    def test_analyze3(self):
        key1 = analyze(mainPlain3, mainCipher4)
        key2 = analyze(mainPlain4, mainCipher5)
        self.assertTrue((key1 == mainkey2) or (key2 == mainkey2))

    def test_analyze4(self):
        key = analyze(newPlain, newCipher)
        self.assertEqual(key, newKey)
