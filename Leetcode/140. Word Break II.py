'''
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
Example 2:

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []
 

Constraints:

1 <= s.length <= 20
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 10
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
'''

from typing import *

import unittest


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        string_map = {}
        word_set = set(wordDict)
        for i in range(len(s)):
            for j in range(len(s)):
                if s[i:j+1] in word_set:
                    string_map.setdefault(i, []).append(j + 1)
        return self.helper(s, 0, string_map)
    
    def helper(self, s: str, start_index: int, string_map: Dict[int, List[int]]):
        res = []
        for end in string_map.get(start_index, []):
            if end == len(s):
                res.append(s[start_index:end])
            else:
                for ans in self.helper(s, end, string_map):
                    res.append(s[start_index:end] + " " + ans)
        return res



class TestSolution(unittest.TestCase):
    def test_case(self):
        examples = (
            (("catsanddog", ["cat","cats","and","sand","dog"]), ["cats and dog","cat sand dog"]),
            (("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"]), ["pine apple pen apple","pineapple pen apple","pine applepen apple"]),
            (("catsandog", ["cats","dog","sand","and","cat"]), []),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().wordBreak(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()