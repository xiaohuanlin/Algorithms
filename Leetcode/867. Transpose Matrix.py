'''

Given a matrix A, return the transpose of A.

The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.



Example 1:

Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
Example 2:

Input: [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]


Note:

1 <= A.length <= 1000
1 <= A[0].length <= 1000

'''
import unittest


class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        # row = len(A)
        # col = len(A[0])
        # B = [[0] * row for _ in range(col)]
        # for i in range(row):
        #     for j in range(col):
        #         B[j][i] = A[i][j]
        # return B
        # ----------------------------------
        return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ([[1,2,3],[4,5,6],[7,8,9]], [[1,4,7],[2,5,8],[3,6,9]]),
            ([[1,2,3],[4,5,6]], [[1,4],[2,5],[3,6]])
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().transpose(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
