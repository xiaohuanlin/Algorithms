'''
Given a positive integer num represented as a string, return the integer num without trailing zeros as a string.

 

Example 1:

Input: num = "51230100"
Output: "512301"
Explanation: Integer "51230100" has 2 trailing zeros, we remove them and return integer "512301".
Example 2:

Input: num = "123"
Output: "123"
Explanation: Integer "123" has no trailing zeros, we return integer "123".
 

Constraints:

1 <= num.length <= 1000
num consists of only digits.
num doesn't have any leading zeros.
'''
from typing import *
import unittest


class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        for i in range(len(num))[::-1]:
            if num[i] != '0':
                return num[:i+1]
        return num


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("51230100",),"512301"),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().removeTrailingZeros(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()