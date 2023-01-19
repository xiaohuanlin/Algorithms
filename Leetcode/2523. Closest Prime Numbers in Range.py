'''
Given two positive integers left and right, find the two integers num1 and num2 such that:

left <= nums1 < nums2 <= right .
nums1 and nums2 are both prime numbers.
nums2 - nums1 is the minimum amongst all other pairs satisfying the above conditions.
Return the positive integer array ans = [nums1, nums2]. If there are multiple pairs satisfying these conditions, return the one with the minimum nums1 value or [-1, -1] if such numbers do not exist.

A number greater than 1 is called prime if it is only divisible by 1 and itself.



Example 1:

Input: left = 10, right = 19
Output: [11,13]
Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
Since 11 is smaller than 17, we return the first pair.
Example 2:

Input: left = 4, right = 6
Output: [-1,-1]
Explanation: There exists only one prime number in the given range, so the conditions cannot be satisfied.


Constraints:

1 <= left <= right <= 106
'''
import unittest

from typing import *
from math import sqrt

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        bool_primes = [True for _ in range(right+1)]
        bool_primes[1] = False
        for i in range(2, int(sqrt(right)) + 1):
            if not bool_primes[i]:
                continue
            j = i * i
            while j < len(bool_primes):
                bool_primes[j] = False
                j += i

        primes = []
        for i in range(left, right + 1):
            if bool_primes[i]:
                primes.append(i)
        min_v = float('inf')
        res = [-1, -1]
        for i in range(len(primes) - 1):
            dis = primes[i + 1] - primes[i]
            if dis < min_v:
                min_v = dis
                res = [primes[i], primes[i + 1]]
        return res



class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((10, 19), [11, 13]),
            ((19, 31), [29, 31]),
            (((1, 100000), [2, 3])),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().closestPrimes(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
