'''
You are given an integer array nums consisting of 2 * n integers.

You need to divide nums into n pairs such that:

Each element belongs to exactly one pair.
The elements present in a pair are equal.
Return true if nums can be divided into n pairs, otherwise return false.

 

Example 1:

Input: nums = [3,2,3,2,2,2]
Output: true
Explanation: 
There are 6 elements in nums, so they should be divided into 6 / 2 = 3 pairs.
If nums is divided into the pairs (2, 2), (3, 3), and (2, 2), it will satisfy all the conditions.
Example 2:

Input: nums = [1,2,3,4]
Output: false
Explanation: 
There is no way to divide nums into 4 / 2 = 2 pairs such that the pairs satisfy every condition.
 

Constraints:

nums.length == 2 * n
1 <= n <= 500
1 <= nums[i] <= 500
'''
import unittest

from typing import *
from collections import Counter


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        c = Counter(nums)        
        for k, v in c.items():
            if v % 2 != 0:
                return False
        return True


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([3,2,3,2,2,2],),True),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().divideArray(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
