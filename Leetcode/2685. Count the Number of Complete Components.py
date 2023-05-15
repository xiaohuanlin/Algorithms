'''
You are given an integer n. There is an undirected graph with n vertices, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting vertices ai and bi.

Return the number of complete connected components of the graph.

A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.

A connected component is said to be complete if there exists an edge between every pair of its vertices.

 

Example 1:



Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]
Output: 3
Explanation: From the picture above, one can see that all of the components of this graph are complete.
Example 2:



Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
Output: 1
Explanation: The component containing vertices 0, 1, and 2 is complete since there is an edge between every pair of two vertices. On the other hand, the component containing vertices 3, 4, and 5 is not complete since there is no edge between vertices 4 and 5. Thus, the number of complete components in this graph is 1.
 

Constraints:

1 <= n <= 50
0 <= edges.length <= n * (n - 1) / 2
edges[i].length == 2
0 <= ai, bi <= n - 1
ai != bi
There are no repeated edges.
'''
import unittest

from typing import *

class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.pairs = [0 for _ in range(n)]
        self.counts = [1 for _ in range(n)]
        self.count = n

    def find(self, v):
        tmp = v
        while tmp != self.root[tmp]:
            tmp = self.root[tmp]
        
        while v != self.root[v]:
            next_ = self.root[v]
            self.root[v] = tmp
            v = next_
        return v

    def is_connected(self, u, v):
        return self.find(u) == self.find(v)

    def connect(self, u, v):
        if self.is_connected(u, v):
            self.pairs[self.find(u)] += 1
            return
        u_root = self.find(u)
        v_root = self.find(v)
        self.root[u_root] = v_root
        self.count -= 1
        self.pairs[v_root] += (self.pairs[u_root] + 1)
        self.counts[v_root] += self.counts[u_root]

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for u, v in edges:
            uf.connect(u, v)

        roots = set()
        for r in uf.root:
            roots.add(uf.find(r))

        res = 0
        for r in roots:
            if uf.pairs[r] == (uf.counts[r] * (uf.counts[r] - 1)) // 2:
                res += 1
        return res

        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((6, [[0,1],[0,2],[1,2],[3,4]]), 3),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().countCompleteComponents(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
