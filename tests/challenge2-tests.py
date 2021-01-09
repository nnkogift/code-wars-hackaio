import unittest
from solutions.challenge2 import dig_pow


class TestChallenge1(unittest.TestCase):

    def test_dig_pow(self):
        self.assertEqual(dig_pow(89, 1), 1, "Should be 1")
        self.assertEqual(dig_pow(92, 1), -1, "Should be -1")
        self.assertEqual(dig_pow(46288, 3), 51, "Should be 51")


if __name__ == '__main__':
    unittest.main()
