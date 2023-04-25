'''
Given a string word to which you can insert letters "a", "b" or "c" anywhere and any number of times, return the minimum number of letters that must be inserted so that word becomes valid.

A string is called valid if it can be formed by concatenating the string "abc" several times.

 

Example 1:

Input: word = "b"
Output: 2
Explanation: Insert the letter "a" right before "b", and the letter "c" right next to "a" to obtain the valid string "abc".
Example 2:

Input: word = "aaa"
Output: 6
Explanation: Insert letters "b" and "c" next to each "a" to obtain the valid string "abcabcabc".
Example 3:

Input: word = "abc"
Output: 0
Explanation: word is already valid. No modifications are needed. 
 

Constraints:

1 <= word.length <= 50
word consists of letters "a", "b" and "c" only. 
'''
from typing import *
import unittest

class Solution:
    def addMinimum(self, word: str) -> int:
        start = 0
        res = 0
        while start < len(word):
            s = word[start:start + 3]
            if s == 'abc':
                start += 3
            elif s[:2] == 'aa' or s[:2] == 'ba' or s[:2] == 'bb' or s[:1] == 'c':
                res += 2
                start += 1
            elif s[:2] == 'ac' or s[:2] == 'ab':
                res += 1
                start += 2
            elif s[:2] == 'bc':
                res += 1
                start += 2
            elif len(s) == 1:
                res += 2
                start += 1
        return res
                    

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("abc",),0),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().addMinimum(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
