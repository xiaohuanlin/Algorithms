'''
You are given an integer array nums and an integer k. Your task is to partition nums into one or more non-empty contiguous segments such that in each segment, the difference between its maximum and minimum elements is at most k.

Return the total number of ways to partition nums under this condition.

Since the answer may be too large, return it modulo 109 + 7.

 

Example 1:

Input: nums = [9,4,1,3,7], k = 4

Output: 6

Explanation:

There are 6 valid partitions where the difference between the maximum and minimum elements in each segment is at most k = 4:

[[9], [4], [1], [3], [7]]
[[9], [4], [1], [3, 7]]
[[9], [4], [1, 3], [7]]
[[9], [4, 1], [3], [7]]
[[9], [4, 1], [3, 7]]
[[9], [4, 1, 3], [7]]
Example 2:

Input: nums = [3,3,4], k = 0

Output: 2

Explanation:

There are 2 valid partitions that satisfy the given conditions:

[[3], [3], [4]]
[[3, 3], [4]]
 

Constraints:

2 <= nums.length <= 5 * 104
1 <= nums[i] <= 109
0 <= k <= 109
'''
import unittest
from collections import deque
from typing import *


class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        dp = [0 for _ in range(len(nums) + 1)]
        dp[0] = 1
        maxq = deque([])
        minq = deque([])
        left = 0
        presum = [0 for _ in range(len(nums) + 1)]
        presum[0] = 1
        mod = int(1e9+7)
        for i in range(len(nums)):
            while maxq and nums[maxq[-1]] <= nums[i]:
                maxq.pop()
            maxq.append(i)
            while minq and nums[minq[-1]] >= nums[i]:
                minq.pop()
            minq.append(i)

            while maxq and minq and nums[maxq[0]] - nums[minq[0]] > k:
                if maxq[0] == left:
                    maxq.popleft()
                if minq[0] == left:
                    minq.popleft()
                left += 1
            dp[i+1] = (presum[i] - presum[left - 1]) % mod
            presum[i+1] = (presum[i] + dp[i+1]) % mod
        return dp[-1]
        
        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([9,4,1,3,7], 4), 6),
            (([3,3,4], 0), 2),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().countPartitions(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
