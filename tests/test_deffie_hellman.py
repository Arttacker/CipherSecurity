import unittest
from encryption.modern.asymmetric.deffie_hellman import get_shared_key


class TestDeffieHellman(unittest.TestCase):

    def test1(self):
        shared_key = get_shared_key(19, 2, 6, 13)
        self.assertTrue(shared_key[0] == 7 and shared_key[1] == 7)

    def test2(self):
        shared_key = get_shared_key(353, 2, 97, 233)
        self.assertTrue(shared_key[0] == 81 and shared_key[1] == 81)

    def test3(self):
        shared_key = get_shared_key(353, 3, 97, 233)
        self.assertTrue(shared_key[0] == 160 and shared_key[1] == 160)

    def test4(self):
        shared_key = get_shared_key(541, 10, 50, 100)
        self.assertTrue(shared_key[0] == 449 and shared_key[1] == 449)
