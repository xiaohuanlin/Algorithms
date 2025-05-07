'''
For an integer array nums, an inverse pair is a pair of integers [i, j] where 0 <= i < j < nums.length and nums[i] > nums[j].

Given two integers n and k, return the number of different arrays consisting of numbers from 1 to n such that there are exactly k inverse pairs. Since the answer can be huge, return it modulo 109 + 7.

 

Example 1:

Input: n = 3, k = 0
Output: 1
Explanation: Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pairs.
Example 2:

Input: n = 3, k = 1
Output: 2
Explanation: The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.
 

Constraints:

1 <= n <= 1000
0 <= k <= 1000
'''
import unittest

from typing import *


class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
        dp[1][0] = 1

        for i in range(2, n+1):
            for j in range(k + 1):
                #dp[i][j-1] = dp[i-1][j-1] + dp[i-1][j-2] + ... + dp[i-1][j-1-(i-1)]
                #dp[i][j] = dp[i-1][j] + dp[i-1][j-1] + ... + dp[i-1][j-(i-1)]
                dp[i][j] = ((dp[i][j-1] if j > 0 else 0) + dp[i-1][j] - (dp[i-1][j-1-(i-1)] if j - i >= 0 else 0)) % int(1e9 + 7)

        return dp[n][k]


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((3, 0), 1),
            ((3, 1), 2),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().kInversePairs(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

