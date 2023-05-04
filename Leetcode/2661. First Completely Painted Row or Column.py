'''
You are given a 0-indexed integer array arr, and an m x n integer matrix mat. arr and mat both contain all the integers in the range [1, m * n].

Go through each index i in arr starting from index 0 and paint the cell in mat containing the integer arr[i].

Return the smallest index i at which either a row or a column will be completely painted in mat.

 

Example 1:

image explanation for example 1
Input: arr = [1,3,4,2], mat = [[1,4],[2,3]]
Output: 2
Explanation: The moves are shown in order, and both the first row and second column of the matrix become fully painted at arr[2].
Example 2:

image explanation for example 2
Input: arr = [2,8,7,4,1,3,5,6,9], mat = [[3,2,5],[1,4,6],[8,7,9]]
Output: 3
Explanation: The second column becomes fully painted at arr[3].
 

Constraints:

m == mat.length
n = mat[i].length
arr.length == m * n
1 <= m, n <= 105
1 <= m * n <= 105
1 <= arr[i], mat[r][c] <= m * n
All the integers of arr are unique.
All the integers of mat are unique.
'''

from typing import *

import unittest


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        maps = [() for _ in range(len(arr))]
        for i in range(m):
            for j in range(n):
                maps[mat[i][j]-1] = (i, j)

        count_row = [0 for _ in range(m)]
        count_col = [0 for _ in range(n)]
        for i in range(len(arr)):
            row, col = maps[arr[i]-1]
            count_row[row] += 1
            count_col[col] += 1
            if count_row[row] == n or count_col[col] == m:
                return i
        return -1




class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
          (([1,3,4,2], [[1,4],[2,3]]),2),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().firstCompleteIndex(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
