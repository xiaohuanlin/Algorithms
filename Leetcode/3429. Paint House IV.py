'''
You are given an even integer n representing the number of houses arranged in a straight line, and a 2D array cost of size n x 3, where cost[i][j] represents the cost of painting house i with color j + 1.

The houses will look beautiful if they satisfy the following conditions:

No two adjacent houses are painted the same color.
Houses equidistant from the ends of the row are not painted the same color. For example, if n = 6, houses at positions (0, 5), (1, 4), and (2, 3) are considered equidistant.
Return the minimum cost to paint the houses such that they look beautiful.

 

Example 1:

Input: n = 4, cost = [[3,5,7],[6,2,9],[4,8,1],[7,3,5]]

Output: 9

Explanation:

The optimal painting sequence is [1, 2, 3, 2] with corresponding costs [3, 2, 1, 3]. This satisfies the following conditions:

No adjacent houses have the same color.
Houses at positions 0 and 3 (equidistant from the ends) are not painted the same color (1 != 2).
Houses at positions 1 and 2 (equidistant from the ends) are not painted the same color (2 != 3).
The minimum cost to paint the houses so that they look beautiful is 3 + 2 + 1 + 3 = 9.

Example 2:

Input: n = 6, cost = [[2,4,6],[5,3,8],[7,1,9],[4,6,2],[3,5,7],[8,2,4]]

Output: 18

Explanation:

The optimal painting sequence is [1, 3, 2, 3, 1, 2] with corresponding costs [2, 8, 1, 2, 3, 2]. This satisfies the following conditions:

No adjacent houses have the same color.
Houses at positions 0 and 5 (equidistant from the ends) are not painted the same color (1 != 2).
Houses at positions 1 and 4 (equidistant from the ends) are not painted the same color (3 != 1).
Houses at positions 2 and 3 (equidistant from the ends) are not painted the same color (2 != 3).
The minimum cost to paint the houses so that they look beautiful is 2 + 8 + 1 + 2 + 3 + 2 = 18.

 

Constraints:

2 <= n <= 105
n is even.
cost.length == n
cost[i].length == 3
0 <= cost[i][j] <= 105
'''
import unittest

from typing import *


class Solution:
    def minCost(self, n: int, cost: List[List[int]]) -> int:
        color = len(cost[0])

        # base condition: size = 2
        prev = [[float('inf') for _ in range(color)] for _ in range(color)]
        for i in range(color):
            for j in range(color):
                if i == j:
                    continue
                prev[i][j] = min(prev[i][j], cost[n // 2 - 1][i] + cost[n // 2][j])
        cur = [[float('inf') for _ in range(color)] for _ in range(color)]

        size = 2
        while size < n:
            for j in range(color):
                for k in range(color):
                    if j == k:
                        continue

                    for x in range(color):
                        for y in range(color):
                            if j == x or k == y or x == y:
                                continue

                            cur[j][k] = min(cur[j][k], prev[x][y])
                    cur[j][k] += cost[n // 2 - size // 2 - 1][j] + cost[n // 2 + size // 2][k]
            prev = cur
            cur = [[float('inf') for _ in range(color)] for _ in range(color)]
            size += 2
        return min(min(x) for x in prev)

        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            # ((4, [[3,5,7],[6,2,9],[4,8,1],[7,3,5]]), 9),
            ((6, [[2,4,6],[5,3,8],[7,1,9],[4,6,2],[3,5,7],[8,2,4]]), 18),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minCost(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
