'''
A string is considered beautiful if it satisfies the following conditions:

Each of the 5 English vowels ('a', 'e', 'i', 'o', 'u') must appear at least once in it.
The letters must be sorted in alphabetical order (i.e. all 'a's before 'e's, all 'e's before 'i's, etc.).
For example, strings "aeiou" and "aaaaaaeiiiioou" are considered beautiful, but "uaeio", "aeoiu", and "aaaeeeooo" are not beautiful.

Given a string word consisting of English vowels, return the length of the longest beautiful substring of word. If no such substring exists, return 0.

A substring is a contiguous sequence of characters in a string.

 

Example 1:

Input: word = "aeiaaioaaaaeiiiiouuuooaauuaeiu"
Output: 13
Explanation: The longest beautiful substring in word is "aaaaeiiiiouuu" of length 13.
Example 2:

Input: word = "aeeeiiiioooauuuaeiou"
Output: 5
Explanation: The longest beautiful substring in word is "aeiou" of length 5.
Example 3:

Input: word = "a"
Output: 0
Explanation: There is no beautiful substring, so return 0.
 

Constraints:

1 <= word.length <= 5 * 105
word consists of characters 'a', 'e', 'i', 'o', and 'u'.
'''
from typing import *

import unittest

class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        res = 0
        vowels = ['a', 'e', 'i', 'o', 'u']
        i = 0

        while i < len(word):
            if word[i] == 'a':
                cur = 0
                start = i
                while start < len(word):
                    if word[start] == vowels[cur]:
                        pass
                    elif cur < 4 and word[start] == vowels[cur+1]:
                        cur += 1
                    else:
                        break
                    start += 1
                if cur == 4:
                    res = max(res, start - i)
                i = start
            else:
                i += 1
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("aeiaaioaaaaeiiiiouuuooaauuaeiu",),13),
        )

        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().longestBeautifulSubstring(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
