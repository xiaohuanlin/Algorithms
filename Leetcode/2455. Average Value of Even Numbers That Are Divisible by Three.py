'''
Given an integer array nums of positive integers, return the average value of all even integers that are divisible by 3.

Note that the average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.

 

Example 1:

Input: nums = [1,3,6,10,12,15]
Output: 9
Explanation: 6 and 12 are even numbers that are divisible by 3. (6 + 12) / 2 = 9.
Example 2:

Input: nums = [1,2,4,7,10]
Output: 0
Explanation: There is no single number that satisfies the requirement, so return 0.
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 1000
'''
import unittest

from typing import *


class Solution:
    def averageValue(self, nums: List[int]) -> int:
        total = 0
        count = 0
        for n in nums:
            if n % 6 == 0:
                total += n
                count += 1
        return total // count if count != 0 else 0


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,3,6,10,12,15],),9),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().averageValue(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
