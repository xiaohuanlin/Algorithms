'''
Given an integer n, add a dot (".") as the thousands separator and return it in string format.



Example 1:

Input: n = 987
Output: "987"
Example 2:

Input: n = 1234
Output: "1.234"


Constraints:

0 <= n <= 231 - 1
'''
from typing import *

import unittest

class Solution:
    def thousandSeparator(self, n: int) -> str:
        k = 0
        res = []
        while n:
            res.append(str(n % 10))
            k += 1
            if k % 3 == 0:
                res.append('.')
            n //= 10

        if k % 3 == 0 and res:
            res.pop()
        return ''.join(res[::-1]) if res else '0'


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((987,), "987"),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().thousandSeparator(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
