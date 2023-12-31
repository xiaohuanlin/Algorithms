'''
Given a string s consisting of only the characters 'a' and 'b', return true if every 'a' appears before every 'b' in the string. Otherwise, return false.

 

Example 1:

Input: s = "aaabbb"
Output: true
Explanation:
The 'a's are at indices 0, 1, and 2, while the 'b's are at indices 3, 4, and 5.
Hence, every 'a' appears before every 'b' and we return true.
Example 2:

Input: s = "abab"
Output: false
Explanation:
There is an 'a' at index 2 and a 'b' at index 1.
Hence, not every 'a' appears before every 'b' and we return false.
Example 3:

Input: s = "bbb"
Output: true
Explanation:
There are no 'a's, hence, every 'a' appears before every 'b' and we return true.
 

Constraints:

1 <= s.length <= 100
s[i] is either 'a' or 'b'.
'''
import unittest

from typing import *


class Solution:
    def checkString(self, s: str) -> bool:
        ai = s[::-1].find('a')
        if ai == -1:
            return True
        bi = s.find('b')
        if bi == -1:
            return True
        return len(s) - ai - 1 < bi


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("aaabbb",),True),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().checkString(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
