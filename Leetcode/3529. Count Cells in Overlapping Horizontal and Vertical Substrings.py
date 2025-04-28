'''
You are given an m x n matrix grid consisting of characters and a string pattern.

A horizontal substring is a contiguous sequence of characters read from left to right. If the end of a row is reached before the substring is complete, it wraps to the first column of the next row and continues as needed. You do not wrap from the bottom row back to the top.

A vertical substring is a contiguous sequence of characters read from top to bottom. If the bottom of a column is reached before the substring is complete, it wraps to the first row of the next column and continues as needed. You do not wrap from the last column back to the first.

Count the number of cells in the matrix that satisfy the following condition:

The cell must be part of at least one horizontal substring and at least one vertical substring, where both substrings are equal to the given pattern.
Return the count of these cells.

 

Example 1:


Input: grid = [["a","a","c","c"],["b","b","b","c"],["a","a","b","a"],["c","a","a","c"],["a","a","b","a"]], pattern = "abaca"

Output: 1

Explanation:

The pattern "abaca" appears once as a horizontal substring (colored blue) and once as a vertical substring (colored red), intersecting at one cell (colored purple).

Example 2:


Input: grid = [["c","a","a","a"],["a","a","b","a"],["b","b","a","a"],["a","a","b","a"]], pattern = "aba"

Output: 4

Explanation:

The cells colored above are all part of at least one horizontal and one vertical substring matching the pattern "aba".

Example 3:

Input: grid = [["a"]], pattern = "a"

Output: 1

 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 1000
1 <= m * n <= 105
1 <= pattern.length <= m * n
grid and pattern consist of only lowercase English letters.
'''
import unittest

from typing import *



class Solution:
    def countCells(self, grid: List[List[str]], pattern: str) -> int:
        row_string = []
        col_string = []
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                row_string.append((grid[i][j], (i, j)))
        for i in range(col):
            for j in range(row):
                col_string.append((grid[j][i], (j, i)))
        
        all_valid = set()
        next = [0 for _ in range(len(pattern))]
        j = 0
        for i in range(1, len(pattern)):
            while j > 0 and pattern[i] != pattern[j]:
                j = next[j-1]
            if pattern[i] == pattern[j]:
                j += 1
            next[i] = j

        def kmp(string):
            j = 0
            all_valid = set()
            pre_e = 0
            for i in range(len(string)):
                while j > 0 and string[i][0] != pattern[j]:
                    j = next[j-1]
                if string[i][0] == pattern[j]:
                    j += 1
                if j == len(pattern):
                    s, e = i-j+1, i+1
                    s = pre_e if s <= pre_e else s
                    pre_e = e
                    for k in range(s, e):
                        all_valid.add(string[k][1])
                    j = next[j-1]
            return all_valid

        return len(kmp(row_string) & kmp(col_string))



class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([
                ["a", "a", "c", "c"],
                ["b", "b", "b", "c"],
                ["a", "a", "b", "a"],
                ["c", "a", "a", "c"],
                ["a", "a", "b", "a"]
            ], "abaca"), 1),
            (([
                ["c", "a", "a", "a"],
                ["a", "a", "b", "a"],
                ["b", "b", "a", "a"],
                ["a", "a", "b", "a"]
            ], "aba"), 4)
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().countCells(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

