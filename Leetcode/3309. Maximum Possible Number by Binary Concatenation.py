'''
You are given an array of integers nums of size 3.

Return the maximum possible number whose binary representation can be formed by concatenating the binary representation of all elements in nums in some order.

Note that the binary representation of any number does not contain leading zeros.



Example 1:

Input: nums = [1,2,3]

Output: 30

Explanation:

Concatenate the numbers in the order [3, 1, 2] to get the result "11110", which is the binary representation of 30.

Example 2:

Input: nums = [2,8,16]

Output: 1296

Explanation:

Concatenate the numbers in the order [2, 8, 16] to get the result "10100010000", which is the binary representation of 1296.



Constraints:

nums.length == 3
1 <= nums[i] <= 127
'''
import unittest

from typing import *
from itertools import permutations


class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        res = 0
        for x, y, z in permutations(nums, 3):
            res = max(res, int(bin(x)[2:] + bin(y)[2:] + bin(z)[2:], 2))
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,2,3],), 30),
            (([2,8,16],), 1296),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maxGoodNumber(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()