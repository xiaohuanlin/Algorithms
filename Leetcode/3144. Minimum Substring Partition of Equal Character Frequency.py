'''
Given a string s, you need to partition it into one or more balanced substrings. For example, if s == "ababcc" then ("abab", "c", "c"), ("ab", "abc", "c"), and ("ababcc") are all valid partitions, but ("a", "bab", "cc"), ("aba", "bc", "c"), and ("ab", "abcc") are not. The unbalanced substrings are bolded.

Return the minimum number of substrings that you can partition s into.

Note: A balanced string is a string where each character in the string occurs the same number of times.

 

Example 1:

Input: s = "fabccddg"

Output: 3

Explanation:

We can partition the string s into 3 substrings in one of the following ways: ("fab, "ccdd", "g"), or ("fabc", "cd", "dg").

Example 2:

Input: s = "abababaccddb"

Output: 2

Explanation:

We can partition the string s into 2 substrings like so: ("abab", "abaccddb").

 

Constraints:

1 <= s.length <= 1000
s consists only of English lowercase letters.
'''
import unittest
from typing import *
from collections import defaultdict


class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        prev = [defaultdict(int) for _ in range(len(s))]
        dp = [float('inf')] * (len(s) + 1)
        dp[0] = 0
        for i in range(len(s)):
            for j in range(i+1):
                c = prev[j]
                c[s[i]] += 1
                l = list(c.values())
                for k in range(1, len(l)):
                    if l[k] != l[k-1]:
                        break
                else:
                    dp[i+1] = min(dp[j] + 1, dp[i+1])
        return dp[-1]
        

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ("fabccddg", 3),
            ("abababaccddb", 2),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minimumSubstringsInPartition(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

