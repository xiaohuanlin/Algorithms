'''
Given an integer array nums, partition it into two (contiguous) subarrays left and right so that:

Every element in left is less than or equal to every element in right.
left and right are non-empty.
left has the smallest possible size.
Return the length of left after such a partitioning.

Test cases are generated such that partitioning exists.

 

Example 1:

Input: nums = [5,0,3,8,6]
Output: 3
Explanation: left = [5,0,3], right = [8,6]
Example 2:

Input: nums = [1,1,1,0,6,12]
Output: 4
Explanation: left = [1,1,1,0], right = [6,12]
 

Constraints:

2 <= nums.length <= 105
0 <= nums[i] <= 106
There is at least one valid answer for the given input.
'''

from typing import *

import unittest


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        global_max = nums[0]
        left_max = nums[0]
        res = 0
        
        for i in range(len(nums)):
            global_max = max(global_max, nums[i])
            if nums[i] < left_max:
                # move pos to current pos
                left_max = global_max
                res = i
        return res + 1

        
class TestSolution(unittest.TestCase):
    def test_case(self):
        examples = (
            (([5,0,3,8,6],),3),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().partitionDisjoint(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

