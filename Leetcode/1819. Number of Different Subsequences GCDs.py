'''
You are given an array nums that consists of positive integers.

The GCD of a sequence of numbers is defined as the greatest integer that divides all the numbers in the sequence evenly.

For example, the GCD of the sequence [4,6,16] is 2.
A subsequence of an array is a sequence that can be formed by removing some elements (possibly none) of the array.

For example, [2,5,10] is a subsequence of [1,2,1,2,4,1,5,10].
Return the number of different GCDs among all non-empty subsequences of nums.

 

Example 1:


Input: nums = [6,10,3]
Output: 5
Explanation: The figure shows all the non-empty subsequences and their GCDs.
The different GCDs are 6, 10, 3, 2, and 1.
Example 2:

Input: nums = [5,15,40,5,6]
Output: 7
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 2 * 105
'''
from math import gcd, sqrt
from typing import *
from collections import defaultdict

import unittest


class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0
        max_v = max(nums)
        for i in range(1, max_v + 1):
            all_gcd = 0
            # if i is gcd of some subarray, it mush be part of all multiples of i
            for j in range(i, max_v + 1, i):
                if j in nums_set:
                    all_gcd = gcd(all_gcd, j)
            if all_gcd == i:
                res += 1
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([6,10,3],), 5),
            (([5,15,40,5,6],), 7)
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().countDifferentSubsequenceGCDs(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
