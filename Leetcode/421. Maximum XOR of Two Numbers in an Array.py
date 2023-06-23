'''
Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 <= i <= j < n.

 

Example 1:

Input: nums = [3,10,5,25,2,8]
Output: 28
Explanation: The maximum result is 5 XOR 25 = 28.
Example 2:

Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
Output: 127
 

Constraints:

1 <= nums.length <= 2 * 105
0 <= nums[i] <= 231 - 1
'''
from typing import *

import unittest
    
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        mask = 0
        target = 0
        for i in range(32):
            mask |= (1 << (31 - i))
            all_prefix = set(n & mask for n in nums)
            # hope we can find another 1
            next_target = target | (1 << (31 - i))
            for prefix in all_prefix:
                if prefix ^ next_target in all_prefix:
                    target = next_target
                    break
        return target
        
        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([14,70,53,83,49,91,36,80,92,51,66,70],),127),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().findMaximumXOR(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
