'''
You are given a string num consisting of digits only.

Return the largest palindromic integer (in the form of a string) that can be formed using digits taken from num. It should not contain leading zeroes.

Notes:

You do not need to use all the digits of num, but you must use at least one digit.
The digits can be reordered.
 

Example 1:

Input: num = "444947137"
Output: "7449447"
Explanation: 
Use the digits "4449477" from "444947137" to form the palindromic integer "7449447".
It can be shown that "7449447" is the largest palindromic integer that can be formed.
Example 2:

Input: num = "00009"
Output: "9"
Explanation: 
It can be shown that "9" is the largest palindromic integer that can be formed.
Note that the integer returned should not contain leading zeroes.
 

Constraints:

1 <= num.length <= 105
num consists of digits.
'''
from typing import *
import unittest


class Solution:
    def largestPalindromic(self, num: str) -> str:
        c = Counter(num)
        res = []
        middle = ""
        for n in "9876543210":
            if c[n] >= 2:
                res.append(n * (c[n] // 2))
            if c[n] % 2 == 1 and not middle:
                middle = n
        if res and '0' in res[0]:
            return middle if middle else '0'
        return "".join(res + [middle] + res[::-1])
        


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("444947137",), "7449447"),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().largestPalindromic(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()