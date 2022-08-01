'''
Given an integer array nums and two integers left and right, return the number of contiguous non-empty subarrays such that the value of the maximum array element in that subarray is in the range [left, right].

The test cases are generated so that the answer will fit in a 32-bit integer.

 

Example 1:

Input: nums = [2,1,4,3], left = 2, right = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].
Example 2:

Input: nums = [2,9,2,5,6], left = 2, right = 8
Output: 7
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
0 <= left <= right <= 109
'''

from typing import *

import unittest

from bisect import bisect_left
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        prev_max = -1
        dp = 0
        res = 0
        
        for i in range(len(nums)):
            if nums[i] < left:
                res += dp
            elif nums[i] > right:
                prev_max = i
                dp = 0
            else:
                dp = i - prev_max
                res += dp
        return res

        
class TestSolution(unittest.TestCase):
    def test_case(self):
        examples = (
            (([2,1,4,3], 2, 3), 3),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().numSubarrayBoundedMax(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

