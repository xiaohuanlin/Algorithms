'''
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

 

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
'''
from typing import *

import unittest
from collections import defaultdict
    
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        maps = defaultdict(int)
        res = 0
        for n in nums:
            res += maps[n]
            maps[n] += 1
        return res
        
        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,2,3,1,1,3],),4),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().numIdenticalPairs(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
