'''
You are given a string s consisting only of characters 'a' and 'b'​​​​.

You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

Return the minimum number of deletions needed to make s balanced.

 

Example 1:

Input: s = "aababbab"
Output: 2
Explanation: You can either:
Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").
Example 2:

Input: s = "bbaaaaabb"
Output: 2
Explanation: The only solution is to delete the first two characters.
 

Constraints:

1 <= s.length <= 105
s[i] is 'a' or 'b'​​.
'''

from typing import *

import unittest

class Solution:
    def minimumDeletions(self, s: str) -> int:
        b_count = 0
        res = 0
        for i in range(len(s)):
            if s[i] == 'b':
                b_count += 1
            else:
                res = min(res + 1, b_count)
        return res

        
class TestSolution(unittest.TestCase):
    def test_case(self):
        examples = (
            (("aababbab",),2),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minimumDeletions(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

