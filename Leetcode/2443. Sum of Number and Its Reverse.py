'''
Given a non-negative integer num, return true if num can be expressed as the sum of any non-negative integer and its reverse, or false otherwise.



Example 1:

Input: num = 443
Output: true
Explanation: 172 + 271 = 443 so we return true.
Example 2:

Input: num = 63
Output: false
Explanation: 63 cannot be expressed as the sum of a non-negative integer and its reverse so we return false.
Example 3:

Input: num = 181
Output: true
Explanation: 140 + 041 = 181 so we return true. Note that when a number is reversed, there may be leading zeros.


Constraints:

0 <= num <= 105
'''
import unittest

from typing import *

class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        if num == 0:
            return True
        start = int(5 * 10 ** (len(str(num)) - 2))
        for i in range(start, num):
            if i + int(str(i)[::-1]) == num:
                return True
        return False


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((5,), False),
            ((0,), True),
            ((181,), True),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().sumOfNumberAndReverse(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
