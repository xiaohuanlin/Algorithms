'''
You are given a string s. It may contain any number of '*' characters. Your task is to remove all '*' characters.

While there is a '*', do the following operation:

Delete the leftmost '*' and the smallest non-'*' character to its left. If there are several smallest characters, you can delete any of them.
Return the 
lexicographically smallest
 resulting string after removing all '*' characters.

 

Example 1:

Input: s = "aaba*"

Output: "aab"

Explanation:

We should delete one of the 'a' characters with '*'. If we choose s[3], s becomes the lexicographically smallest.

Example 2:

Input: s = "abc"

Output: "abc"

Explanation:

There is no '*' in the string.

 

Constraints:

1 <= s.length <= 105
s consists only of lowercase English letters and '*'.
The input is generated such that it is possible to delete all '*' characters.
'''
from typing import *
import unittest


from heapq import heappush, heappop

class Solution:
    def clearStars(self, s: str) -> str:
        l = []
        res = ['' for _ in range(len(s))]

        for i in range(len(s)):
            if s[i] != '*':
                heappush(l, (s[i], -i))
                res[i] = s[i]
            else:
                _, index = heappop(l)
                res[-index] = ''

        return ''.join(res)


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("aaba*",), "aab"),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().clearStars(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()