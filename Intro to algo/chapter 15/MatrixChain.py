import unittest
import unittest.mock
import io
from collections import MutableSequence


def matrix_chain_order(p):
    """
    :param p: the list of column in matrices, which means the first element is the row of fist matrix
    :return:
    """
    n = len(p) - 1
    result = [[float('+inf')] * n for _ in range(n)]
    select = [[float('+inf')] * n for _ in range(n)]
    for i in range(n):
        result[i][i] = select[i][i] = 0

    for length in range(2, n+1):
        # looking for all result in this length
        for start in range(n - length + 1):
            end = start + length - 1
            result[start][end] = float('+inf')
            for point in range(start, end):
                # after we decide the start and end point, we should choose a break point and calculate value
                min_mul = result[start][point] + result[point+1][end] + p[start] * p[point+1] * p[end+1]
                if min_mul < result[start][end]:
                    result[start][end] = min_mul
                    select[start][end] = point + 1

    return result, select


def print_optimal_parens(select, start, end):
    if start == end:
        print("A[{}]".format(start), end='')
    else:
        print("(", end='')
        print_optimal_parens(select, start, select[start-1][end-1])
        print_optimal_parens(select, select[start-1][end-1] + 1, end)
        print(")", end='')


class TestSolution(unittest.TestCase):

    def test_matrix_chain_order(self):
        examples = (
            ([30, 35, 15, 5, 10, 20, 25],
             ([[0, 15750, 7875, 9375, 11875, 15125],
              [float('+inf'), 0, 2625, 4375, 7125, 10500],
              [float('+inf'), float('+inf'), 0, 750, 2500, 5375],
              [float('+inf'), float('+inf'), float('+inf'), 0, 1000, 3500],
              [float('+inf'), float('+inf'), float('+inf'), float('+inf'), 0, 5000],
              [float('+inf'), float('+inf'), float('+inf'), float('+inf'), float('+inf'), 0]],
             [[0, 1, 1, 3, 3, 3],
              [float('+inf'), 0, 2, 3, 3, 3],
              [float('+inf'), float('+inf'), 0, 3, 3, 3],
              [float('+inf'), float('+inf'), float('+inf'), 0, 4, 5],
              [float('+inf'), float('+inf'), float('+inf'), float('+inf'), 0, 5],
              [float('+inf'), float('+inf'), float('+inf'), float('+inf'), float('+inf'), 0]])
             ),
        )
        for first, second in examples:
            self.assert_matrix_chain_order(first, second)

    def assert_matrix_chain_order(self, first, second):
        self.assertEqual(matrix_chain_order(first), second,
                         msg="first: {}; second: {}".format(first, second))

    def test_print_optimal_parens(self):
        examples = (
            ([30, 35, 15, 5, 10, 20, 25], '((A[1](A[2]A[3]))((A[4]A[5])A[6]))'),
        )
        for first, second in examples:
            self.assert_print_optimal_parens(first, second)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_print_optimal_parens(self, first, second, mock_stdout=None):
        print_optimal_parens(matrix_chain_order(first)[1], 1, len(first)-1)
        self.assertEqual(mock_stdout.getvalue(), second)


unittest.main()
