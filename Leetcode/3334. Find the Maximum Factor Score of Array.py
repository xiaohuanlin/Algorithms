'''
You are given an integer array nums.

The factor score of an array is defined as the product of the LCM and GCD of all elements of that array.

Return the maximum factor score of nums after removing at most one element from it.

Note that both the LCM and GCD of a single number are the number itself, and the factor score of an empty array is 0.

 

Example 1:

Input: nums = [2,4,8,16]

Output: 64

Explanation:

On removing 2, the GCD of the rest of the elements is 4 while the LCM is 16, which gives a maximum factor score of 4 * 16 = 64.

Example 2:

Input: nums = [1,2,3,4,5]

Output: 60

Explanation:

The maximum factor score of 60 can be obtained without removing any elements.

Example 3:

Input: nums = [3]

Output: 9

 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 30
'''
import unittest

from typing import *

from math import gcd, lcm

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        presum = [[nums[0], nums[0]] for _ in range(len(nums))]
        sufsum = [[nums[-1], nums[-1]] for _ in range(len(nums))]

        for i in range(1, len(nums)):
            presum[i][0] = gcd(presum[i-1][0], nums[i])
            presum[i][1] = lcm(presum[i-1][1], nums[i])
        for i in range(len(nums) - 1)[::-1]:
            sufsum[i][0] = gcd(sufsum[i+1][0], nums[i])
            sufsum[i][1] = lcm(sufsum[i+1][1], nums[i])

        res = presum[-1][0] * presum[-1][1]
        if len(nums) > 1:
            res = max(res, presum[-2][0] * presum[-2][1], sufsum[1][0] * sufsum[1][1])
        for i in range(1, len(nums) - 1):
            res = max(res, gcd(presum[i-1][0], sufsum[i+1][0]) * lcm(presum[i-1][1], sufsum[i+1][1]))
        return res
            

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([2,4,8,16],), 64),
            (([1,2,3,4,5],), 60),
            (([3],), 9),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maxScore(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
