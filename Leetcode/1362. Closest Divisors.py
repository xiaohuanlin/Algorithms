'''
Given an integer num, find the closest two integers in absolute difference whose product equals num + 1 or num + 2.

Return the two integers in any order.



Example 1:

Input: num = 8
Output: [3,3]
Explanation: For num + 1 = 9, the closest divisors are 3 & 3, for num + 2 = 10, the closest divisors are 2 & 5, hence 3 & 3 is chosen.
Example 2:

Input: num = 123
Output: [5,25]
Example 3:

Input: num = 999
Output: [40,25]


Constraints:

1 <= num <= 10^9
'''
import unittest

from typing import *
from math import sqrt

class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        def get_pair(num):
            for i in range(1, int(sqrt(num)) + 1):
                if num % i == 0:
                    yield i, num // i

        min_v = float('inf')
        res = [0, 0]
        for n in (num+1, num+2):
            for x, y in get_pair(n):
                if abs(x - y) < min_v:
                    min_v = abs(x - y)
                    res = [x, y]
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((999,),[25, 40]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().closestDivisors(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
