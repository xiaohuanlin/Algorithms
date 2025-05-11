'''
You are given an m x n matrix grid of positive integers. Your task is to determine if it is possible to make either one horizontal or one vertical cut on the grid such that:

Each of the two resulting sections formed by the cut is non-empty.
The sum of the elements in both sections is equal.
Return true if such a partition exists; otherwise return false.

 

Example 1:

Input: grid = [[1,4],[2,3]]

Output: true

Explanation:



A horizontal cut between row 0 and row 1 results in two non-empty sections, each with a sum of 5. Thus, the answer is true.

Example 2:

Input: grid = [[1,3],[2,4]]

Output: false

Explanation:

No horizontal or vertical cut results in two non-empty sections with equal sums. Thus, the answer is false.

 

Constraints:

1 <= m == grid.length <= 105
1 <= n == grid[i].length <= 105
2 <= m * n <= 105
1 <= grid[i][j] <= 105
'''
import unittest

from typing import *


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        rows = []
        rows_total = 0
        for row in grid:
            rows_total += sum(row)
            rows.append(rows_total)
        if rows_total / 2 in rows:
            return True
        
        cols = []
        cols_total = 0
        for j in range(len(grid[0])):
            col_total = 0
            for i in range(len(grid)):
                col_total += grid[i][j]
            cols_total += col_total
            cols.append(cols_total)
        return cols_total / 2 in cols
        

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([[1, 4], [2, 3]],), True),
            (([[1, 3], [2, 4]],), False),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().canPartitionGrid(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

