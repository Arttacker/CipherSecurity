import unittest
from encryption.modern.symmetric.AES_128 import *


round_1_key = [
    [160, 136, 35, 42, ],
    [250, 84, 163, 108, ],
    [254, 44, 57, 118, ],
    [23, 177, 57, 5, ],
]
round_1_plaintext_state = [
    [25, 160, 154, 233],
    [61, 244, 198, 248],
    [227, 226, 141, 72],
    [190, 43, 42, 8]
]


main_key = [
        [43, 40, 171, 9, ],
        [126, 174, 247, 207, ],
        [21, 210, 21, 79, ],
        [22, 166, 136, 60, ]
]

main_plaintext_state = [
        [50, 136, 49, 224, ],
        [67, 90, 49, 55, ],
        [246, 48, 152, 7, ],
        [168, 141, 162, 52, ],
]

main_ciphertext_state = [
        [57, 2, 220, 25],
        [37, 220, 17, 106],
        [132, 9, 133, 11],
        [29, 251, 151, 50],
]

plaintext1 = "0x328831e0435a3137f6309807a88da234"
ciphertext1 = "0x3902dc1925dc116a8409850b1dfb9732"
key1 = "0x2b28ab097eaef7cf15d2154f16a6883c"


class TestAES(unittest.TestCase):

    def test_aes_encryption_round(self):
        substituted = sub_bytes(round_1_plaintext_state, sbox=s_box)

        self.assertEqual(
            substituted, [[212, 224, 184, 30], [39, 191, 180, 65], [17, 152, 93, 82], [174, 241, 229, 48]]
        )

        shifted = shift_rows(substituted)
        self.assertEqual(
            shifted, [[212, 224, 184, 30], [191, 180, 65, 39], [93, 82, 17, 152], [48, 174, 241, 229]]
        )

        mixed = mix_columns(shifted)
        self.assertEqual(
            mixed, [[4, 224, 72, 40], [102, 203, 248, 6], [129, 25, 211, 38], [229, 154, 122, 76]]
        )

        ciphered = add_round_key(mixed, round_1_key)
        self.assertEqual(
            ciphered, [[164, 104, 107, 2], [156, 159, 91, 106], [127, 53, 234, 80], [242, 43, 67, 73]]
        )

    def test_add_round_key(self):
        added_round_key = add_round_key(main_plaintext_state, main_key)
        self.assertEqual(added_round_key, [[25, 160, 154, 233], [61, 244, 198, 248], [227, 226, 141, 72], [190, 43, 42, 8, ]])

    def test_key_expansion(self):
        round_keys = key_expansion(main_key, sbox=s_box)
        self.assertEqual(round_keys,
                         [[[43, 40, 171, 9], [126, 174, 247, 207], [21, 210, 21, 79], [22, 166, 136, 60]],
                          [[160, 136, 35, 42], [250, 84, 163, 108], [254, 44, 57, 118], [23, 177, 57, 5]],
                          [[242, 122, 89, 115], [194, 150, 53, 89], [149, 185, 128, 246], [242, 67, 122, 127]],
                          [[61, 71, 30, 109], [128, 22, 35, 122], [71, 254, 126, 136], [125, 62, 68, 59]],
                          [[239, 168, 182, 219], [68, 82, 113, 11], [165, 91, 37, 173], [65, 127, 59, 0]],
                          [[212, 124, 202, 17], [209, 131, 242, 249], [198, 157, 184, 21], [248, 135, 188, 188]],
                          [[109, 17, 219, 202], [136, 11, 249, 0], [163, 62, 134, 147], [122, 253, 65, 253]],
                          [[78, 95, 132, 78], [84, 95, 166, 166], [247, 201, 79, 220], [14, 243, 178, 79]],
                          [[234, 181, 49, 127], [210, 141, 43, 141], [115, 186, 245, 41], [33, 210, 96, 47]],
                          [[172, 25, 40, 87], [119, 250, 209, 92], [102, 220, 41, 0], [243, 33, 65, 110]],
                          [[208, 201, 225, 182], [20, 238, 63, 99], [249, 37, 12, 12], [168, 137, 200, 166]]]
        )

    def test_state_encryption(self):
        ciphertext = encrypt_ordinals_state(main_plaintext_state, main_key)
        self.assertEqual(ciphertext, main_ciphertext_state)

    def test_state_decryption(self):
        decrypted = decrypt_ordinals_state(main_ciphertext_state, main_key)
        self.assertEqual(decrypted, main_plaintext_state)

    def test_encryption1(self):
        ciphertext_out = encrypt(plaintext1, key1)
        self.assertEqual(ciphertext_out, ciphertext1)

    def test_decryption1(self):
        plaintext_out = decrypt(ciphertext1, key1)
        self.assertEqual(plaintext_out, plaintext1)
