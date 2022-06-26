'''
You are given two string arrays words1 and words2.

A string b is a subset of string a if every letter in b occurs in a including multiplicity.

For example, "wrr" is a subset of "warrior" but is not a subset of "world".
A string a from words1 is universal if for every string b in words2, b is a subset of a.

Return an array of all the universal strings in words1. You may return the answer in any order.

 

Example 1:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
Output: ["facebook","google","leetcode"]
Example 2:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]
Output: ["apple","google","leetcode"]
 

Constraints:

1 <= words1.length, words2.length <= 104
1 <= words1[i].length, words2[i].length <= 10
words1[i] and words2[i] consist only of lowercase English letters.
All the strings of words1 are unique.
'''
import unittest
from typing import *

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        requires = [0 for _ in range(26)]
        for w in words2:
            tmp = [0 for _ in range(26)]
            for s in w:
                tmp[ord(s) - ord('a')] += 1
                
            for i in range(26):
                requires[i] = max(requires[i], tmp[i])
                
        res = []
        for w in words1:
            tmp = [0 for _ in range(26)]
            for s in w:
                tmp[ord(s) - ord('a')] += 1
                
            if all(tmp[i] >= requires[i] for i in range(26)):
                res.append(w)
        return res

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((["amazon","apple","facebook","google","leetcode"], ["e","o"]), ["facebook","google","leetcode"]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().wordSubsets(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()