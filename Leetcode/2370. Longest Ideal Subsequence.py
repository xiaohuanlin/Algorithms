'''
You are given a string s consisting of lowercase letters and an integer k. We call a string t ideal if the following conditions are satisfied:

t is a subsequence of the string s.
The absolute difference in the alphabet order of every two adjacent letters in t is less than or equal to k.
Return the length of the longest ideal string.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

Note that the alphabet order is not cyclic. For example, the absolute difference in the alphabet order of 'a' and 'z' is 25, not 1.

 

Example 1:

Input: s = "acfgbd", k = 2
Output: 4
Explanation: The longest ideal string is "acbd". The length of this string is 4, so 4 is returned.
Note that "acfgbd" is not ideal because 'c' and 'f' have a difference of 3 in alphabet order.
Example 2:

Input: s = "abcd", k = 3
Output: 4
Explanation: The longest ideal string is "abcd". The length of this string is 4, so 4 is returned.
 

Constraints:

1 <= s.length <= 105
0 <= k <= 25
s consists of lowercase English letters.
'''
import unittest
from typing import *


class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [1 for _ in range(len(s))]
        last = [-1 for _ in range(26)]

        for i in range(len(s)):
            for delta in range(-k, k+1):
                target = ord(s[i]) - ord('a') + delta
                if target < 0 or target >= 26:
                    continue
                j = last[target]
                if j == -1:
                    continue
                dp[i] = max(dp[i], dp[j] + 1)
            last[ord(s[i]) - ord('a')] = i
        return max(dp)
        

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("acfgbd", 2), 4),
            (("abcd", 3), 4),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().longestIdealString(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

