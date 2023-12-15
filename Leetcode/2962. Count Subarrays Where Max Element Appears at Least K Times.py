'''
You are given an integer array nums and a positive integer k.

Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.

A subarray is a contiguous sequence of elements within an array.

 

Example 1:

Input: nums = [1,3,2,3,3], k = 2
Output: 6
Explanation: The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].
Example 2:

Input: nums = [1,4,2,1], k = 3
Output: 0
Explanation: No subarray contains the element 4 at least 3 times.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 106
1 <= k <= 105
'''
from typing import *

import unittest

from collections import defaultdict


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        windows = 0
        res = 0
        target = max(nums)
        for right in range(len(nums)):
            windows += nums[right] == target
            while left <= right and windows >= k:
                res += len(nums) - right
                windows -= nums[left] == target
                left += 1
        return res

        
        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([61,23,38,23,56,40,82,56,82,82,82,70,8,69,8,7,19,14,58,42,82,10,82,78,15,82],2),224),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().countSubarrays(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
