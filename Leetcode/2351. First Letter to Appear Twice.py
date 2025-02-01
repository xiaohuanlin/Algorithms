'''
Given a string s consisting of lowercase English letters, return the first letter to appear twice.

Note:

A letter a appears twice before another letter b if the second occurrence of a is before the second occurrence of b.
s will contain at least one letter that appears twice.
 

Example 1:

Input: s = "abccbaacz"
Output: "c"
Explanation:
The letter 'a' appears on the indexes 0, 5 and 6.
The letter 'b' appears on the indexes 1 and 4.
The letter 'c' appears on the indexes 2, 3 and 7.
The letter 'z' appears on the index 8.
The letter 'c' is the first letter to appear twice, because out of all the letters the index of its second occurrence is the smallest.
Example 2:

Input: s = "abcdd"
Output: "d"
Explanation:
The only letter that appears twice is 'd' so we return 'd'.
 

Constraints:

2 <= s.length <= 100
s consists of lowercase English letters.
s has at least one repeated letter.
'''
import unittest

from typing import *


class Solution:
    def repeatedCharacter(self, s: str) -> str:
        all_set = set()
        for w in s:
            if w not in all_set:
                all_set.add(w)
            else:
                return w
        return ""

    
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("abcdd",),"d"),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().repeatedCharacter(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
