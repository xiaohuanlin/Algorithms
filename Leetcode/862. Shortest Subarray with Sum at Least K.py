'''
Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1], k = 1
Output: 1
Example 2:

Input: nums = [1,2], k = 4
Output: -1
Example 3:

Input: nums = [2,-1,2], k = 3
Output: 3
 

Constraints:

1 <= nums.length <= 105
-105 <= nums[i] <= 105
1 <= k <= 109
'''

from typing import *

import unittest

from collections import deque
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # monotonic queue
        presum = [0]
        for i in range(len(nums)):
            presum.append(presum[-1] + nums[i])
            
        min_q = deque()
        res = float('inf')
        for i in range(len(presum)):
            # adjust left point
            while min_q and presum[i] - presum[min_q[0]] >= k:
                res = min(res, i - min_q.popleft())
                
            # maintain queue
            while min_q and presum[min_q[-1]] >= presum[i]:
                min_q.pop()
            min_q.append(i)

        return res if res != float('inf') else -1
        
class TestSolution(unittest.TestCase):
    def test_case(self):
        examples = (
            (([2,-1,2],3),3),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().shortestSubarray(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

