"""Unit tests for palindrome tester."""


import unittest

from palindrome_checker import PalindromeChecker


class PalindromeTester(unittest.TestCase):
    def setUp(self):
        self.pc = PalindromeChecker()
        self.tests = {
            "radar": True,
            "toot": True,
            "madam": True,
            "level": True,
            "abcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcba": True,
            "1234567890987654321": True,
            "kljasfdlkjsdf": False,
            "klsjdf laskujfoiu": False,
            "poi3u589usfa": False,
            "levea": False,
            "levbel": False
        }

    def test_palindrome(self):
        for test, answer in self.tests.items():
            self.assertEqual(answer, self.pc.check(test))


if __name__ == "__main__":
    unittest.main()
