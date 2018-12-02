import unittest
import unittest.mock
import io
from pprint import pprint


def string_split(string_length, L: list):
    """
    :param string_length: the length of string
    :param L: the list of break point index
    :return]: result and select
    """
    # extend L
    L.insert(0, 1)
    L.append(string_length)

    n = len(L)
    result = [[float('-inf')] * n for _ in range(n)]
    select = [[None] * n for _ in range(n)]

    # initial data: the cost will become 0 when the delta of points is 1
    for i in range(n-1):
        result[i][i+1] = 0

    for length in range(3, n+1):
        for start in range(n - length + 1):
            end = length + start - 1
            result[start][end] = float('+inf')
            for point in range(start + 1, end):
                # point should start from 'start+1' because of base condition
                min_value = result[start][point] + result[point][end] + L[end] - L[start] + 1
                if min_value < result[start][end]:
                    result[start][end] = min_value
                    select[start][end] = point

    split_list = []
    get_split_list(select, split_list, L, 0, n-1)

    return result[0][n-1], split_list[1:][::-1]


def get_split_list(select, split_list, L, start, end):
    if start == end - 1:
        split_list.append(L[start])
    else:
        get_split_list(select, split_list, L, start, select[start][end])
        get_split_list(select, split_list, L, select[start][end], end)


class TestSolution(unittest.TestCase):

    def test_string_split(self):
        examples = (
            ((20, [2, 8, 10]),
             (38, [10, 8, 2])
             ),
        )
        for first, second in examples:
            self.assert_string_split(first, second)

    def assert_string_split(self, first, second):
        self.assertEqual(string_split(*first), second,
                         msg="first: {}; second: {}".format(first, second))


def print_list(l):
    from copy import deepcopy
    c_l = deepcopy(l)
    max_length = max(len(str(data)) for row in c_l for data in row)
    spe = '{:<' + str(max_length) + '}'
    for row in c_l:
        for i in range(len(row)):
            if row[i] is None:
                row[i] = 'None'
            row[i] = spe.format(row[i])
    pprint(c_l, width=(max_length + 5) * len(c_l[0]))


unittest.main()
