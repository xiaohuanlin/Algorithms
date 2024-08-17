'''
You are given an integer n and a 2D integer array queries.

There are n cities numbered from 0 to n - 1. Initially, there is a unidirectional road from city i to city i + 1 for all 0 <= i < n - 1.

queries[i] = [ui, vi] represents the addition of a new unidirectional road from city ui to city vi. After each query, you need to find the length of the shortest path from city 0 to city n - 1.

Return an array answer where for each i in the range [0, queries.length - 1], answer[i] is the length of the shortest path from city 0 to city n - 1 after processing the first i + 1 queries.

 

Example 1:

Input: n = 5, queries = [[2,4],[0,2],[0,4]]

Output: [3,2,1]

Explanation:



After the addition of the road from 2 to 4, the length of the shortest path from 0 to 4 is 3.



After the addition of the road from 0 to 2, the length of the shortest path from 0 to 4 is 2.



After the addition of the road from 0 to 4, the length of the shortest path from 0 to 4 is 1.

Example 2:

Input: n = 4, queries = [[0,3],[0,2]]

Output: [1,1]

Explanation:



After the addition of the road from 0 to 3, the length of the shortest path from 0 to 3 is 1.



After the addition of the road from 0 to 2, the length of the shortest path remains 1.

 

Constraints:

3 <= n <= 500
1 <= queries.length <= 500
queries[i].length == 2
0 <= queries[i][0] < queries[i][1] < n
1 < queries[i][1] - queries[i][0]
There are no repeated roads among the queries.
'''
import unittest

from typing import *
from collections import deque, defaultdict


from collections import deque
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for i in range(n-1):
            graph[i].append(i+1)

        res = []

        def bfs():
            q = deque([(0, 1)])
            visited = set()
            while q:
                start, dep = q.popleft()
                for next_target in graph[start]:
                    if next_target == n - 1:
                        return dep
                    if next_target not in visited:
                        visited.add(next_target)
                        q.append((next_target, dep + 1))
            return -1

        for u, v in queries:
            graph[u].append(v)
            res.append(bfs())
        return res



class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((5, [[2,4],[0,2],[0,4]]), [3,2,1]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().shortestDistanceAfterQueries(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
