'''
You are given an array nums of positive integers and a positive integer k.

A subset of nums is beautiful if it does not contain two integers with an absolute difference equal to k.

Return the number of non-empty beautiful subsets of the array nums.

A subset of nums is an array that can be obtained by deleting some (possibly none) elements from nums. Two subsets are different if and only if the chosen indices to delete are different.

 

Example 1:

Input: nums = [2,4,6], k = 2
Output: 4
Explanation: The beautiful subsets of the array nums are: [2], [4], [6], [2, 6].
It can be proved that there are only 4 beautiful subsets in the array [2,4,6].
Example 2:

Input: nums = [1], k = 1
Output: 1
Explanation: The beautiful subset of the array nums is [1].
It can be proved that there is only 1 beautiful subset in the array [1].
 

Constraints:

1 <= nums.length <= 20
1 <= nums[i], k <= 1000
'''
from typing import *

import unittest
    
class Solution:
    res = -1

    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        def backtrace(choice, i):
            if i >= len(nums):
                self.res += 1
                return

            backtrace(choice, i+1)

            if not (nums[i] + k in choice or nums[i] - k in choice):
                choice.append(nums[i])
                backtrace(choice, i+1)
                choice.pop()
        
        backtrace([], 0)
        return self.res
        
        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([2,4,6],2),4),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().beautifulSubsets(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
