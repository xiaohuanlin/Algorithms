'''

Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:

Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16 
Explanation: The two words can be "abcw", "xtfn".
Example 2:

Input: ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4 
Explanation: The two words can be "ab", "cd".
Example 3:

Input: ["a","aa","aaa","aaaa"]
Output: 0 
Explanation: No such pair of words.
 

Constraints:

0 <= words.length <= 10^3
0 <= words[i].length <= 10^3
words[i] consists only of lowercase English letters.

'''
import unittest
from typing import *


class Solution:

    def maxProduct(self, words: List[str]) -> int:
        word_set = [set(word) for word in words]   

        max_product = 0
        for i in range(len(word_set)):
            for j in range(i, len(word_set)):
                if (not (word_set[i] & word_set[j]) and (len(words[i]) * len(words[j]) > max_product)):
                    max_product = len(words[i]) * len(words[j])
        return max_product

class TestSolution(unittest.TestCase):

    def test_isPowerOfFour(self):
        examples = (
            ([], 0),
            (["ab", "cd"], 4),
            (["abcw","baz","foo","bar","xtfn","abcdef"], 16),
            (["a","ab","abc","d","cd","bcd","abcd"], 4),
            (["a","aa","aaa","aaaa"], 0)
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maxProduct(first), second, msg="first: {}; second: {}".format(first, second))


unittest.main()