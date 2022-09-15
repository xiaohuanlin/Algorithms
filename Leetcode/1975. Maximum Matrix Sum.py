'''
You are given an n x n integer matrix. You can do the following operation any number of times:

Choose any two adjacent elements of matrix and multiply each of them by -1.
Two elements are considered adjacent if and only if they share a border.

Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.

 

Example 1:


Input: matrix = [[1,-1],[-1,1]]
Output: 4
Explanation: We can follow the following steps to reach sum equals 4:
- Multiply the 2 elements in the first row by -1.
- Multiply the 2 elements in the first column by -1.
Example 2:


Input: matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
Output: 16
Explanation: We can follow the following step to reach sum equals 16:
- Multiply the 2 last elements in the second row by -1.
 

Constraints:

n == matrix.length == matrix[i].length
2 <= n <= 250
-105 <= matrix[i][j] <= 105
'''

from typing import *

import unittest


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        count = 0
        min_v = float('inf')
        
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                total += abs(matrix[i][j])
                count += matrix[i][j] < 0
                min_v = min(min_v, abs(matrix[i][j]))
                
        return total if count % 2 == 0 else total - 2 * min_v
        
class TestSolution(unittest.TestCase):
    def test_case(self):
        examples = (
            (([[1,-1],[-1,1]],),4),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maxMatrixSum(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

