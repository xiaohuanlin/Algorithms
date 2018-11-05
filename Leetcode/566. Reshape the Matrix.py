'''

In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:
Input:
nums =
[[1,2],
 [3,4]]
r = 1, c = 4
Output:
[[1,2,3,4]]
Explanation:
The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.
Example 2:
Input:
nums =
[[1,2],
 [3,4]]
r = 2, c = 4
Output:
[[1,2],
 [3,4]]
Explanation:
There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.
Note:
The height and width of the given matrix is in range [1, 100].
The given r and c are all positive.

'''
import unittest


class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        flat_list = []
        for row in nums:
            flat_list.extend(row)
        if r*c != len(flat_list):
            return nums

        return [flat_list[i * c: (i + 1) * c] for i in range(r)]



class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([[1,2], [3,4]], 1, 4), [[1,2,3,4]]),
            (([[1,2], [3,4]], 2, 4), [[1,2], [3,4]]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().matrixReshape(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
