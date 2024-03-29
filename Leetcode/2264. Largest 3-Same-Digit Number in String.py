'''
You are given a string num representing a large integer. An integer is good if it meets the following conditions:

It is a substring of num with length 3.
It consists of only one unique digit.
Return the maximum good integer as a string or an empty string "" if no such integer exists.

Note:

A substring is a contiguous sequence of characters within a string.
There may be leading zeroes in num or a good integer.
 

Example 1:

Input: num = "6777133339"
Output: "777"
Explanation: There are two distinct good integers: "777" and "333".
"777" is the largest, so we return "777".
Example 2:

Input: num = "2300019"
Output: "000"
Explanation: "000" is the only good integer.
Example 3:

Input: num = "42352338"
Output: ""
Explanation: No substring of length 3 consists of only one unique digit. Therefore, there are no good integers.
 

Constraints:

3 <= num.length <= 1000
num only consists of digits.
'''
from typing import *
import unittest

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_v = -1
        res = ""

        for i in range(len(num)):
            v = int(num[i:i+3])
            if v % 111 == 0 and len(num[i:i+3]) == 3:
                if v > max_v:
                    max_v = v
                    res = num[i:i+3]
        return res
                    

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("6777133339",),"777"),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().largestGoodInteger(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
