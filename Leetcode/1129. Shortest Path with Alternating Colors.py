'''
You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

You are given two arrays redEdges and blueEdges where:

redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist.

 

Example 1:

Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
Output: [0,1,-1]
Example 2:

Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
Output: [0,1,-1]
 

Constraints:

1 <= n <= 100
0 <= redEdges.length, blueEdges.length <= 400
redEdges[i].length == blueEdges[j].length == 2
0 <= ai, bi, uj, vj < n
'''
from typing import *

import unittest

from collections import deque

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red_graph = {}
        for u, v in redEdges:
            red_graph.setdefault(u, []).append(v)
            
        blue_graph = {}
        for u, v in blueEdges:
            blue_graph.setdefault(u, []).append(v)
            
        red_path = [101 for i in range(n)]
        red_path[0] = 0
        blue_path = [101 for i in range(n)]
        blue_path[0] = 0
        
        pq = deque()
        pq.append((0, 0, True))
        pq.append((0, 0, False))
        while pq:
            dis, u, is_red = pq.popleft()
            if is_red:
                for v in blue_graph.get(u, []):
                    if red_path[u] + 1 < blue_path[v]:
                        blue_path[v] = red_path[u] + 1
                        pq.append((blue_path[v], v, False))
            else:
                for v in red_graph.get(u, []):
                    if blue_path[u] + 1 < red_path[v]:
                        red_path[v] = blue_path[u] + 1
                        pq.append((red_path[v], v, True))
        
        for i in range(n):
            red_path[i] = min(red_path[i], blue_path[i])
            if red_path[i] == 101:
                red_path[i] = -1
        return red_path



class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((3, [[0,1],[1,2]], []), [0,1,-1]),
            ((3, [[0,1]], [[2,1]]), [0,1,-1]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().shortestAlternatingPaths(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
