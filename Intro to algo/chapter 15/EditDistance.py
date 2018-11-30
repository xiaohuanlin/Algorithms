import unittest
import unittest.mock
import io
from pprint import pprint
from collections import namedtuple

Cost = namedtuple('Cost', ['copy', 'replace', 'delete', 'insert', 'twiddle', 'kill'])


def edit_distance(source_string, target_string, cost_list: Cost):
    # copy+replace < delete+insert

    row = len(source_string)
    col = len(target_string)
    result = [[float('+inf')] * (col+1) for _ in range(row+1)]
    select = [[None] * (col+1) for _ in range(row+1)]

    result[0][0] = 0
    # the initial data is very important
    for i in range(1, row+1):
        result[i][0] = i * cost_list.delete
        select[i][0] = 'delete'
    for j in range(1, col+1):
        result[0][j] = j * cost_list.insert
        select[0][j] = 'insert'

    for i in range(1, row + 1):
        for j in range(1, col + 1):
            result[i][j] = float('+inf')

            if source_string[i-1] == target_string[j-1]:
                copy_value = result[i-1][j-1] + cost_list.copy
                if result[i][j] > copy_value:
                    result[i][j] = copy_value
                    select[i][j] = 'copy'
            else:
                replace_value = result[i-1][j-1] + cost_list.replace
                if result[i][j] > replace_value:
                    result[i][j] = replace_value
                    select[i][j] = 'replace'

            delete_value = result[i-1][j] + cost_list.delete
            if result[i][j] > delete_value:
                result[i][j] = delete_value
                select[i][j] = 'delete'

            insert_value = result[i][j-1] + cost_list.insert
            if result[i][j] > insert_value:
                result[i][j] = insert_value
                select[i][j] = 'insert'

            # make sure there are at least two element
            if i >= 2 and j >= 2 and source_string[i-2:i] == target_string[j-1:j-3:-1]:
                twiddle_value = result[i-2][j-2] + cost_list.twiddle
                if result[i][j] > twiddle_value:
                    result[i][j] = twiddle_value
                    select[i][j] = 'twiddle'

            for m in range(row):
                kill_value = result[m][j] + cost_list.kill
                if result[i][j] > kill_value:
                    result[i][j] = kill_value
                    select[i][j] = 'kill->{}'.format(m)
    # print_list(result)
    # print_list(select)

    return result[row][col]


class TestSolution(unittest.TestCase):

    def test_edit_distance(self):
        examples = (
            (('algorithm', 'altruistic', Cost(2, 3, 3, 4, 1, 1)),
             26),
        )
        for first, second in examples:
            self.assert_edit_distance(first, second)

    def assert_edit_distance(self, first, second):
        self.assertEqual(edit_distance(*first), second,
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
