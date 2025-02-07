'''
You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.

Return the number of special letters in word.

 

Example 1:

Input: word = "aaAbcBC"

Output: 3

Explanation:

The special characters in word are 'a', 'b', and 'c'.

Example 2:

Input: word = "abc"

Output: 0

Explanation:

No character in word appears in uppercase.

Example 3:

Input: word = "abBCab"

Output: 1

Explanation:

The only special character in word is 'b'.

 

Constraints:

1 <= word.length <= 50
word consists of only lowercase and uppercase English letters.
'''
import unittest

from typing import *


from string import ascii_lowercase

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s = set(word)
        res = 0
        for a in ascii_lowercase:
            if a in s and a.upper() in s:
                res += 1
        return res

    
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("aaAbcBC",),3),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().numberOfSpecialChars(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
