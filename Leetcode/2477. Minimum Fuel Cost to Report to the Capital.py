'''
There is a tree (i.e., a connected, undirected graph with no cycles) structure country network consisting of n cities numbered from 0 to n - 1 and exactly n - 1 roads. The capital city is city 0. You are given a 2D integer array roads where roads[i] = [ai, bi] denotes that there exists a bidirectional road connecting cities ai and bi.

There is a meeting for the representatives of each city. The meeting is in the capital city.

There is a car in each city. You are given an integer seats that indicates the number of seats in each car.

A representative can use the car in their city to travel or change the car and ride with another representative. The cost of traveling between two cities is one liter of fuel.

Return the minimum number of liters of fuel to reach the capital city.

 

Example 1:


Input: roads = [[0,1],[0,2],[0,3]], seats = 5
Output: 3
Explanation: 
- Representative1 goes directly to the capital with 1 liter of fuel.
- Representative2 goes directly to the capital with 1 liter of fuel.
- Representative3 goes directly to the capital with 1 liter of fuel.
It costs 3 liters of fuel at minimum. 
It can be proven that 3 is the minimum number of liters of fuel needed.
Example 2:


Input: roads = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]], seats = 2
Output: 7
Explanation: 
- Representative2 goes directly to city 3 with 1 liter of fuel.
- Representative2 and representative3 go together to city 1 with 1 liter of fuel.
- Representative2 and representative3 go together to the capital with 1 liter of fuel.
- Representative1 goes directly to the capital with 1 liter of fuel.
- Representative5 goes directly to the capital with 1 liter of fuel.
- Representative6 goes directly to city 4 with 1 liter of fuel.
- Representative4 and representative6 go together to the capital with 1 liter of fuel.
It costs 7 liters of fuel at minimum. 
It can be proven that 7 is the minimum number of liters of fuel needed.
Example 3:


Input: roads = [], seats = 1
Output: 0
Explanation: No representatives need to travel to the capital city.
 

Constraints:

1 <= n <= 105
roads.length == n - 1
roads[i].length == 2
0 <= ai, bi < n
ai != bi
roads represents a valid tree.
1 <= seats <= 105
'''
import unittest

from typing import *

from collections import defaultdict
from math import ceil
from queue import deque

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        maps = defaultdict(list)
        for u, v in roads:
            maps[u].append(v)
            maps[v].append(u)
        q = deque([])
        for i in range(1, len(roads) + 1):
            if len(maps[i]) == 1:
                q.append(i)
        
        cnt = [1] * (len(roads) + 1)
        res = 0
        while q:
            u = q.popleft()
            res += ceil(cnt[u] / seats)
            v = maps[u][0]
            cnt[v] += cnt[u]
            maps[v].remove(u)
            if v != 0 and len(maps[v]) == 1:
                q.append(v)
        return res
            

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([[0,1],[0,2],[0,3]], 5), 3),
            (([[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]], 2), 7),
            (([], 1), 0),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minimumFuelCost(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
