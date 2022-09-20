'''
You are given an m x n integer matrix mat and an integer target.

Choose one integer from each row in the matrix such that the absolute difference between target and the sum of the chosen elements is minimized.

Return the minimum absolute difference.

The absolute difference between two numbers a and b is the absolute value of a - b.

 

Example 1:


Input: mat = [[1,2,3],[4,5,6],[7,8,9]], target = 13
Output: 0
Explanation: One possible choice is to:
- Choose 1 from the first row.
- Choose 5 from the second row.
- Choose 7 from the third row.
The sum of the chosen elements is 13, which equals the target, so the absolute difference is 0.
Example 2:


Input: mat = [[1],[2],[3]], target = 100
Output: 94
Explanation: The best possible choice is to:
- Choose 1 from the first row.
- Choose 2 from the second row.
- Choose 3 from the third row.
The sum of the chosen elements is 6, and the absolute difference is 94.
Example 3:


Input: mat = [[1,2,9,8,7]], target = 6
Output: 1
Explanation: The best choice is to choose 7 from the first row.
The absolute difference is 1.
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 70
1 <= mat[i][j] <= 70
1 <= target <= 800
'''

from typing import *

import unittest


from functools import cache
class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        global min_v
        min_v = float('inf')
        
        @cache
        def dfs(i, t):
            global min_v
            if -t > min_v:
                return float('inf')
            
            if i == len(mat):
                return abs(t)
            min_diff = float('inf')
            for j in set(mat[i]):
                min_diff = min(min_diff, dfs(i+1, t-j))
            min_v = min(min_v, min_diff)
            return min_diff
        
        return dfs(0, target)

        
class TestSolution(unittest.TestCase):
    def test_case(self):
        examples = (
            (([[1,2,9,8,7]],6),1),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minimizeTheDifference(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

