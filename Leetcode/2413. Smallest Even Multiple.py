'''
Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n.
 

Example 1:

Input: n = 5
Output: 10
Explanation: The smallest multiple of both 5 and 2 is 10.
Example 2:

Input: n = 6
Output: 6
Explanation: The smallest multiple of both 6 and 2 is 6. Note that a number is a multiple of itself.
 

Constraints:

1 <= n <= 150
'''
from typing import *
import unittest

from math import gcd
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        g = gcd(n, 2)
        return 2 * n // g
                    

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((6,),6),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().smallestEvenMultiple(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
