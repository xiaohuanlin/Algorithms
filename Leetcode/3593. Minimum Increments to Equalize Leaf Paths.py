'''
You are given an integer n and an undirected tree rooted at node 0 with n nodes numbered from 0 to n - 1. This is represented by a 2D array edges of length n - 1, where edges[i] = [ui, vi] indicates an edge from node ui to vi .

Each node i has an associated cost given by cost[i], representing the cost to traverse that node.

The score of a path is defined as the sum of the costs of all nodes along the path.

Your goal is to make the scores of all root-to-leaf paths equal by increasing the cost of any number of nodes by any non-negative amount.

Return the minimum number of nodes whose cost must be increased to make all root-to-leaf path scores equal.

 

Example 1:

Input: n = 3, edges = [[0,1],[0,2]], cost = [2,1,3]

Output: 1

Explanation:



There are two root-to-leaf paths:

Path 0 → 1 has a score of 2 + 1 = 3.
Path 0 → 2 has a score of 2 + 3 = 5.
To make all root-to-leaf path scores equal to 5, increase the cost of node 1 by 2.
Only one node is increased, so the output is 1.

Example 2:

Input: n = 3, edges = [[0,1],[1,2]], cost = [5,1,4]

Output: 0

Explanation:



There is only one root-to-leaf path:

Path 0 → 1 → 2 has a score of 5 + 1 + 4 = 10.

Since only one root-to-leaf path exists, all path costs are trivially equal, and the output is 0.

Example 3:

Input: n = 5, edges = [[0,4],[0,1],[1,2],[1,3]], cost = [3,4,1,1,7]

Output: 1

Explanation:



There are three root-to-leaf paths:

Path 0 → 4 has a score of 3 + 7 = 10.
Path 0 → 1 → 2 has a score of 3 + 4 + 1 = 8.
Path 0 → 1 → 3 has a score of 3 + 4 + 1 = 8.
To make all root-to-leaf path scores equal to 10, increase the cost of node 1 by 2. Thus, the output is 1.

 

Constraints:

2 <= n <= 105
edges.length == n - 1
edges[i] == [ui, vi]
0 <= ui, vi < n
cost.length == n
1 <= cost[i] <= 109
The input is generated such that edges represents a valid tree.
'''
from collections import defaultdict
import unittest
from typing import *


class Solution:
    def minIncrease(self, n: int, edges: List[List[int]], cost: List[int]) -> int:
        m = defaultdict(list)
        for u, v in edges:
            m[u].append(v)
            m[v].append(u)

        def dfs(node, parent):
            maxv = 0
            maxc = 0
            cnt = 0
            for v in m[node]:
                if v == parent:
                    continue
                cnt += 1
                changed, total = dfs(v, node)
                cnt += changed
                if maxv < total:
                    maxv = total
                    maxc = 1
                elif maxv == total:
                    maxc += 1
            return cnt - maxc, maxv + cost[node]

        return dfs(0, None)[0]
        
        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((3, [[0,1],[0,2]], [2,1,3]), 1),
            ((3, [[0,1],[1,2]], [5,1,4]), 0),
            ((5, [[0,4],[0,1],[1,2],[1,3]], [3,4,1,1,7]), 1),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minIncrease(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
