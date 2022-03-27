'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

 

Example 1:


Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
Example 2:

Input: n = 1
Output: 1
 

Constraints:

1 <= n <= 9
'''
from typing import *

import unittest
from pprint import pprint


class Solution:
    res = 0
    
    def totalNQueens(self, n: int) -> int:
        
        def valid(selected, row, col):
            for r, c in enumerate(selected):
                if abs(r - row) == abs(c - col) or col == c:
                    return False
            return True
        
        def getResult(selected):
            row = len(selected)
            if row == n:
                self.res += 1
                return
            
            for c in range(n):
                if not valid(selected, row, c):
                    continue
                selected.append(c)
                getResult(selected)
                selected.pop()
                
        getResult([])
        return self.res

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((4,), 2),
            ((1,), 1),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().totalNQueens(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
