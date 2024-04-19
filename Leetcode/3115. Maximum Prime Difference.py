'''
You are given an integer array nums.

Return an integer that is the maximum distance between the indices of two (not necessarily different) prime numbers in nums.



Example 1:

Input: nums = [4,2,9,5,3]

Output: 3

Explanation: nums[1], nums[3], and nums[4] are prime. So the answer is |4 - 1| = 3.

Example 2:

Input: nums = [4,8,2,8]

Output: 0

Explanation: nums[2] is prime. Because there is just one prime number, the answer is |2 - 2| = 0.



Constraints:

1 <= nums.length <= 3 * 105
1 <= nums[i] <= 100
The input is generated such that the number of prime numbers in the nums is at least one.
'''
import unittest

from typing import *

from math import sqrt

class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        def is_prime(n):
            if n == 1:
                return False
            for i in range(2, int(sqrt(n)) + 1):
                if n % i == 0:
                    return False
            return True

        first = -1
        last = -1
        for i, n in enumerate(nums):
            if is_prime(n):
                if first == -1:
                    first = i
                last = i
        return last - first


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([4,2,9,5,3],),3),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maximumPrimeDifference(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
