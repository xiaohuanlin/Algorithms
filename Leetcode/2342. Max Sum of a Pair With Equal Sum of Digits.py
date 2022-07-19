'''
You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].

Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions.

 

Example 1:

Input: nums = [18,43,36,13,7]
Output: 54
Explanation: The pairs (i, j) that satisfy the conditions are:
- (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
- (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
So the maximum sum that we can obtain is 54.
Example 2:

Input: nums = [10,12,19,14]
Output: -1
Explanation: There are no two numbers that satisfy the conditions, so we return -1.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
'''

from typing import *

import unittest
from  collections import deque


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def get_sum(x):
            t = 0
            for n in str(x):
                t += int(n)
            return t
        
        maps = {}
        max_v = -1
        for i in range(len(nums)):
            k = get_sum(nums[i])
            maps.setdefault(k, []).append(nums[i])
            if len(maps[k]) >= 2:
                maps[k].sort()
                if len(maps[k]) > 2:
                    maps[k].pop(0)
                max_v = max(sum(maps[k]), max_v)
        return max_v
        
class TestSolution(unittest.TestCase):
    def test_case(self):
        examples = (
            (([18,43,36,13,7],),54),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maximumSum(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

