'''
You are given an integer n.

A string s is called good if it contains only lowercase English characters and it is possible to rearrange the characters of s such that the new string contains "leet" as a substring.

For example:

The string "lteer" is good because we can rearrange it to form "leetr" .
"letl" is not good because we cannot rearrange it to contain "leet" as a substring.
Return the total number of good strings of length n.

Since the answer may be large, return it modulo 109 + 7.

A substring is a contiguous sequence of characters within a string.

 
 

Example 1:

Input: n = 4
Output: 12
Explanation: The 12 strings which can be rearranged to have "leet" as a substring are: "eelt", "eetl", "elet", "elte", "etel", "etle", "leet", "lete", "ltee", "teel", "tele", and "tlee".
Example 2:

Input: n = 10
Output: 83943898
Explanation: The number of strings with length 10 which can be rearranged to have "leet" as a substring is 526083947580. Hence the answer is 526083947580 % (109 + 7) = 83943898.
 

Constraints:

1 <= n <= 105
'''
import unittest

from typing import *


class Solution:
    def stringCount(self, n: int) -> int:
        dp = [[0 for _ in range(2**4)] for _ in range(n)]
        dp[0][0] = 23
        dp[0][1] = 1
        dp[0][2] = 1
        dp[0][8] = 1

        mod = int(1e9 + 7)
        for i in range(1, len(dp)):
            for j in range(16):
                dp[i][j] = (dp[i][j] +23 * dp[i-1][j]) % mod # other
                dp[i][j | 1] = (dp[i][j | 1] + dp[i-1][j]) % mod # l
                if j & 2:
                    dp[i][j | 4] = (dp[i][j | 4] + dp[i-1][j]) % mod # e
                else:
                    dp[i][j | 2] = (dp[i][j | 2] + dp[i-1][j]) % mod # e
                dp[i][j | 8] = (dp[i][j | 8] + dp[i-1][j]) % mod # t
        return dp[-1][-1]
                

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((10,),83943898),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().stringCount(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
