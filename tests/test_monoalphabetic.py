import unittest
from encryption.classic.monoalphabetic import *


class TestMonoalphaCipher(unittest.TestCase):

    def setUp(self):
        self.plaintext = "Hello World"
        self.key = generate_random_key()
        self.ciphertext = encrypt(self.plaintext, self.key)

    def test_generate_random_key(self):
        key = generate_random_key()
        self.assertEqual(len(key), 26)  # Ensure the key length is correct
        self.assertEqual(len(set(key.values())), 26)  # Ensure all letters are mapped uniquely

    def test_encryption(self):
        encrypted_text = encrypt(self.plaintext, self.key)
        self.assertEqual(encrypted_text, self.ciphertext)  # Ensure encrypted text matches ciphertext

    def test_decryption(self):
        decrypted_text = decrypt(self.ciphertext, self.key)
        self.assertEqual(decrypted_text, self.plaintext)  # Ensure decrypted text matches plaintext

    def test_known_plaintext_attack(self):
        known_plaintext = "This is a known plaintext to try doing the attack"
        known_ciphertext = encrypt(known_plaintext, self.key)
        mapping = known_plaintext_attack(known_plaintext, known_ciphertext)
        decrypted_text = decrypt_with_single_mapping(self.ciphertext, mapping)
        self.assertEqual(decrypted_text, self.plaintext)  # Ensure decrypted text matches plaintext


if __name__ == '__main__':
    unittest.main()
