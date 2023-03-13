'''
You are given a 2D integer grid of size m x n and an integer x. In one operation, you can add x to or subtract x from any element in the grid.

A uni-value grid is a grid where all the elements of it are equal.

Return the minimum number of operations to make the grid uni-value. If it is not possible, return -1.



Example 1:


Input: grid = [[2,4],[6,8]], x = 2
Output: 4
Explanation: We can make every element equal to 4 by doing the following:
- Add x to 2 once.
- Subtract x from 6 once.
- Subtract x from 8 twice.
A total of 4 operations were used.
Example 2:


Input: grid = [[1,5],[2,3]], x = 1
Output: 5
Explanation: We can make every element equal to 3.
Example 3:


Input: grid = [[1,2],[3,4]], x = 2
Output: -1
Explanation: It is impossible to make every element equal.


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 105
1 <= m * n <= 105
1 <= x, grid[i][j] <= 104
'''
import unittest

from typing import *
from bisect import insort

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        remind = -1
        res = []
        for row in grid:
            for n in row:
                if remind == -1:
                    remind = n % x
                if n % x != remind:
                    return -1
                real_value = (n - remind) // x
                insort(res, real_value)

        middle = res[len(res) // 2] if len(res) % 2 == 1 else (res[len(res) // 2] + res[len(res) // 2 - 1]) // 2
        total = 0
        for n in res:
            total += abs(n - middle)
        return total


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([[596,904,960,232,120,932,176],[372,792,288,848,960,960,764],[652,92,904,120,680,904,120],[372,960,92,680,876,624,904],[176,652,64,344,316,764,316],[820,624,848,596,960,960,372],[708,120,456,92,484,932,540]], 28), 473),
            (([[529,529,989],[989,529,345],[989,805,69]], 92), 25),
            (([[1,5],[2,3]], 1), 5),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minOperations(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
