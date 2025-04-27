'''
You are given an integer n representing the number of nodes in a graph, labeled from 0 to n - 1.

You are also given an integer array nums of length n sorted in non-decreasing order, and an integer maxDiff.

An undirected edge exists between nodes i and j if the absolute difference between nums[i] and nums[j] is at most maxDiff (i.e., |nums[i] - nums[j]| <= maxDiff).

You are also given a 2D integer array queries. For each queries[i] = [ui, vi], determine whether there exists a path between nodes ui and vi.

Return a boolean array answer, where answer[i] is true if there exists a path between ui and vi in the ith query and false otherwise.

 

Example 1:

Input: n = 2, nums = [1,3], maxDiff = 1, queries = [[0,0],[0,1]]

Output: [true,false]

Explanation:

Query [0,0]: Node 0 has a trivial path to itself.
Query [0,1]: There is no edge between Node 0 and Node 1 because |nums[0] - nums[1]| = |1 - 3| = 2, which is greater than maxDiff.
Thus, the final answer after processing all the queries is [true, false].
Example 2:

Input: n = 4, nums = [2,5,6,8], maxDiff = 2, queries = [[0,1],[0,2],[1,3],[2,3]]

Output: [false,false,true,true]

Explanation:

The resulting graph is:



Query [0,1]: There is no edge between Node 0 and Node 1 because |nums[0] - nums[1]| = |2 - 5| = 3, which is greater than maxDiff.
Query [0,2]: There is no edge between Node 0 and Node 2 because |nums[0] - nums[2]| = |2 - 6| = 4, which is greater than maxDiff.
Query [1,3]: There is a path between Node 1 and Node 3 through Node 2 since |nums[1] - nums[2]| = |5 - 6| = 1 and |nums[2] - nums[3]| = |6 - 8| = 2, both of which are within maxDiff.
Query [2,3]: There is an edge between Node 2 and Node 3 because |nums[2] - nums[3]| = |6 - 8| = 2, which is equal to maxDiff.
Thus, the final answer after processing all the queries is [false, false, true, true].
 

Constraints:

1 <= n == nums.length <= 105
0 <= nums[i] <= 105
nums is sorted in non-decreasing order.
0 <= maxDiff <= 105
1 <= queries.length <= 105
queries[i] == [ui, vi]
0 <= ui, vi < n
'''
import unittest

from typing import *


class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, u):
        root = u
        while self.root[root] != root:
            root = self.root[root]
        
        while self.root[u] != root:
            p = self.root[u]
            self.root[u] = root
            u = p
        return root
    
    def union(self, u, v):
        r_u = self.find(u)
        r_v = self.find(v)
        if self.size[r_u] > self.size[r_v]:
            self.root[r_u] = r_v
            self.size[r_v] += self.size[r_u]
        else:
            self.root[r_v] = r_u
            self.size[r_u] += self.size[r_v]

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        union = UnionFind(n)
        for i in range(len(nums)-1):
            if abs(nums[i] - nums[i+1]) <= maxDiff:
                union.union(i, i+1)
        res = []
        for u, v in queries:
            res.append(union.find(u) == union.find(v))
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((2, [1, 3], 1, [[0, 0], [0, 1]]), [True, False]),
            ((4, [2, 5, 6, 8], 2, [[0, 1], [0, 2], [1, 3], [2, 3]]), [False, False, True, True])
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().pathExistenceQueries(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

