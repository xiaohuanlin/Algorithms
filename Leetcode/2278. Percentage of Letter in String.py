'''
Given a string s and a character letter, return the percentage of characters in s that equal letter rounded down to the nearest whole percent.



Example 1:

Input: s = "foobar", letter = "o"
Output: 33
Explanation:
The percentage of characters in s that equal the letter 'o' is 2 / 6 * 100% = 33% when rounded down, so we return 33.
Example 2:

Input: s = "jjjj", letter = "k"
Output: 0
Explanation:
The percentage of characters in s that equal the letter 'k' is 0%, so we return 0.


Constraints:

1 <= s.length <= 100
s consists of lowercase English letters.
letter is a lowercase English letter.
'''
import unittest

from typing import *


class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return s.count(letter) * 100 // len(s)


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("foobar", "o"), 33),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().percentageLetter(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
