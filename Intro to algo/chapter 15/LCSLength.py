import unittest
import unittest.mock
import io


def lcs_length(x, y):
    """
    :param x: list
    :param y: list
    :return: result and select
    """
    x, y = list(x), list(y)
    x_len = len(x)
    y_len = len(y)
    result = [[float('-inf')] * (y_len+1) for _ in range(x_len+1)]
    select = [[None] * (y_len+1) for _ in range(x_len+1)]

    # initial data, extend the raw data to make it calculate more easier
    for i in range(x_len+1):
        result[i][0] = 0
    for j in range(y_len+1):
        result[0][j] = 0

    # so, i and j will start from 1
    for i in range(1, x_len+1):
        for j in range(1, y_len+1):
            # we should transfer i and j to index of list
            # consider that we only need the three surrender value, it is possible to cut the
            # table into 2 row, and store values. like i --> i % 2.
            if x[i-1] == y[j-1]:
                result[i][j] = result[i-1][j-1] + 1
                select[i][j] = "left_top"
            elif result[i-1][j] >= result[i][j-1]:
                result[i][j] = result[i-1][j]
                select[i][j] = "top"
            else:
                result[i][j] = result[i][j-1]
                select[i][j] = "left"
    return result, select


def memorized_lcs_length(x, y):
    """
    :param x: list
    :param y: list
    :return: result and select
    """
    x, y = list(x), list(y)
    x_len = len(x)
    y_len = len(y)
    result = [[float('-inf')] * (y_len+1) for _ in range(x_len+1)]
    select = [[None] * (y_len+1) for _ in range(x_len+1)]

    # initial data, extend the raw data to make it calculate more easier
    for i in range(x_len+1):
        result[i][0] = 0
    for j in range(y_len+1):
        result[0][j] = 0
    memorized_lcs_length_pro(result, select, x, y, x_len, y_len)
    return result, select


def memorized_lcs_length_pro(result, select, x, y, i, j):
    if result[i][j] >= 0:
        return result[i][j]
    if x[i - 1] == y[j - 1]:
        result[i][j] = memorized_lcs_length_pro(result, select, x, y, i - 1, j - 1) + 1
        select[i][j] = "left_top"

    else:
        top_value = memorized_lcs_length_pro(result, select, x, y, i - 1, j)
        left_value = memorized_lcs_length_pro(result, select, x, y, i, j - 1)
        if top_value >= left_value:
            result[i][j] = top_value
            select[i][j] = "top"
        else:
            result[i][j] = left_value
            select[i][j] = "left"
    return result[i][j]


def print_lcs(select, x, i, j):
    """
    :param select: select table
    :param x: list x
    :param i: row index
    :param j: column index
    :return: none
    """
    if i == 0 or j == 0:
        return
    if select[i][j] == 'left_top':
        print_lcs(select, x, i-1, j-1)
        print(x[i-1], end='')
    elif select[i][j] == 'top':
        print_lcs(select, x, i-1, j)
    else:
        print_lcs(select, x, i, j-1)


class TestSolution(unittest.TestCase):

    def test_lcs_length(self):
        examples = (
            (["ABCBDAB", "BDCABA"],
             ([[0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 1, 1],
               [0, 1, 1, 1, 1, 2, 2],
               [0, 1, 1, 2, 2, 2, 2],
               [0, 1, 1, 2, 2, 3, 3],
               [0, 1, 2, 2, 2, 3, 3],
               [0, 1, 2, 2, 3, 3, 4],
               [0, 1, 2, 2, 3, 4, 4]],
              [[None, None, None, None, None, None, None],
               [None, 'top', 'top', 'top', 'left_top', 'left', 'left_top'],
               [None, 'left_top', 'left', 'left', 'top', 'left_top', 'left'],
               [None, 'top', 'top', 'left_top', 'left', 'top', 'top'],
               [None, 'left_top', 'top', 'top', 'top', 'left_top', 'left'],
               [None, 'top', 'left_top', 'top', 'top', 'top', 'top'],
               [None, 'top', 'top', 'top', 'left_top', 'top', 'left_top'],
               [None, 'left_top', 'top', 'top', 'top', 'left_top', 'top']]
              )),
        )
        for first, second in examples:
            self.assert_lcs_length(first, second)

    def assert_lcs_length(self, first, second):
        self.assertEqual(lcs_length(*first), second,
                         msg="first: {}; second: {}".format(first, second))

    def test_memorized_lcs_length(self):
        examples = (
            (["ABCBDAB", "BDCABA"],
             ([[0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, float('-inf'), float('-inf')],
               [0, 1, 1, 1, 1, float('-inf'), float('-inf')],
               [0, 1, 1, 2, 2, float('-inf'), float('-inf')],
               [0, 1, 1, 2, 2, 3, float('-inf')],
               [0, float('-inf'), 2, 2, 2, 3, float('-inf')],
               [0, float('-inf'), float('-inf'), float('-inf'), 3, float('-inf'), 4],
               [0, float('-inf'), float('-inf'), float('-inf'), float('-inf'), 4, 4]],
              [[None, None, None, None, None, None, None],
               [None, 'top', 'top', 'top', 'left_top', None, None],
               [None, 'left_top', 'left', 'left', 'top', None, None],
               [None, 'top', 'top', 'left_top', 'left', None, None],
               [None, 'left_top', 'top', 'top', 'top', 'left_top', None],
               [None, None, 'left_top', 'top', 'top', 'top', None],
               [None, None, None, None, 'left_top', None, 'left_top'],
               [None, None, None, None, None, 'left_top', 'top']]
              )),
        )
        for first, second in examples:
            self.assert_memorized_lcs_length(first, second)

    def assert_memorized_lcs_length(self, first, second):
        self.assertEqual(memorized_lcs_length(*first), second,
                         msg="first: {}; second: {}".format(first, second))

    def test_print_lcs(self):
        examples = (
            (["ABCBDAB", "BDCABA"], 'BCBA'),
            (["10010101", "010110110"], '100110'),
        )
        for first, second in examples:
            self.assert_print_lcs(first, second)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_print_lcs(self, first, second, mock_stdout=None):
        print_lcs(lcs_length(*first)[1], first[0], len(first[0]), len(first[1]))
        self.assertEqual(mock_stdout.getvalue(), second)


unittest.main()
