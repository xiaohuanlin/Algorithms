'''
A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbors to the left, right, top, and bottom.

Given a 0-indexed m x n matrix mat where no two adjacent cells are equal, find any peak element mat[i][j] and return the length 2 array [i,j].

You may assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.

You must write an algorithm that runs in O(m log(n)) or O(n log(m)) time.

 

Example 1:



Input: mat = [[1,4],[3,2]]
Output: [0,1]
Explanation: Both 3 and 4 are peak elements so [1,0] and [0,1] are both acceptable answers.
Example 2:



Input: mat = [[10,20,15],[21,30,14],[7,16,32]]
Output: [1,1]
Explanation: Both 30 and 32 are peak elements so [1,1] and [2,2] are both acceptable answers.
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 500
1 <= mat[i][j] <= 105
No two adjacent cells are equal.
'''

from typing import *

import unittest

from collections import defaultdict

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:        
        row = len(mat)
        col = len(mat[0])
        
        def find(start, end):
            if start > end:
                return False
            if start == end:
                for j in range(col):
                    up = mat[start-1][j] if start-1 >= 0 else -1
                    down = mat[start+1][j] if start+1 < row else -1
                    left = mat[start][j-1] if j-1 >= 0 else -1
                    right = mat[start][j+1] if j+1 < col else -1
                    if mat[start][j] > up and mat[start][j] > down and mat[start][j] > left and mat[start][j] > right:
                        return True, [start, j]
                return False, []
            middle = start + (end - start) // 2
            is_true, res = find(start, middle)
            if is_true:
                return True, res
            
            return find(middle+1, end)
        
        is_true, res = find(0, row)
        return res


class TestSolution(unittest.TestCase):
    def test_case(self):
        examples = (
            (([[10,20,15],[21,30,14],[7,16,32]],),[1,1]),
        )

        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().findPeakGrid(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()