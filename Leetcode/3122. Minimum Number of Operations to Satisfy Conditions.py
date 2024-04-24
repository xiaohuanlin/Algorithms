'''
You are given a 2D matrix grid of size m x n. In one operation, you can change the value of any cell to any non-negative number. You need to perform some operations such that each cell grid[i][j] is:

Equal to the cell below it, i.e. grid[i][j] == grid[i + 1][j] (if it exists).
Different from the cell to its right, i.e. grid[i][j] != grid[i][j + 1] (if it exists).
Return the minimum number of operations needed.



Example 1:

Input: grid = [[1,0,2],[1,0,2]]

Output: 0

Explanation:



All the cells in the matrix already satisfy the properties.

Example 2:

Input: grid = [[1,1,1],[0,0,0]]

Output: 3

Explanation:



The matrix becomes [[1,0,1],[1,0,1]] which satisfies the properties, by doing these 3 operations:

Change grid[1][0] to 1.
Change grid[0][1] to 0.
Change grid[1][2] to 1.
Example 3:

Input: grid = [[1],[2],[3]]

Output: 2

Explanation:



There is a single column. We can change the value to 1 in each cell using 2 operations.



Constraints:

1 <= n, m <= 1000
0 <= grid[i][j] <= 9
'''
import unittest

from typing import *


class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        dp = [[0 for _ in range(col)] for _ in range(10)]

        for j in range(col):
            # counter numbers
            counters = [0 for _ in range(10)]
            for i in range(row):
                counters[grid[i][j]] += 1

            for i in range(10):
                previous = float('inf') if j != 0 else 0
                current = row - counters[i]
                for k in range(10):
                    # count previous operations
                    if j > 0 and i != k:
                        previous = min(previous, dp[k][j-1])

                dp[i][j] = previous + current

        return min(dp[i][-1] for i in range(10))



class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([[2,6,6,9,8,4,2,6,2,3]],),1),
            (([[0,6,2],[9,0,9],[4,9,6]],),6),
            (([[1,1,1],[0,0,0]],),3),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minimumOperations(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
