'''
Given an integer array nums and an integer k, return the maximum sum of a non-empty subsequence of that array such that for every two consecutive integers in the subsequence, nums[i] and nums[j], where i < j, the condition j - i <= k is satisfied.

A subsequence of an array is obtained by deleting some number of elements (can be zero) from the array, leaving the remaining elements in their original order.

 

Example 1:

Input: nums = [10,2,-10,5,20], k = 2
Output: 37
Explanation: The subsequence is [10, 2, 5, 20].
Example 2:

Input: nums = [-1,-2,-3], k = 1
Output: -1
Explanation: The subsequence must be non-empty, so we choose the largest number.
Example 3:

Input: nums = [10,-2,-10,-5,20], k = 2
Output: 23
Explanation: The subsequence is [10, -2, -5, 20].
 

Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
'''
from typing import *
import unittest


from heapq import heappush, heappop

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dp = [n for n in nums]
        h = []
        v = 0
        index = 0

        for i in range(len(nums)):
            while h and h[0][1] < i - k:
                heappop(h)

            if h:
                dp[i] = max(dp[i], -h[0][0] + nums[i])
            heappush(h, (-dp[i], i))
                
        return max(dp)


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([10,2,-10,5,20], 2), 37),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().constrainedSubsetSum(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()