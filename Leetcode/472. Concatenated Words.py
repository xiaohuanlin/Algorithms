'''
Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

 

Example 1:

Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
"dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
Example 2:

Input: words = ["cat","dog","catdog"]
Output: ["catdog"]
 

Constraints:

1 <= words.length <= 104
0 <= words[i].length <= 30
words[i] consists of only lowercase English letters.
0 <= sum(words[i].length) <= 105
'''
from typing import *

import unittest
from functools import lru_cache

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        word_set = set(words)
        res = []
        
        @lru_cache(None)
        def dfs(word):
            if word == "":
                return 0
            for i in range(len(word)):
                if word[:i + 1] in word_set:
                    if i + 1 == len(word):
                        return 1
                    if dfs(word[i + 1:]) > 0:
                        return 2
            return -1
        
        for w in words:
            if dfs(w) > 1:
                res.append(w)
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((["cat","dog","catdog"],),["catdog"]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().findAllConcatenatedWordsInADict(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
