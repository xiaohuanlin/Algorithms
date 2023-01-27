'''
Given an array of positive integers nums, return the number of distinct prime factors in the product of the elements of nums.

Note that:

A number greater than 1 is called prime if it is divisible by only 1 and itself.
An integer val1 is a factor of another integer val2 if val2 / val1 is an integer.
 

Example 1:

Input: nums = [2,4,3,7,10,6]
Output: 4
Explanation:
The product of all the elements in nums is: 2 * 4 * 3 * 7 * 10 * 6 = 10080 = 25 * 32 * 5 * 7.
There are 4 distinct prime factors so we return 4.
Example 2:

Input: nums = [2,4,8,16]
Output: 1
Explanation:
The product of all the elements in nums is: 2 * 4 * 8 * 16 = 1024 = 210.
There is 1 distinct prime factor so we return 1.
 

Constraints:

1 <= nums.length <= 104
2 <= nums[i] <= 1000
'''

from typing import *
import unittest

from math import sqrt
class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        all_set = set()

        def get_primes(num):
            for i in range(2, int(sqrt(num))+1):
                if num % i == 0:
                    return {i} | get_primes(num // i)
            return {num}

        for num in nums:
            all_set |= get_primes(num)
        return len(all_set)


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([2,4,3,7,10,6],),4),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().distinctPrimeFactors(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()