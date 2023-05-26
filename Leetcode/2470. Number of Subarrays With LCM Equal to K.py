'''
Given an integer array nums and an integer k, return the number of subarrays of nums where the least common multiple of the subarray's elements is k.

A subarray is a contiguous non-empty sequence of elements within an array.

The least common multiple of an array is the smallest positive integer that is divisible by all the array elements.

 

Example 1:

Input: nums = [3,6,2,7,1], k = 6
Output: 4
Explanation: The subarrays of nums where 6 is the least common multiple of all the subarray's elements are:
- [3,6,2,7,1]
- [3,6,2,7,1]
- [3,6,2,7,1]
- [3,6,2,7,1]
Example 2:

Input: nums = [3], k = 2
Output: 0
Explanation: There are no subarrays of nums where 2 is the least common multiple of all the subarray's elements.
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i], k <= 1000
'''
import unittest

from typing import *

from math import gcd
class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            l = nums[i]
            if l == k:
                res += 1
            for j in range(i + 1, len(nums)):
                l = l * nums[j] // gcd(l, nums[j])
                if l == k:
                    res += 1
        return res

        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([3,6,2,7,1], 6), 4),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().subarrayLCM(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
