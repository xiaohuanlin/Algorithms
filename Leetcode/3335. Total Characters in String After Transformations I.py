'''
You are given a string s and an integer t, representing the number of transformations to perform. In one transformation, every character in s is replaced according to the following rules:

If the character is 'z', replace it with the string "ab".
Otherwise, replace it with the next character in the alphabet. For example, 'a' is replaced with 'b', 'b' is replaced with 'c', and so on.
Return the length of the resulting string after exactly t transformations.

Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: s = "abcyy", t = 2

Output: 7

Explanation:

First Transformation (t = 1):
'a' becomes 'b'
'b' becomes 'c'
'c' becomes 'd'
'y' becomes 'z'
'y' becomes 'z'
String after the first transformation: "bcdzz"
Second Transformation (t = 2):
'b' becomes 'c'
'c' becomes 'd'
'd' becomes 'e'
'z' becomes "ab"
'z' becomes "ab"
String after the second transformation: "cdeabab"
Final Length of the string: The string is "cdeabab", which has 7 characters.
Example 2:

Input: s = "azbk", t = 1

Output: 5

Explanation:

First Transformation (t = 1):
'a' becomes 'b'
'z' becomes "ab"
'b' becomes 'c'
'k' becomes 'l'
String after the first transformation: "babcl"
Final Length of the string: The string is "babcl", which has 5 characters.
 

Constraints:

1 <= s.length <= 105
s consists only of lowercase English letters.
1 <= t <= 105
'''
import unittest

from typing import *


class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        c = [0] * 26
        for w in s:
            c[ord(w) - ord('a')] += 1

        m = int(1e9 + 7)
        for _ in range(t):
            nc = [0] * 26
            for i in range(26):
                if i == 25:
                    nc[0] += c[25]
                    nc[0] %= m
                    nc[1] += c[25]
                    nc[1] %= m
                else:
                    nc[i+1] += c[i]
            c = nc
        return sum(c) % m



class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("abcyy", 2), 7),
            (("azbk", 1), 5),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().lengthAfterTransformations(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
