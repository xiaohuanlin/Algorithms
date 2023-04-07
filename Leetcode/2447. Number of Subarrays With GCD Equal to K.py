'''
Given an integer array nums and an integer k, return the number of subarrays of nums where the greatest common divisor of the subarray's elements is k.

A subarray is a contiguous non-empty sequence of elements within an array.

The greatest common divisor of an array is the largest integer that evenly divides all the array elements.



Example 1:

Input: nums = [9,3,1,2,6,3], k = 3
Output: 4
Explanation: The subarrays of nums where 3 is the greatest common divisor of all the subarray's elements are:
- [9,3,1,2,6,3]
- [9,3,1,2,6,3]
- [9,3,1,2,6,3]
- [9,3,1,2,6,3]
Example 2:

Input: nums = [4], k = 7
Output: 0
Explanation: There are no subarrays of nums where 7 is the greatest common divisor of all the subarray's elements.


Constraints:

1 <= nums.length <= 1000
1 <= nums[i], k <= 109
'''
import unittest

from typing import *
from math import gcd

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            gcd_v = 0
            for j in range(i, len(nums)):
                gcd_v = gcd(gcd_v, nums[j])
                if gcd_v == k:
                    res += 1
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([5,],1),0),
            (([1],1),1),
            (([9,3,1,2,6,3], 3), 4),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().subarrayGCD(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
