'''
You are given a 2D matrix of size m x n, consisting of non-negative integers. You are also given an integer k.

The value of coordinate (a, b) of the matrix is the XOR of all matrix[i][j] where 0 <= i <= a < m and 0 <= j <= b < n (0-indexed).

Find the kth largest value (1-indexed) of all the coordinates of matrix.

 

Example 1:

Input: matrix = [[5,2],[1,6]], k = 1
Output: 7
Explanation: The value of coordinate (0,1) is 5 XOR 2 = 7, which is the largest value.
Example 2:

Input: matrix = [[5,2],[1,6]], k = 2
Output: 5
Explanation: The value of coordinate (0,0) is 5 = 5, which is the 2nd largest value.
Example 3:

Input: matrix = [[5,2],[1,6]], k = 3
Output: 4
Explanation: The value of coordinate (1,0) is 5 XOR 1 = 4, which is the 3rd largest value.
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 1000
0 <= matrix[i][j] <= 106
1 <= k <= m * n
'''

from typing import *
import unittest

from heapq import heappush, heappop
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        pq = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i > 0:
                    matrix[i][j] ^= matrix[i-1][j]
                if j > 0:
                    matrix[i][j] ^= matrix[i][j-1]
                if i > 0 and j > 0:
                    matrix[i][j] ^= matrix[i-1][j-1]
                pq.append(matrix[i][j])
        return sorted(pq, reverse=True)[k-1]


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([[5,2],[1,6]],1),7),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().kthLargestValue(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()