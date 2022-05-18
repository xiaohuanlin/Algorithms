'''
Given the string s, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.

 

Example 1:

Input: s = "eleetminicoworoep"
Output: 13
Explanation: The longest substring is "leetminicowor" which contains two each of the vowels: e, i and o and zero of the vowels: a and u.
Example 2:

Input: s = "leetcodeisgreat"
Output: 5
Explanation: The longest substring is "leetc" which contains two e's.
Example 3:

Input: s = "bcbcbc"
Output: 6
Explanation: In this case, the given string "bcbcbc" is the longest because all vowels: a, e, i, o and u appear zero times.
 

Constraints:

1 <= s.length <= 5 x 10^5
s contains only lowercase English letters.
'''
import unittest

from typing import *

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        maps = {0: -1}
        xor_v_map = {
            'a': 1,
            'e': 2,
            'i': 4,
            'o': 8,
            'u': 16
        }
        xor = 0
        res = 0
        for i in range(len(s)):
            xor ^= xor_v_map.get(s[i], 0)
            if xor not in maps:
                maps[xor] = i
            else:
                res = max(res, i - maps[xor])
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("eleetminicoworoep",), 13),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().findTheLongestSubstring(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()