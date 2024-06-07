'''
An integer divisible by the sum of its digits is said to be a Harshad number. You are given an integer x. Return the sum of the digits of x if x is a Harshad number, otherwise, return -1.

 

Example 1:

Input: x = 18

Output: 9

Explanation:

The sum of digits of x is 9. 18 is divisible by 9. So 18 is a Harshad number and the answer is 9.

Example 2:

Input: x = 23

Output: -1

Explanation:

The sum of digits of x is 5. 23 is not divisible by 5. So 23 is not a Harshad number and the answer is -1.

 

Constraints:

1 <= x <= 100
'''
from typing import *
import unittest


class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        res = sum(int(d) for d in str(x))
        return res if x % res == 0 else -1


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((18,),9),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().sumOfTheDigitsOfHarshadNumber(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()