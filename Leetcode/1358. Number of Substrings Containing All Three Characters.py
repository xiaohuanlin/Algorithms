'''
Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

 

Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 
Example 3:

Input: s = "abc"
Output: 1
 

Constraints:

3 <= s.length <= 5 x 10^4
s only consists of a, b or c characters.
'''
import unittest
from typing import *

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = 0
        window = [0, 0, 0]
        res = 0
        for i in range(len(s)):
            window[ord(s[i]) - ord('a')] += 1
            while all(n > 0 for n in window):
                # move left
                window[ord(s[left]) - ord('a')] -= 1
                left += 1
                res += (len(s) - i)
        return res

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("abcabc",),10),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().numberOfSubstrings(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()