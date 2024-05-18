'''
A word is considered valid if:

It contains a minimum of 3 characters.
It contains only digits (0-9), and English letters (uppercase and lowercase).
It includes at least one vowel.
It includes at least one consonant.
You are given a string word.

Return true if word is valid, otherwise, return false.

Notes:

'a', 'e', 'i', 'o', 'u', and their uppercases are vowels.
A consonant is an English letter that is not a vowel.
 

Example 1:

Input: word = "234Adas"

Output: true

Explanation:

This word satisfies the conditions.

Example 2:

Input: word = "b3"

Output: false

Explanation:

The length of this word is fewer than 3, and does not have a vowel.

Example 3:

Input: word = "a3$e"

Output: false

Explanation:

This word contains a '$' character and does not have a consonant.

 

Constraints:

1 <= word.length <= 20
word consists of English uppercase and lowercase letters, digits, '@', '#', and '$'.
'''
from typing import *
import unittest

from string import ascii_letters, digits


class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        vowels = ['a', 'e', 'i', 'o', 'u']
        has_vowel = False
        has_consonant = False
        for w in word:
            if w not in ascii_letters and w not in digits:
                return False
            if w.lower() in vowels:
                has_vowel = True
            if w in ascii_letters and w.lower() not in vowels:
                has_consonant = True
        return has_vowel and has_consonant


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("234Adas",), True),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().isValid(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()