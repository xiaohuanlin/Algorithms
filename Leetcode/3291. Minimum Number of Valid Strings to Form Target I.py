'''
You are given an array of strings words and a string target.

A string x is called valid if x is a
prefix
 of any string in words.

Return the minimum number of valid strings that can be concatenated to form target. If it is not possible to form target, return -1.



Example 1:

Input: words = ["abc","aaaaa","bcdef"], target = "aabcdabc"

Output: 3

Explanation:

The target string can be formed by concatenating:

Prefix of length 2 of words[1], i.e. "aa".
Prefix of length 3 of words[2], i.e. "bcd".
Prefix of length 3 of words[0], i.e. "abc".
Example 2:

Input: words = ["abababab","ab"], target = "ababaababa"

Output: 2

Explanation:

The target string can be formed by concatenating:

Prefix of length 5 of words[0], i.e. "ababa".
Prefix of length 5 of words[0], i.e. "ababa".
Example 3:

Input: words = ["abcdef"], target = "xyz"

Output: -1



Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 5 * 103
The input is generated such that sum(words[i].length) <= 105.
words[i] consists only of lowercase English letters.
1 <= target.length <= 5 * 103
target consists only of lowercase English letters.
'''
import unittest

from typing import *

class Node:
    def __init__(self) -> None:
        self.children = {}

    def insert(self, c):
        if c not in self.children:
            self.children[c] = Node()
        return self.children[c]

    def get(self, c):
        return self.children.get(c)

class Trie:
    def __init__(self) -> None:
        self.root = Node()

    def insert(self, w):
        node = self.root
        for c in w:
            node = node.insert(c)

    def all_prefix(self, s, start, end):
        node = self.root
        res = []
        for i in range(start, end):
            node = node.get(s[i])
            if node is None:
                break
            res.append(i)
        return res

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        t = Trie()
        for w in words:
            t.insert(w)

        dp = [float('inf') for _ in range(len(target) + 1)]
        dp[0] = 0
        for i in range(len(target) + 1):
            all_prefix = t.all_prefix(target, i, len(target))
            for j in all_prefix:
                dp[j+1] = min(dp[j+1], dp[i] + 1)

        return dp[-1] if dp[-1] != float('inf') else -1


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((["abc","aaaaa","bcdef"], "aabcdabc"), 3),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minValidStrings(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
