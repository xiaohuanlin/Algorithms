'''
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
'''
from typing import *

import unittest


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        left = 0
        count = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                count += 1

            while count > k:
                if nums[left] == 0:
                    count -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
            


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,1,1,0,0,0,1,1,1,1,0], 2), 6),
            (([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3), 10),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().longestOnes(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
