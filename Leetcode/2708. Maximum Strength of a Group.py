'''
You are given a 0-indexed integer array nums representing the score of students in an exam. The teacher would like to form one non-empty group of students with maximal strength, where the strength of a group of students of indices i0, i1, i2, ... , ik is defined as nums[i0] * nums[i1] * nums[i2] * ... * nums[ik​].

Return the maximum strength of a group the teacher can create.

 

Example 1:

Input: nums = [3,-1,-5,2,5,-9]
Output: 1350
Explanation: One way to form a group of maximal strength is to group the students at indices [0,2,3,4,5]. Their strength is 3 * (-5) * 2 * 5 * (-9) = 1350, which we can show is optimal.
Example 2:

Input: nums = [-4,-5,-4]
Output: 20
Explanation: Group the students at indices [0, 1] . Then, we’ll have a resulting strength of 20. We cannot achieve greater strength.
 

Constraints:

1 <= nums.length <= 13
-9 <= nums[i] <= 9
'''
import unittest

from typing import *


class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        res = 1
        max_minus = float('-inf')
        valid_count = 0
        minus_count = 0
        for n in nums:
            if n != 0:
                res *= n
                valid_count += 1
            if n < 0:
                minus_count += 1
                max_minus = max(max_minus, n)
        if valid_count == minus_count:
            if valid_count != len(nums):
                if valid_count <= 1:
                    return 0
            else:
                if valid_count == 1:
                    return max_minus
        return res if minus_count % 2 == 0 else res // max_minus
        

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ([3, -1, -5, 2, 5, -9], 1350),
            ([-4, -5, -4], 20),
            ([0, 0, 0], 0),
            ([1, 2, 3], 6),
            ([-1, -2, -3], 6),
            ([1, -2, -3], 3),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maxStrength(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

