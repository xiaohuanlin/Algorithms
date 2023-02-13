'''
Given an integer num, return the number of digits in num that divide num.

An integer val divides nums if nums % val == 0.

 

Example 1:

Input: num = 7
Output: 1
Explanation: 7 divides itself, hence the answer is 1.
Example 2:

Input: num = 121
Output: 2
Explanation: 121 is divisible by 1, but not 2. Since 1 occurs twice as a digit, we return 2.
Example 3:

Input: num = 1248
Output: 4
Explanation: 1248 is divisible by all of its digits, hence the answer is 4.
 

Constraints:

1 <= num <= 109
num does not contain 0 as one of its digits.
'''

from typing import *
import unittest


class Solution:
    def countDigits(self, num: int) -> int:
        s = 0
        v = num
        while v:
            div = v % 10
            if num % div == 0:
                s += 1
            v //= 10
        return s
        

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((121,),2),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().countDigits(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()