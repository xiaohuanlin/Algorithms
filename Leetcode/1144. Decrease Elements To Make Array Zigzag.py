'''
Given an array nums of integers, a move consists of choosing any element and decreasing it by 1.

An array A is a zigzag array if either:

Every even-indexed element is greater than adjacent elements, ie. A[0] > A[1] < A[2] > A[3] < A[4] > ...
OR, every odd-indexed element is greater than adjacent elements, ie. A[0] < A[1] > A[2] < A[3] > A[4] < ...
Return the minimum number of moves to transform the given array nums into a zigzag array.

 

Example 1:

Input: nums = [1,2,3]
Output: 2
Explanation: We can decrease 2 to 0 or 3 to 1.
Example 2:

Input: nums = [9,6,1,6,2]
Output: 4
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 1000
'''
import unittest

from typing import *


class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
            
        even = 0
        odd = 0

        for i in range(len(nums)):
            if i == 0:
                target = nums[i+1] - 1
            elif i == len(nums) - 1:
                target = nums[i-1] - 1
            else:
                target = min(nums[i-1], nums[i+1]) - 1
            if i % 2 == 0:
                even += max(0, nums[i] - target)
            else:
                odd += max(0, nums[i] - target)
        return min(even, odd)
            

    
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([9,6,1,6,2],),4),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().movesToMakeZigzag(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
