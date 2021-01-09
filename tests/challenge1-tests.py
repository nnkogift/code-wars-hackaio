import unittest

from solutions.challenge1 import duplicate_count


class TestChallenge1(unittest.TestCase):

    def test_duplicate_count(self):
        self.assertEqual(duplicate_count(""), 0, "Should be 0")
        self.assertEqual(duplicate_count("abcde"), 0, "Should be 0")
        self.assertEqual(duplicate_count("abcdeaa"), 1, "Should be 1")
        self.assertEqual(duplicate_count("abcdeaB"), 2, "Should be 2")
        self.assertEqual(duplicate_count("Indivisibilities"), 2, "Should be 2")


if __name__ == '__main__':
    unittest.main()
