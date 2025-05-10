'''
You are given two integers, n and k, along with two 2D integer arrays, stayScore and travelScore.

A tourist is visiting a country with n cities, where each city is directly connected to every other city. The tourist's journey consists of exactly k 0-indexed days, and they can choose any city as their starting point.

Each day, the tourist has two choices:

Stay in the current city: If the tourist stays in their current city curr during day i, they will earn stayScore[i][curr] points.
Move to another city: If the tourist moves from their current city curr to city dest, they will earn travelScore[curr][dest] points.
Return the maximum possible points the tourist can earn.

 

Example 1:

Input: n = 2, k = 1, stayScore = [[2,3]], travelScore = [[0,2],[1,0]]

Output: 3

Explanation:

The tourist earns the maximum number of points by starting in city 1 and staying in that city.

Example 2:

Input: n = 3, k = 2, stayScore = [[3,4,2],[2,1,2]], travelScore = [[0,2,1],[2,0,4],[3,2,0]]

Output: 8

Explanation:

The tourist earns the maximum number of points by starting in city 1, staying in that city on day 0, and traveling to city 2 on day 1.

 

Constraints:

1 <= n <= 200
1 <= k <= 200
n == travelScore.length == travelScore[i].length == stayScore[i].length
k == stayScore.length
1 <= stayScore[i][j] <= 100
0 <= travelScore[i][j] <= 100
travelScore[i][i] == 0
'''
import unittest

from typing import *


class Solution:
    def maxScore(self, n: int, k: int, stayScore: List[List[int]], travelScore: List[List[int]]) -> int:
        dp = [[0 for _ in range(n)] for _ in range(k+1)]
        for i in range(1, k+1):
            for j in range(n):
                dp[i][j] = dp[i-1][j] + stayScore[i-1][j]
                for z in range(n):
                    if z == j:
                        continue
                    dp[i][j] = max(dp[i][j], dp[i-1][z] + travelScore[z][j])
        return max(dp[-1])


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((2, 1, [[2,3]], [[0,2],[1,0]]), 3),
            ((3, 2, [[3,4,2],[2,1,2]], [[0,2,1],[2,0,4],[3,2,0]]), 8),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maxScore(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

