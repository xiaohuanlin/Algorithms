'''
A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each of the words consists of only uppercase and lowercase English letters (no punctuation).

For example, "Hello World", "HELLO", and "hello world hello world" are all sentences.
You are given a sentence s​​​​​​ and an integer k​​​​​​. You want to truncate s​​​​​​ such that it contains only the first k​​​​​​ words. Return s​​​​​​ after truncating it.

 

Example 1:

Input: s = "Hello how are you Contestant", k = 4
Output: "Hello how are you"
Explanation:
The words in s are ["Hello", "how" "are", "you", "Contestant"].
The first 4 words are ["Hello", "how", "are", "you"].
Hence, you should return "Hello how are you".
Example 2:

Input: s = "What is the solution to this problem", k = 4
Output: "What is the solution"
Explanation:
The words in s are ["What", "is" "the", "solution", "to", "this", "problem"].
The first 4 words are ["What", "is", "the", "solution"].
Hence, you should return "What is the solution".
Example 3:

Input: s = "chopper is not a tanuki", k = 5
Output: "chopper is not a tanuki"
 

Constraints:

1 <= s.length <= 500
k is in the range [1, the number of words in s].
s consist of only lowercase and uppercase English letters and spaces.
The words in s are separated by a single space.
There are no leading or trailing spaces.
'''
import unittest

from typing import *


class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        cnt = 0
        res = []
        w = []
        for i in range(len(s)):
            if s[i] == ' ':
                if w:
                    cnt += 1
                    res.append(''.join(w))
                    w = []
                if len(res) == k:
                    break
            else:
                w.append(s[i])
        if w:
            res.append(''.join(w))
        return ' '.join(res)

        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("What is the solution to this problem", 4), "What is the solution"),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().truncateSentence(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
