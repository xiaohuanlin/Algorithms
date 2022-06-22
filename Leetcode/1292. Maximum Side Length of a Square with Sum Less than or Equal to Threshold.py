'''
Given a m x n matrix mat and an integer threshold, return the maximum side-length of a square with a sum less than or equal to threshold or return 0 if there is no such square.

 

Example 1:


Input: mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
Output: 2
Explanation: The maximum side length of square with sum less than 4 is 2 as shown.
Example 2:

Input: mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
Output: 0
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 300
0 <= mat[i][j] <= 104
0 <= threshold <= 105
'''
import unittest

from typing import *

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        row = len(mat)
        col = len(mat[0])
        pre = [[0 for _ in range(col + 1)] for _ in range(row + 1)]
        for i in range(1, row+1):
            for j in range(1, col+1):
                pre[i][j] = pre[i-1][j] + pre[i][j-1] - pre[i-1][j-1] + mat[i-1][j-1]
        
        def get_area(x, y, length):
            return pre[x+length+1][y+length+1] - pre[x+length+1][y] - pre[x][y+length+1] + pre[x][y]

        res = -1
        for i in range(row):
            for j in range(col):
                start = 0
                end = min(row-1-i, col-1-j)
                cur_length = -1
                while start < end:
                    middle = start + (end - start) // 2
                    area = get_area(i, j, middle) 
                    if area > threshold:
                        end = middle - 1
                    elif area == threshold:
                        start = middle
                        cur_length = max(cur_length, middle)
                        break
                    else:
                        cur_length = max(cur_length, middle)
                        start = middle + 1
                if start > cur_length and get_area(i, j, start) <= threshold:
                    cur_length = max(cur_length, start)
                    
                res = max(res, cur_length)
        return res + 1


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], 1), 0),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maxSideLength(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
