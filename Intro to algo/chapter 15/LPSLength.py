import unittest
from pprint import pprint


def lps_length(s):
    s = list(s)
    length = len(s)
    result = [[float('-inf')] * (length+1) for _ in range(length+1)]
    select = [[None] * (length+1) for _ in range(length+1)]

    # initial data
    for i in range(length+1):
        result[i][0] = 0
    for j in range(length+1):
        result[length][j] = 0
    for k in range(length):
        result[k][k+1] = 1

    lps_length_pro(s, result, select, 0, length)

    lps_result = []
    get_lps(select, s, 0, length, lps_result)
    return ''.join(lps_result)


def lps_length_pro(s, result, select, start, end):
    if result[start][end] >= 0:
        return result[start][end]
    # print(start, end)
    if s[start] == s[end-1]:
        max_value = lps_length_pro(s, result, select, start+1, end-1) + 2
        select[start][end] = 'left_bottom'
    else:
        # in this case, we either reduce the end value or increase start value
        # 1. fix the start value
        fix_start_value = lps_length_pro(s, result, select, start, end-1)

        # 2. fix the end value
        fix_end_value = lps_length_pro(s, result, select, start+1, end)

        if fix_start_value > fix_end_value:
            max_value = fix_start_value
            select[start][end] = 'left'
        else:
            max_value = fix_end_value
            select[start][end] = 'bottom'

    result[start][end] = max_value
    return max_value


def get_lps(select, s, i, j, result: list):
    """
    :param select: select table
    :param s: list s
    :param i: row index
    :param j: column index
    :param result: the lps list
    :return: none
    """
    if i >= j:
        return
    if select[i][j] is None:
        # only one word
        result.append(s[i])
    elif select[i][j] == 'left_bottom':
        result.append(s[i])
        get_lps(select, s, i+1, j-1, result)
        result.append(s[j-1])
    elif select[i][j] == 'bottom':
        get_lps(select, s, i+1, j, result)
    else:
        get_lps(select, s, i, j-1, result)


class TestSolution(unittest.TestCase):

    def test_lps_length(self):
        examples = (
            ('character', 'carac'),
            ('civic', 'civic')
        )
        for first, second in examples:
            self.assert_lps_length(first, second)

    def assert_lps_length(self, first, second):
        self.assertEqual(lps_length(first), second,
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
