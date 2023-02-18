'''
Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.

A pair (i, j) is fair if:

0 <= i < j < n, and
lower <= nums[i] + nums[j] <= upper
 

Example 1:

Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
Output: 6
Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).
Example 2:

Input: nums = [1,7,9,2,5], lower = 11, upper = 11
Output: 1
Explanation: There is a single fair pair: (2,3).
 

Constraints:

1 <= nums.length <= 105
nums.length == n
-109 <= nums[i] <= 109
-109 <= lower <= upper <= 109
'''
from typing import *

import unittest


from bisect import bisect_left, bisect_right
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        res = 0
        for i, n in enumerate(nums):
            left = bisect_left(nums, lower - n)
            right = bisect_right(nums, upper - n)
            res += (right - left)
            if i >= left and i < right:
                res -= 1
        return res // 2
        
        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([0,1,7,4,4,5], 3, 6), 6),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().countFairPairs(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
