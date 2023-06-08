'''
You are given a positive integer n. Each digit of n has a sign according to the following rules:

The most significant digit is assigned a positive sign.
Each other digit has an opposite sign to its adjacent digits.
Return the sum of all digits with their corresponding sign.



Example 1:

Input: n = 521
Output: 4
Explanation: (+5) + (-2) + (+1) = 4.
Example 2:

Input: n = 111
Output: 1
Explanation: (+1) + (-1) + (+1) = 1.
Example 3:

Input: n = 886996
Output: 0
Explanation: (+8) + (-8) + (+6) + (-9) + (+9) + (-6) = 0.


Constraints:

1 <= n <= 109
'''
import unittest

from typing import *


class Solution:
    def alternateDigitSum(self, n: int) -> int:
        mul = 1
        arr = []
        res = 0
        while n:
            arr.append(n % 10)
            n //= 10

        for v in arr[::-1]:
            res += mul * v
            mul *= -1
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((886996,),0),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().alternateDigitSum(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
