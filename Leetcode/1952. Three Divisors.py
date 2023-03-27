'''
Given an integer n, return true if n has exactly three positive divisors. Otherwise, return false.

An integer m is a divisor of n if there exists an integer k such that n = k * m.

 

Example 1:

Input: n = 2
Output: false
Explantion: 2 has only two divisors: 1 and 2.
Example 2:

Input: n = 4
Output: true
Explantion: 4 has three divisors: 1, 2, and 4.
 

Constraints:

1 <= n <= 104
'''

from typing import *

import unittest

from math import sqrt
class Solution:
    def isThree(self, n: int) -> bool:
        if n == 1:
            return False
        def is_prime(num):
            for i in range(2, int(sqrt(num)) + 1):
                if num % i == 0:
                    return False
            return True

        sqrt_n = int(sqrt(n))
        return sqrt_n * sqrt_n == n and is_prime(sqrt_n)

        
class TestSolution(unittest.TestCase):
    def test_case(self):
        examples = (
            ((4,),True),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().isThree(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

