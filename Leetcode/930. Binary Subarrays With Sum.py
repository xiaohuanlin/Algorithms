'''
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.

 

Example 1:

Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
Example 2:

Input: nums = [0,0,0,0,0], goal = 0
Output: 15
 

Constraints:

1 <= nums.length <= 3 * 104
nums[i] is either 0 or 1.
0 <= goal <= nums.length
'''
import unittest

from typing import *

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        maps = {0: 1}
        count = 0
        res = 0
        for i in range(len(nums)):
            count += nums[i]
            if count >= goal:
                res += maps.get(count - goal, 0)
            maps[count] = maps.setdefault(count, 0) + 1

        return res
        
        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,0,1,0,1], 2), 4),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().numSubarraysWithSum(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
