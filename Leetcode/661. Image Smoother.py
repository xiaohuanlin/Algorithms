'''

Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.

Example 1:
Input:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
Explanation:
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
Note:
The value in the given matrix is in the range of [0, 255].
The length and width of the given matrix are in the range of [1, 150].

'''
import unittest


class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(M)
        col = len(M[0])
        result = [[0 for _ in range(col)] for _ in range(row)]

        for i in range(row):
            for j in range(col):
                self.value = 0
                self.length = 0
                for m, n in (
                    (i - 1, j - 1),
                    (i - 1, j),
                    (i - 1, j + 1),
                    (i, j - 1),
                    (i, j),
                    (i, j + 1),
                    (i + 1, j - 1),
                    (i + 1, j),
                    (i + 1, j + 1),
                ):
                    self.get_value(M, m, n)
                result[i][j] = int(self.value/self.length)
                # print(result)
        return result

    def get_value(self, M, i, j):
        try:
            value = M[i][j]
            length = 1
        except IndexError:
            value = 0
            length = 0
        if i < 0 or j < 0:
            value = 0
            length = 0
        self.value += value
        self.length += length


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ([[1, 1, 1],
              [1, 0, 1],
              [1, 1, 1]],
             [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
             ),
            ([[1, 1, 1],
              [1, 1, 1],
              [1, 0, 1]],
             [[1, 1, 1],
              [0, 0, 0],
              [0, 0, 0]]
             ),
            (
                [[2, 3, 4], [5, 6, 7], [8, 9, 10], [11, 12, 13], [14, 15, 16]],
                [[4, 4, 5], [5, 6, 6], [8, 9, 9], [11, 12, 12], [13, 13, 14]])
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().imageSmoother(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
