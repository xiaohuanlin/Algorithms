'''
You are given an integer array nums and two integers, k and m.

Return the maximum sum of k non-overlapping subarrays of nums, where each subarray has a length of at least m.

 

Example 1:

Input: nums = [1,2,-1,3,3,4], k = 2, m = 2

Output: 13

Explanation:

The optimal choice is:

Subarray nums[3..5] with sum 3 + 3 + 4 = 10 (length is 3 >= m).
Subarray nums[0..1] with sum 1 + 2 = 3 (length is 2 >= m).
The total sum is 10 + 3 = 13.

Example 2:

Input: nums = [-10,3,-1,-2], k = 4, m = 1

Output: -10

Explanation:

The optimal choice is choosing each element as a subarray. The output is (-10) + 3 + (-1) + (-2) = -10.

 

Constraints:

1 <= nums.length <= 2000
-104 <= nums[i] <= 104
1 <= k <= floor(nums.length / m)
1 <= m <= 3
'''
from typing import *

import unittest


class Solution:
    def maxSum(self, nums: List[int], k: int, m: int) -> int:
        pre_sum = [0 for _ in range(len(nums)+1)]
        for i in range(1, len(nums)+1):
            pre_sum[i] = pre_sum[i-1] + nums[i-1]

        dp = [[float('-inf') for _ in range(len(nums)+1)] for _ in range(k+1)]
        for j in range(len(nums)+1):
            dp[0][j] = 0

        for i in range(1, k+1):
            best = float('-inf')
            for j in range(1, len(nums)+1):
                dp[i][j] = dp[i][j-1] # use the previous result
                if j - m >= 0:
                    best = max(best, dp[i-1][j-m] - pre_sum[j-m])
                    dp[i][j] = max(dp[i][j], best + pre_sum[j])
        return dp[-1][-1]


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,2,-1,3,3,4], 2, 2), 13),
            (([-10,3,-1,-2], 4, 1), -10),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maxSum(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
