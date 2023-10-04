'''
You are given a 0-indexed string text and another 0-indexed string pattern of length 2, both of which consist of only lowercase English letters.

You can add either pattern[0] or pattern[1] anywhere in text exactly once. Note that the character can be added even at the beginning or at the end of text.

Return the maximum number of times pattern can occur as a subsequence of the modified text.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

 

Example 1:

Input: text = "abdcdbc", pattern = "ac"
Output: 4
Explanation:
If we add pattern[0] = 'a' in between text[1] and text[2], we get "abadcdbc". Now, the number of times "ac" occurs as a subsequence is 4.
Some other strings which have 4 subsequences "ac" after adding a character to text are "aabdcdbc" and "abdacdbc".
However, strings such as "abdcadbc", "abdccdbc", and "abdcdbcc", although obtainable, have only 3 subsequences "ac" and are thus suboptimal.
It can be shown that it is not possible to get more than 4 subsequences "ac" by adding only one character.
Example 2:

Input: text = "aabb", pattern = "ab"
Output: 6
Explanation:
Some of the strings which can be obtained from text and have 6 subsequences "ab" are "aaabb", "aaabb", and "aabbb".
 

Constraints:

1 <= text.length <= 105
pattern.length == 2
text and pattern consist only of lowercase English letters.
'''

from typing import *

import unittest


from math import comb
class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        if pattern[0] == pattern[1]:
            n = text.count(pattern[0])
            return comb(n + 1, 2)
        else:
            count_0 = 0
            count_1 = 0
            res = 0
            for i in range(len(text))[::-1]:
                if text[i] == pattern[1]:
                    count_1 += 1
                elif text[i] == pattern[0]:
                    res += count_1
                    count_0 += 1
            return res + max(count_0, count_1)

        
class TestSolution(unittest.TestCase):
    def test_case(self):
        examples = (
            (("abdcdbc","ac"),4),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maximumSubsequenceCount(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

