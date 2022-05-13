'''
You are given a string text. You can swap two of the characters in the text.

Return the length of the longest substring with repeated characters.

 

Example 1:

Input: text = "ababa"
Output: 3
Explanation: We can swap the first 'b' with the last 'a', or the last 'b' with the first 'a'. Then, the longest repeated character substring is "aaa" with length 3.
Example 2:

Input: text = "aaabaaa"
Output: 6
Explanation: Swap 'b' with the last 'a' (or the first 'a'), and we get longest repeated character substring "aaaaaa" with length 6.
Example 3:

Input: text = "aaaaa"
Output: 5
Explanation: No need to swap, longest repeated character substring is "aaaaa" with length is 5.
 

Constraints:

1 <= text.length <= 2 * 104
text consist of lowercase English characters only.
'''
import unittest

from typing import *

class Solution:
    def maxRepOpt1(self, text: str) -> int:
        maps = {}
        start = 0
        for i in range(1, len(text)):
            if text[i] != text[i - 1]:
                maps.setdefault(text[i-1], []).append((start, i))
                start = i
        maps.setdefault(text[-1], []).append((start, len(text)))
            
        res = 0
        for v in maps.values():
            for i in range(len(v)):
                res = max(res, v[i][1] - v[i][0] + int(len(v) > 1))
                if i > 0 and v[i][0] - v[i-1][1] == 1:
                    res = max(res, v[i][1] - v[i-1][0] - int(len(v) <= 2))
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("ababa",),3),
            (("aaabaaa",),6)
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maxRepOpt1(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()