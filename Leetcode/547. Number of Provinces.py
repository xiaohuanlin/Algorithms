'''
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

 

Example 1:


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:


Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
 

Constraints:

1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]
'''
from typing import *

import unittest
    
class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.count = n
        
    def find(self, u):
        while u != self.parent[u]:
            self.parent[u] = self.parent[self.parent[u]]
            u = self.parent[u]
        return u
        
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u == root_v:
            return
        self.parent[root_u] = root_v
        self.count -= 1

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        uf = UF(len(isConnected))
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    uf.union(i, j)
        return uf.count
        
        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([[1,1,0],[1,1,0],[0,0,1]],),2),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().findCircleNum(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
