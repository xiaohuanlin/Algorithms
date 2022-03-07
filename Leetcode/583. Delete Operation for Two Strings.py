'''
Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.

 

Example 1:

Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Example 2:

Input: word1 = "leetcode", word2 = "etco"
Output: 4
 

Constraints:

1 <= word1.length, word2.length <= 500
word1 and word2 consist of only lowercase English letters.
'''
from typing import *
from pprint import pprint

import unittest


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        common = self.longestCommonSub(word1, word2)
        return len(word1) + len(word2) - 2 * common
        
    def longestCommonSub(self, word1, word2):
        row = len(word1)
        col = len(word2)
        dp = [[0 for _ in range(col + 1)] for _ in range(row + 1)]

        for i in range(1, row + 1):
            for j in range(1, col + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[row][col]



class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("sea", "eat"), 2),
            (("leetcode", "etco"), 4),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minDistance(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
