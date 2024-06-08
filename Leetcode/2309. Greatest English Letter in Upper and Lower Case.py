'''
Given a string of English letters s, return the greatest English letter which occurs as both a lowercase and uppercase letter in s. The returned letter should be in uppercase. If no such letter exists, return an empty string.

An English letter b is greater than another letter a if b appears after a in the English alphabet.

 

Example 1:

Input: s = "lEeTcOdE"
Output: "E"
Explanation:
The letter 'E' is the only letter to appear in both lower and upper case.
Example 2:

Input: s = "arRAzFif"
Output: "R"
Explanation:
The letter 'R' is the greatest letter to appear in both lower and upper case.
Note that 'A' and 'F' also appear in both lower and upper case, but 'R' is greater than 'F' or 'A'.
Example 3:

Input: s = "AbCdEfGhIjK"
Output: ""
Explanation:
There is no letter that appears in both lower and upper case.
 

Constraints:

1 <= s.length <= 1000
s consists of lowercase and uppercase English letters.
'''
from typing import *
import unittest

from collections import defaultdict

class Solution:
    def greatestLetter(self, s: str) -> str:
        maps = defaultdict(int)

        res = ""
        for w in s:
            upper_w = w.upper()
            maps[upper_w] |= (1 if w == upper_w else 2)
            if maps[upper_w] == 3:
                res = max(res, upper_w)
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("arRAzFif",),"R"),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().greatestLetter(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()