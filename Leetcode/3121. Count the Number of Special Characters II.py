'''
You are given a string word. A letter c is called special if it appears both in lowercase and uppercase in word, and every lowercase occurrence of c appears before the first uppercase occurrence of c.

Return the number of special letters in word.



Example 1:

Input: word = "aaAbcBC"

Output: 3

Explanation:

The special characters are 'a', 'b', and 'c'.

Example 2:

Input: word = "abc"

Output: 0

Explanation:

There are no special characters in word.

Example 3:

Input: word = "AbBCab"

Output: 0

Explanation:

There are no special characters in word.



Constraints:

1 <= word.length <= 2 * 105
word consists of only lowercase and uppercase English letters.
'''
import unittest

from typing import *


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        arr = [0 for i in range(26)]
        bad = set()

        for w in word:
            index = ord(w.lower()) - ord('a')
            value = 1 if w.lower() == w else 2
            if arr[index] == 1 and value >= 1:
                arr[index] |= value
            elif arr[index] == 0 and value == 1:
                arr[index] |= value
            elif arr[index] == 3 and value == 2:
                arr[index] |= value
            else:
                bad.add(w.lower())

        return sum(bool(v == 3 and chr(ord('a') + i) not in bad) for i,v in enumerate(arr))


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("AbBCab",),0),
            (("aaAbcBC",),3),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().numberOfSpecialChars(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
