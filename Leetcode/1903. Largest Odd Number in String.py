'''
You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: num = "52"
Output: "5"
Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.
Example 2:

Input: num = "4206"
Output: ""
Explanation: There are no odd numbers in "4206".
Example 3:

Input: num = "35427"
Output: "35427"
Explanation: "35427" is already an odd number.
 

Constraints:

1 <= num.length <= 105
num only consists of digits and does not contain any leading zeros.
'''
import unittest

from typing import *


class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num))[::-1]:
            if num[i] in ('1', '3', '5', '7', '9'):
                return num[:i+1]
        return ""
                

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("35427",),"35427"),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().largestOddNumber(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
