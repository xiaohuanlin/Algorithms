'''
The factorial of a positive integer n is the product of all positive integers less than or equal to n.

For example, factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1.
We make a clumsy factorial using the integers in decreasing order by swapping out the multiply operations for a fixed rotation of operations with multiply '*', divide '/', add '+', and subtract '-' in this order.

For example, clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1.
However, these operations are still applied using the usual order of operations of arithmetic. We do all multiplication and division steps before any addition or subtraction steps, and multiplication and division steps are processed left to right.

Additionally, the division that we use is floor division such that 10 * 9 / 8 = 90 / 8 = 11.

Given an integer n, return the clumsy factorial of n.

 

Example 1:

Input: n = 4
Output: 7
Explanation: 7 = 4 * 3 / 2 + 1
Example 2:

Input: n = 10
Output: 12
Explanation: 12 = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1
 

Constraints:

1 <= n <= 104
'''
from typing import *
import unittest

class Solution:
    def clumsy(self, n: int) -> int:
        stack = [n]
        count = 0
        for i in range(1, n)[::-1]:
            if count % 4 == 0:
                item = stack.pop()
                stack.append(item * i)
            elif count % 4 == 1:
                item = stack.pop()
                stack.append(item // i)
            else:
                stack.append(i)
            count += 1
        
        res = stack[0]
        for i in range(1,len(stack)):
            if i % 2 == 1:
                res += stack[i]
            else:
                res -= stack[i]
        return res

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((10,),12),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().clumsy(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()