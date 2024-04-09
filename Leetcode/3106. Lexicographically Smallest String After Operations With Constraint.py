'''
You are given a string s and an integer k.

Define a function distance(s1, s2) between two strings s1 and s2 of the same length n as:

The sum of the minimum distance between s1[i] and s2[i] when the characters from 'a' to 'z' are placed in a cyclic order, for all i in the range [0, n - 1].
For example, distance("ab", "cd") == 4, and distance("a", "z") == 1.

You can change any letter of s to any other lowercase English letter, any number of times.

Return a string denoting the
lexicographically smallest
 string t you can get after some changes, such that distance(s, t) <= k.



Example 1:

Input: s = "zbbz", k = 3

Output: "aaaz"

Explanation:

Change s to "aaaz". The distance between "zbbz" and "aaaz" is equal to k = 3.

Example 2:

Input: s = "xaxcd", k = 4

Output: "aawcd"

Explanation:

The distance between "xaxcd" and "aawcd" is equal to k = 4.

Example 3:

Input: s = "lol", k = 0

Output: "lol"

Explanation:

It's impossible to change any character as k = 0.



Constraints:

1 <= s.length <= 100
0 <= k <= 2000
s consists only of lowercase English letters.
'''
import unittest

from typing import *
from string import ascii_lowercase


class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        res = []
        con_s = ascii_lowercase * 3
        for w in s:
            delta = min(ord(w) - ord('a'), ord('a') + 26 - ord(w))
            if k >= delta:
                res.append('a')
                k -= delta
            else:
                index = ord(w) - ord('a') + 26
                res.append(min(con_s[index - k], con_s[index + k]))
                k = 0
        return ''.join(res)



class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("xaxcd", 4), "aawcd"),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().getSmallestString(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
