'''
A wonderful string is a string where at most one letter appears an odd number of times.

For example, "ccjjc" and "abab" are wonderful, but "ab" is not.
Given a string word that consists of the first ten lowercase English letters ('a' through 'j'), return the number of wonderful non-empty substrings in word. If the same substring appears multiple times in word, then count each occurrence separately.

A substring is a contiguous sequence of characters in a string.

 

Example 1:

Input: word = "aba"
Output: 4
Explanation: The four wonderful substrings are underlined below:
- "aba" -> "a"
- "aba" -> "b"
- "aba" -> "a"
- "aba" -> "aba"
Example 2:

Input: word = "aabb"
Output: 9
Explanation: The nine wonderful substrings are underlined below:
- "aabb" -> "a"
- "aabb" -> "aa"
- "aabb" -> "aab"
- "aabb" -> "aabb"
- "aabb" -> "a"
- "aabb" -> "abb"
- "aabb" -> "b"
- "aabb" -> "bb"
- "aabb" -> "b"
Example 3:

Input: word = "he"
Output: 2
Explanation: The two wonderful substrings are underlined below:
- "he" -> "h"
- "he" -> "e"
 

Constraints:

1 <= word.length <= 105
word consists of lowercase English letters from 'a' to 'j'.
'''
from typing import *

import unittest

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        pre = {0: 1}
        for i in range(10):
            key = (1 << i)
            pre[key] = pre.setdefault(key, 0) + 1
        cur = 0
        sum_v = 0
        for i in range(len(word)):
            cur ^= (1 << (ord(word[i]) - ord('a')))
            if cur in pre:
                sum_v += pre[cur]
                
            pre[cur] = pre.setdefault(cur, 0) + 1
            for j in range(10):
                key = cur ^ (1 << j)
                pre[key] = pre.setdefault(key, 0) + 1
        
        return sum_v
        
        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            # (("aba",), 4),
            (("aabb",), 9),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().wonderfulSubstrings(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
