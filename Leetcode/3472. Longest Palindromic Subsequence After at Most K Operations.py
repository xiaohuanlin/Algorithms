'''
You are given a string s and an integer k.

In one operation, you can replace the character at any position with the next or previous letter in the alphabet (wrapping around so that 'a' is after 'z'). For example, replacing 'a' with the next letter results in 'b', and replacing 'a' with the previous letter results in 'z'. Similarly, replacing 'z' with the next letter results in 'a', and replacing 'z' with the previous letter results in 'y'.

Return the length of the longest palindromic subsequence of s that can be obtained after performing at most k operations.

 

Example 1:

Input: s = "abced", k = 2

Output: 3

Explanation:

Replace s[1] with the next letter, and s becomes "acced".
Replace s[4] with the previous letter, and s becomes "accec".
The subsequence "ccc" forms a palindrome of length 3, which is the maximum.

Example 2:

Input: s = "aaazzz", k = 4

Output: 6

Explanation:

Replace s[0] with the previous letter, and s becomes "zaazzz".
Replace s[4] with the next letter, and s becomes "zaazaz".
Replace s[3] with the next letter, and s becomes "zaaaaz".
The entire string forms a palindrome of length 6.

 

Constraints:

1 <= s.length <= 200
1 <= k <= 200
s consists of only lowercase English letters.
'''
from typing import *

import unittest


class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        def cost(x, y):
            if ord(x) > ord(y):
                x, y = y, x
            return min(ord(y) - ord(x), ord(x) + 26 - ord(y))

        dp = [[0 for _ in range(k+1)] for _ in range(len(s)+1)]
        for i in range(len(s))[::-1]:
            new_dp = [[0 for _ in range(k+1)] for _ in range(len(s)+1)]
            new_dp[i+1] = [1 for _ in range(k+1)]
            for j in range(i+2, len(s)+1):
                for z in range(k+1):
                    new_dp[j][z] = max(new_dp[j-1][z], dp[j][z])
                    c = cost(s[i], s[j-1])
                    if z - c >= 0:
                        new_dp[j][z] = max(new_dp[j][z], dp[j-1][z-c] + 2)
            dp = new_dp
        return dp[-1][-1]



class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("abced", 2), 3),
            (("aaazzz", 4), 6),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().longestPalindromicSubsequence(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
