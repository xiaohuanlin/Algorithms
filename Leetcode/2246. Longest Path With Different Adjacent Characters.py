'''
You are given a tree (i.e. a connected, undirected graph that has no cycles) rooted at node 0 consisting of n nodes numbered from 0 to n - 1. The tree is represented by a 0-indexed array parent of size n, where parent[i] is the parent of node i. Since node 0 is the root, parent[0] == -1.

You are also given a string s of length n, where s[i] is the character assigned to node i.

Return the length of the longest path in the tree such that no pair of adjacent nodes on the path have the same character assigned to them.

 

Example 1:


Input: parent = [-1,0,0,1,1,2], s = "abacbe"
Output: 3
Explanation: The longest path where each two adjacent nodes have different characters in the tree is the path: 0 -> 1 -> 3. The length of this path is 3, so 3 is returned.
It can be proven that there is no longer path that satisfies the conditions. 
Example 2:


Input: parent = [-1,0,0,0], s = "aabc"
Output: 3
Explanation: The longest path where each two adjacent nodes have different characters is the path: 2 -> 0 -> 3. The length of this path is 3, so 3 is returned.
 

Constraints:

n == parent.length == s.length
1 <= n <= 105
0 <= parent[i] <= n - 1 for all i >= 1
parent[0] == -1
parent represents a valid tree.
s consists of only lowercase English letters.
'''
from typing import *

import unittest
import heapq

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = {}
        for i in range(len(parent)):
            graph.setdefault(parent[i], []).append(i)
            
        def dfs(node):
            res = 1
            single_lengths = []
            for child in graph.get(node, []):
                max_length, max_single_length = dfs(child)
                res = max(res, max_length)
                if s[child] != s[node]:
                    heapq.heappush(single_lengths, max_single_length)
                    if len(single_lengths) > 2:
                        heapq.heappop(single_lengths)
            res = max(res, sum(single_lengths) + 1)
            return res, max(single_lengths) + 1 if single_lengths else 1
            
        return dfs(0)[0]


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([-1,0,0,1,1,2], "abacbe"), 3),
            (([-1,0,0,0], "aabc"), 3)
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().longestPath(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
