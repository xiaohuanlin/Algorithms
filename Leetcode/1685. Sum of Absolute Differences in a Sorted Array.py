'''
You are given an integer array nums sorted in non-decreasing order.

Build and return an integer array result with the same length as nums such that result[i] is equal to the summation of absolute differences between nums[i] and all the other elements in the array.

In other words, result[i] is equal to sum(|nums[i]-nums[j]|) where 0 <= j < nums.length and j != i (0-indexed).

 

Example 1:

Input: nums = [2,3,5]
Output: [4,3,5]
Explanation: Assuming the arrays are 0-indexed, then
result[0] = |2-2| + |2-3| + |2-5| = 0 + 1 + 3 = 4,
result[1] = |3-2| + |3-3| + |3-5| = 1 + 0 + 2 = 3,
result[2] = |5-2| + |5-3| + |5-5| = 3 + 2 + 0 = 5.
Example 2:

Input: nums = [1,4,6,8,10]
Output: [24,15,13,15,21]
 

Constraints:

2 <= nums.length <= 105
1 <= nums[i] <= nums[i + 1] <= 104
'''
import unittest

from typing import *

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        presum = [0 for _ in range(len(nums) + 1)]
        
        for i in range(len(nums)):
            presum[i+1] = presum[i] + nums[i]
        
        res = []
        for i in range(len(nums)):
            left = nums[i] * (i + 1) - presum[i+1]
            right = (presum[-1] - presum[i]) - nums[i] * (len(nums) - i)
            res.append(left + right)
        return res

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([2,3,5],),[4,3,5]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().getSumAbsoluteDifferences(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()