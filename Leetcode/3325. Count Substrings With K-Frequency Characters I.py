'''
Given a string s and an integer k, return the total number of 
substrings
 of s where at least one character appears at least k times.

 

Example 1:

Input: s = "abacb", k = 2

Output: 4

Explanation:

The valid substrings are:

"aba" (character 'a' appears 2 times).
"abac" (character 'a' appears 2 times).
"abacb" (character 'a' appears 2 times).
"bacb" (character 'b' appears 2 times).
Example 2:

Input: s = "abcde", k = 1

Output: 15

Explanation:

All substrings are valid because every character appears at least once.

 

Constraints:

1 <= s.length <= 3000
1 <= k <= s.length
s consists only of lowercase English letters.
'''
import unittest

from typing import *
from collections import defaultdict


class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        windows = defaultdict(int)
        left = 0
        res = 0
        for right in range(len(s)):
            windows[s[right]] += 1
            while windows[s[right]] == k:
                windows[s[left]] -= 1
                res += len(s) - right
                left += 1
        return res
    
            
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("abcde", 1), 15),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().numberOfSubstrings(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
