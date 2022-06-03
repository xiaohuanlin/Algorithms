'''
Given an array of integers nums, find the maximum length of a subarray where the product of all its elements is positive.

A subarray of an array is a consecutive sequence of zero or more values taken out of that array.

Return the maximum length of a subarray with positive product.

 

Example 1:

Input: nums = [1,-2,-3,4]
Output: 4
Explanation: The array nums already has a positive product of 24.
Example 2:

Input: nums = [0,1,-2,-3,-4]
Output: 3
Explanation: The longest subarray with positive product is [1,-2,-3] which has a product of 6.
Notice that we cannot include 0 in the subarray since that'll make the product 0 which is not positive.
Example 3:

Input: nums = [-1,-2,-3,0,1]
Output: 2
Explanation: The longest subarray with positive product is [-1,-2] or [-2,-3].
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
'''
import unittest
from typing import *


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        first_negative_pos = -1
        last_negative_pos = -1
        negative_count = 0
        start = 0
        res = 0
        for i in range(len(nums) + 1):
            if i == len(nums) or nums[i] == 0:
                # divide
                if negative_count % 2 == 0:
                    res = max(res, i - start)
                else:
                    res = max(res, i - first_negative_pos - 1, last_negative_pos - start)
                first_negative_pos = -1
                last_negative_pos = -1
                start = i + 1
                negative_count = 0
            
            if i < len(nums) and nums[i] < 0:
                negative_count += 1
                if first_negative_pos == -1:
                    first_negative_pos = i
                last_negative_pos = i
        return res

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([0,1,-2,-3,-4],), 3),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().getMaxLen(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()