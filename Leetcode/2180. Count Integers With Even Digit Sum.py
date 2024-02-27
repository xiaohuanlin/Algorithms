'''
Given a positive integer num, return the number of positive integers less than or equal to num whose digit sums are even.

The digit sum of a positive integer is the sum of all its digits.

 

Example 1:

Input: num = 4
Output: 2
Explanation:
The only integers less than or equal to 4 whose digit sums are even are 2 and 4.    
Example 2:

Input: num = 30
Output: 14
Explanation:
The 14 integers less than or equal to 30 whose digit sums are even are
2, 4, 6, 8, 11, 13, 15, 17, 19, 20, 22, 24, 26, and 28.
 

Constraints:

1 <= num <= 1000
'''
import unittest

from typing import *


class Solution:
    def countEven(self, num: int) -> int:
        # 0-100:4+5+5+5+5+5+5+5+5+5=49
        # 101-200:5+5+5+5+5+5+5+5+5+5=50
        # abc
        if num == 1000:
            return 499
        a = (num // 100) % 10
        b = (num // 10) % 10
        c = num % 10
        return a * 50 + b * 5 + ((c // 2 + 1) if (a + b) % 2 == 0 else (c + 1) // 2) - 1
                

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((30,),14),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().countEven(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
