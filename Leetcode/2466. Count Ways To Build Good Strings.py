'''
Given the integers zero, one, low, and high, we can construct a string by starting with an empty string, and then at each step perform either of the following:

Append the character '0' zero times.
Append the character '1' one times.
This can be performed any number of times.

A good string is a string constructed by the above process having a length between low and high (inclusive).

Return the number of different good strings that can be constructed satisfying these properties. Since the answer can be large, return it modulo 109 + 7.

 

Example 1:

Input: low = 3, high = 3, zero = 1, one = 1
Output: 8
Explanation: 
One possible valid good string is "011". 
It can be constructed as follows: "" -> "0" -> "01" -> "011". 
All binary strings from "000" to "111" are good strings in this example.
Example 2:

Input: low = 2, high = 3, zero = 1, one = 2
Output: 5
Explanation: The good strings are "00", "11", "000", "110", and "011".
 

Constraints:

1 <= low <= high <= 105
1 <= zero, one <= low
'''

from typing import *
import unittest

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0 for _ in range(high + 1)]
        dp[0] = 1
        res = 0
        m = int(1e9) + 7
        for i in range(1, high + 1):
            dp[i] = (dp[i - zero] if i - zero >= 0 else 0) + (dp[i - one] if i - one >= 0 else 0)
            if i >= low:
                res = (res + dp[i]) % m
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((3,3,1,1),8),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().countGoodStrings(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()