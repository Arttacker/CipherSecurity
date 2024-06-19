import unittest
from encryption.modern.symmetric.DES import encrypt_hex_block, decrypt_hex_block, encrypt, decrypt, convert_hex_to_text

plaintext1 = "0x68656C6C6F20776F"
ciphertext1 = "0x4B1DFA463CCE98F4"
key1 = "0x717765727479"

plaintext2 = "0x596F7572206C6970"
ciphertext2 = "0xC0999FDDE378D7ED"
key2 = "0x0E329232EA6D0D73"

plaintext3 = "0x6D6573736167652E"
ciphertext3 = "0x7CF45E129445D451"
key3 = "0x38627974656B6579"

plaintext4 = "Saleh Adel is a professional hacker!"
ciphertext4 = "8402051B58C62B2FCB58443ECD05DFD17F38DADF8DF1DDCB8B5ACB600E54EAB7D694562104A5EAD6"
decrypted4 = "Saleh Adel is a professional hacker!\x00\x00\x00\x00"
key4 = "security"


class TestDES(unittest.TestCase):

    def test_encryption1(self):

        cipher_text_out = encrypt_hex_block(plaintext1, key1)
        self.assertEqual(cipher_text_out, ciphertext1)

    def test_encryption2(self):

        cipher_text_out = encrypt_hex_block(plaintext2, key2)
        self.assertEqual(cipher_text_out, ciphertext2)

    def test_encryption3(self):

        cipher_text_out = encrypt_hex_block(plaintext3, key3)
        self.assertEqual(cipher_text_out, ciphertext3)

    def test_encryption4(self):

        cipher_text_out = encrypt(plaintext4, key4)
        self.assertEqual(cipher_text_out, ciphertext4)

    def test_decryption1(self):

        plain_text_out = decrypt_hex_block(ciphertext1, key1)
        self.assertEqual(plain_text_out, plaintext1)

    def test_decryption2(self):

        plain_text_out = decrypt_hex_block(ciphertext2, key2)
        self.assertEqual(plain_text_out, plaintext2)

    def test_decryption3(self):

        plain_text_out = decrypt_hex_block(ciphertext3, key3)
        self.assertEqual(plain_text_out, plaintext3)

    def test_decryption4(self):

        plain_text_out = decrypt(ciphertext4, key4)
        self.assertEqual(convert_hex_to_text(plain_text_out),  decrypted4)
