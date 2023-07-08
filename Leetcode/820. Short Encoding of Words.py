'''
A valid encoding of an array of words is any reference string s and array of indices indices such that:

words.length == indices.length
The reference string s ends with the '#' character.
For each index indices[i], the substring of s starting from indices[i] and up to (but not including) the next '#' character is equal to words[i].
Given an array of words, return the length of the shortest reference string s possible of any valid encoding of words.

 

Example 1:

Input: words = ["time", "me", "bell"]
Output: 10
Explanation: A valid encoding would be s = "time#bell#" and indices = [0, 2, 5].
words[0] = "time", the substring of s starting from indices[0] = 0 to the next '#' is underlined in "time#bell#"
words[1] = "me", the substring of s starting from indices[1] = 2 to the next '#' is underlined in "time#bell#"
words[2] = "bell", the substring of s starting from indices[2] = 5 to the next '#' is underlined in "time#bell#"
Example 2:

Input: words = ["t"]
Output: 2
Explanation: A valid encoding would be s = "t#" and indices = [0].
 

Constraints:

1 <= words.length <= 2000
1 <= words[i].length <= 7
words[i] consists of only lowercase letters.
'''
from typing import *

import unittest


class Node:
    def __init__(self, key, depth=1):
        self.key = key
        self.children = {}
        self.depth = depth
    
    def insert(self, s, index):
        if index >= len(s):
            return
        key = s[index]
        if key not in self.children:
            self.children[key] = Node(key, self.depth + 1)
        self.children[key].insert(s, index+1)


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        dummy = Node(None)
        for w in words:
            dummy.insert(w[::-1], 0)
        
        res = 0
        def dfs(node):
            nonlocal res
            if not node.children:
                res += node.depth
                return
            for child in node.children.values():
                dfs(child)
        dfs(dummy)
        return res

        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((["time", "me", "bell"],),10),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minimumLengthEncoding(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
