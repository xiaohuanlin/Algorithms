'''
You are given an unrooted weighted tree with n vertices representing servers numbered from 0 to n - 1, an array edges where edges[i] = [ai, bi, weighti] represents a bidirectional edge between vertices ai and bi of weight weighti. You are also given an integer signalSpeed.

Two servers a and b are connectable through a server c if:

a < b, a != c and b != c.
The distance from c to a is divisible by signalSpeed.
The distance from c to b is divisible by signalSpeed.
The path from c to b and the path from c to a do not share any edges.
Return an integer array count of length n where count[i] is the number of server pairs that are connectable through the server i.

 

Example 1:


Input: edges = [[0,1,1],[1,2,5],[2,3,13],[3,4,9],[4,5,2]], signalSpeed = 1
Output: [0,4,6,6,4,0]
Explanation: Since signalSpeed is 1, count[c] is equal to the number of pairs of paths that start at c and do not share any edges.
In the case of the given path graph, count[c] is equal to the number of servers to the left of c multiplied by the servers to the right of c.
Example 2:


Input: edges = [[0,6,3],[6,5,3],[0,3,1],[3,2,7],[3,1,6],[3,4,2]], signalSpeed = 3
Output: [2,0,0,0,0,0,2]
Explanation: Through server 0, there are 2 pairs of connectable servers: (4, 5) and (4, 6).
Through server 6, there are 2 pairs of connectable servers: (4, 5) and (0, 5).
It can be shown that no two servers are connectable through servers other than 0 and 6.
 

Constraints:

2 <= n <= 1000
edges.length == n - 1
edges[i].length == 3
0 <= ai, bi < n
edges[i] = [ai, bi, weighti]
1 <= weighti <= 106
1 <= signalSpeed <= 106
The input is generated such that edges represents a valid tree.
'''
import unittest

from typing import *


from collections import defaultdict
class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        res = []
        maps = defaultdict(list)
        for u, v, w in edges:
            maps[u].append((v, w))
            maps[v].append((u, w))
        
        def dfs(u, w_ori, sets):
            if u in sets:
                return 0
            sets.add(u)
            res = 0
            if w_ori % signalSpeed == 0:
                res += 1

            for v, w in maps[u]:
                res += dfs(v, w_ori + w, sets)
            sets.remove(u)
            return res

        for i in range(len(edges) + 1):
            total = 0
            elements = []

            for v, w in maps[i]:
                elements.append(dfs(v, w, set([i])))

            for i in range(len(elements)):
                for j in range(i+1, len(elements)):
                    total += elements[i] * elements[j]
            res.append(total)
        return res
                

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([[0,6,3],[6,5,3],[0,3,1],[3,2,7],[3,1,6],[3,4,2]], 3), [2,0,0,0,0,0,2]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().countPairsOfConnectableServers(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
