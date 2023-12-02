'''
There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.

You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.

 

Example 1:


Input: edges = [[1,2],[2,3],[4,2]]
Output: 2
Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.
Example 2:

Input: edges = [[1,2],[5,1],[1,3],[1,4]]
Output: 1
 

Constraints:

3 <= n <= 105
edges.length == n - 1
edges[i].length == 2
1 <= ui, vi <= n
ui != vi
The given edges represent a valid star graph.
'''

from typing import *
import unittest


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        counts = [0 for _ in range(n)]
        for u, v in edges:
            counts[u-1] += 1
            counts[v-1] += 1

        for i in range(n):
            if counts[i] == n - 1:
                return i + 1
        return -1


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([[1,2],[2,3],[4,2]],),2),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().findCenter(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()