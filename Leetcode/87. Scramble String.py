'''
We can scramble a string s to get a string t using the following algorithm:

If the length of the string is 1, stop.
If the length of the string is > 1, do the following:
Split the string into two non-empty substrings at a random index, i.e., if the string is s, divide it to x and y where s = x + y.
Randomly decide to swap the two substrings or to keep them in the same order. i.e., after this step, s may become s = x + y or s = y + x.
Apply step 1 recursively on each of the two substrings x and y.
Given two strings s1 and s2 of the same length, return true if s2 is a scrambled string of s1, otherwise, return false.

 

Example 1:

Input: s1 = "great", s2 = "rgeat"
Output: true
Explanation: One possible scenario applied on s1 is:
"great" --> "gr/eat" // divide at random index.
"gr/eat" --> "gr/eat" // random decision is not to swap the two substrings and keep them in order.
"gr/eat" --> "g/r / e/at" // apply the same algorithm recursively on both substrings. divide at random index each of them.
"g/r / e/at" --> "r/g / e/at" // random decision was to swap the first substring and to keep the second substring in the same order.
"r/g / e/at" --> "r/g / e/ a/t" // again apply the algorithm recursively, divide "at" to "a/t".
"r/g / e/ a/t" --> "r/g / e/ a/t" // random decision is to keep both substrings in the same order.
The algorithm stops now, and the result string is "rgeat" which is s2.
As one possible scenario led s1 to be scrambled to s2, we return true.
Example 2:

Input: s1 = "abcde", s2 = "caebd"
Output: false
Example 3:

Input: s1 = "a", s2 = "a"
Output: true
 

Constraints:

s1.length == s2.length
1 <= s1.length <= 30
s1 and s2 consist of lowercase English letters.
'''
from typing import *

import unittest


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        dp = [[[False for _ in range(len(s2))] for _ in range(len(s1))] for _ in range(len(s1)+1)]

        for size in range(1, len(s1)+1):
            if size == 1:
                for i in range(len(s1)):
                    for j in range(len(s2)):
                        dp[size][i][j] = s1[i] == s2[j]
            else:
                for i in range(len(s1)):
                    for j in range(len(s2)):
                        if i + size > len(s1) or j + size > len(s2):
                            continue
                        for k in range(1, size):
                            if dp[k][i][j] and dp[size-k][i+k][j+k] or (dp[k][i][j+size-k] and dp[size-k][i+k][j]):
                                dp[size][i][j] = True
                                break

        return dp[len(s1)][0][0]
                            


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("ab", "aa"), False),
            (("great", "rgeat"), True),
            (("abcde", "caebd"), False),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().isScramble(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
