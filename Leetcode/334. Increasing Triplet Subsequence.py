'''
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
 

Constraints:

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1
'''
from typing import *

import unittest

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        bigger = [0 for _ in range(len(nums))]
        next_bigger = nums[-1]
        bigger[-1] = next_bigger
        for i in range(len(nums)-1)[::-1]:
            if nums[i] > next_bigger:
                next_bigger = nums[i]
            bigger[i] = next_bigger

        prev_smaller = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < prev_smaller:
                prev_smaller = nums[i]
            if nums[i] > prev_smaller and bigger[i] > nums[i]:
                return True
        return False
        

class TestSolution(unittest.TestCase):
    def test_case(self):
        examples = (
            (([2,1,5,0,4,6],),True),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().increasingTriplet(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()