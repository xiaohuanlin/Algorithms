'''
You are given an integer array nums and a positive integer k. Return the sum of the maximum and minimum elements of all subsequences of nums with at most k elements.

Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: nums = [1,2,3], k = 2

Output: 24

Explanation:

The subsequences of nums with at most 2 elements are:

Subsequence	Minimum	Maximum	Sum
[1]	1	1	2
[2]	2	2	4
[3]	3	3	6
[1, 2]	1	2	3
[1, 3]	1	3	4
[2, 3]	2	3	5
Final Total	 	 	24
The output would be 24.

Example 2:

Input: nums = [5,0,6], k = 1

Output: 22

Explanation:

For subsequences with exactly 1 element, the minimum and maximum values are the element itself. Therefore, the total is 5 + 5 + 0 + 0 + 6 + 6 = 22.

Example 3:

Input: nums = [1,1,1], k = 2

Output: 12

Explanation:

The subsequences [1, 1] and [1] each appear 3 times. For all of them, the minimum and maximum are both 1. Thus, the total is 12.

 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
1 <= k <= min(70, nums.length)
'''
import unittest

from typing import *


class Solution:
    def minMaxSums(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0

        dp = [[1 for _ in range(k+1)] for _ in range(len(nums) + 1)]
        dp[0] = [1] * (k + 1)
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

        for i in range(len(nums)):
            res += (dp[i][k-1] * nums[i] % int(1e9 + 7))
            res += (dp[len(nums) - i - 1][k-1] * nums[i] % int(1e9 + 7))
            res %= int(1e9 + 7)
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1, 2, 3], 2), 24),
            (([5, 0, 6], 1), 22),
            (([1, 1, 1], 2), 12),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minMaxSums(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

