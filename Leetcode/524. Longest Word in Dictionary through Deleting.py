'''
Given a string s and a string array dictionary, return the longest string in the dictionary that can be formed by deleting some of the given string characters. If there is more than one possible result, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

 

Example 1:

Input: s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
Output: "apple"
Example 2:

Input: s = "abpcplea", dictionary = ["a","b","c"]
Output: "a"
 

Constraints:

1 <= s.length <= 1000
1 <= dictionary.length <= 1000
1 <= dictionary[i].length <= 1000
s and dictionary[i] consist of lowercase English letters.
'''
from typing import *
from pprint import pprint
from collections import deque

import unittest

class TrieTree:
    def __init__(self, val) -> None:
        self.val = val
        self.children = {}
        self.end = False

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        root = TrieTree("")
        for w in dictionary:
            iter = root
            for c in w:
                node = TrieTree("c")
                iter.children.setdefault(c, []).append(node)
                iter = node
            iter.end = True
        
        positions = [{} for _ in range(len(s) + 1)]
        for i in range(len(s) - 1, -1, -1):
            positions[i] = positions[i + 1].copy()
            positions[i][s[i]] = i
        
        # bfs
        queue = deque()
        queue.append((root, "", -1))
        res = ""
        while queue:
            node, path, index = queue.popleft()
            if node.end:
                if len(path) > len(res):
                    res = path
                elif len(path) == len(res) and path < res:
                    res = path

            for k, child in node.children.items():
                for c in child:
                    if k in positions[index + 1]:
                        queue.append((c, path + k, positions[index + 1][k]))
            
        return res
                




class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("a", ["aaa"]), ""),
            (("abpcplea", ["ale","apple","monkey","plea"]), "apple"),
            (("abpcplea", ["a","b","c"]), "a"),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().findLongestWord(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
