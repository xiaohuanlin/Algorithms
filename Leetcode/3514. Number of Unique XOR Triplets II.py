'''
You are given an integer array nums.

A XOR triplet is defined as the XOR of three elements nums[i] XOR nums[j] XOR nums[k] where i <= j <= k.

Return the number of unique XOR triplet values from all possible triplets (i, j, k).



Example 1:

Input: nums = [1,3]

Output: 2

Explanation:

The possible XOR triplet values are:

(0, 0, 0) → 1 XOR 1 XOR 1 = 1
(0, 0, 1) → 1 XOR 1 XOR 3 = 3
(0, 1, 1) → 1 XOR 3 XOR 3 = 1
(1, 1, 1) → 3 XOR 3 XOR 3 = 3
The unique XOR values are {1, 3}. Thus, the output is 2.

Example 2:

Input: nums = [6,7,8,9]

Output: 4

Explanation:

The possible XOR triplet values are {6, 7, 8, 9}. Thus, the output is 4.



Constraints:

1 <= nums.length <= 1500
1 <= nums[i] <= 1500
'''
import unittest

from typing import *


class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        maxv = 0
        single = set()
        double = set()
        for i in range(len(nums)):
            single.add(nums[i])
            maxv |= nums[i]
            for j in range(i+1, len(nums)):
                double.add(nums[i] ^ nums[j])

        res = 0
        for n in range(maxv+1):
            for d in double:
                if d ^ n in single:
                    res += 1
                    break
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([6,7,8,9],),4),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().uniqueXorTriplets(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

