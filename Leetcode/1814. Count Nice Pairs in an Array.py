'''
You are given an array nums that consists of non-negative integers. Let us define rev(x) as the reverse of the non-negative integer x. For example, rev(123) = 321, and rev(120) = 21. A pair of indices (i, j) is nice if it satisfies all of the following conditions:

0 <= i < j < nums.length
nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
Return the number of nice pairs of indices. Since that number can be too large, return it modulo 109 + 7.

 

Example 1:

Input: nums = [42,11,1,97]
Output: 2
Explanation: The two pairs are:
 - (0,3) : 42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121.
 - (1,2) : 11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12.
Example 2:

Input: nums = [13,10,35,24,76]
Output: 4
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
'''
import unittest
from typing import *

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        maps = {}
        
        def rev(x):
            return int(str(x)[::-1])
        
        res = 0
        for i in range(len(nums)):
            target = nums[i] - rev(nums[i])
            if target in maps:
                res += maps[target] 
            maps[target] = maps.get(target, 0) + 1
        return res % int(1e9 + 7)

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([42,11,1,97],),2),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().countNicePairs(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()