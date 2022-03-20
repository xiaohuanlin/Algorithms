'''
You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.

 

Example 1:

Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
Output: 2
Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
Example 2:

Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
Output: -1
 

Constraints:

1 <= routes.length <= 500.
1 <= routes[i].length <= 105
All the values of routes[i] are unique.
sum(routes[i].length) <= 105
0 <= routes[i][j] < 106
0 <= source, target < 106
'''
from typing import *

import unittest
from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        graph = defaultdict(list)
        for j, route in enumerate(routes):
            for i in range(len(route)):
                graph[route[i]].append(j)
        
        q = deque()
        q.append(source)
        distance = 0
        visit = set()
        while q:
            size = len(q)
            for _ in range(size):
                n = q.popleft()
                if n in visit:
                    continue
                if n == target:
                    return distance
                visit.add(n)
                for next_route in graph[n]:
                    for next_ in routes[next_route]:
                        q.append(next_)
                    routes[next_route] = []
            distance += 1
        return -1


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([[1,2,7],[3,6,7]], 1, 6), 2),
            (([[7,12],[4,5,15],[6],[15,19],[9,12,13]], 15, 12), -1)
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().numBusesToDestination(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
