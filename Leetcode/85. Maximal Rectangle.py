'''
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

 

Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
Example 2:

Input: matrix = [["0"]]
Output: 0
Example 3:

Input: matrix = [["1"]]
Output: 1
 

Constraints:

rows == matrix.length
cols == matrix[i].length
1 <= row, cols <= 200
matrix[i][j] is '0' or '1'.
'''
from typing import *

import unittest
from pprint import pprint


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        # only need one row
        heights = [0 for _ in range(col + 2)]

        res = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == "1":
                    heights[j + 1] += 1
                else:
                    heights[j + 1] = 0
            
            stack = []
            for j in range(col + 2):
                while stack and heights[stack[-1]] > heights[j]:
                    height = heights[stack.pop()]
                    width = j - stack[-1] - 1
                    res = max(res, width * height)
                stack.append(j)
            
        return res
        


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]],), 6),
            (([["0"]],), 0),
            (([["1"]],), 1),
            (([["0","0","1"],["1","1","1"]],), 3),
            (([["0","1","1","0","1"],["1","1","0","1","0"],["0","1","1","1","0"],["1","1","1","1","0"],["1","1","1","1","1"],["0","0","0","0","0"]],), 9),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maximalRectangle(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
