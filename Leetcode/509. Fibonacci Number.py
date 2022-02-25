'''
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

 

Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 

Constraints:

0 <= n <= 30
'''
from typing import *

import unittest


class Solution:
    def fib(self, n: int) -> int:
        first = 0
        second = 1
        count = 0
        while count < n:
            first, second = second, first + second
            count += 1
        return first


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((3,),2),
            ((4,),3),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().fib(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
