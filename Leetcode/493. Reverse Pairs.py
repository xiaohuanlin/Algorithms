'''
Given an integer array nums, return the number of reverse pairs in the array.

A reverse pair is a pair (i, j) where:

0 <= i < j < nums.length and
nums[i] > 2 * nums[j].
 

Example 1:

Input: nums = [1,3,2,3,1]
Output: 2
Explanation: The reverse pairs are:
(1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1
Example 2:

Input: nums = [2,4,3,5,1]
Output: 3
Explanation: The reverse pairs are:
(1, 4) --> nums[1] = 4, nums[4] = 1, 4 > 2 * 1
(2, 4) --> nums[2] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 5, nums[4] = 1, 5 > 2 * 1
 

Constraints:

1 <= nums.length <= 5 * 104
-231 <= nums[i] <= 231 - 1
'''
from typing import *
import unittest

from bisect import bisect_left, insort

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        a = []
        res = 0
        for n in nums[::-1]:
            index = bisect_left(a, n)
            res += index
            insort(a, n * 2)
        return res
                    

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,3,2,3,1],),2),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().reversePairs(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
