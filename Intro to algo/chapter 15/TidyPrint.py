import unittest
import unittest.mock
import io
from pprint import pprint


def tidy_print(l_list, max_l_per_line):
    n = len(l_list)
    len_list = [len(s) for s in l_list]
    result = [[float('-inf')] * n for _ in range(n)]
    select = [[None] * n for _ in range(n)]

    for length in range(1, n+1):
        # because we need initial data, so length will start from 1
        for i in range(n - length + 1):
            j = i + length - 1
            space = max_l_per_line - sum(len_list[i: j+1]) - (j - i)
            if space > 0:
                # only if the space large than 0, we can use this data to initial data
                result[i][j] = space ** 3
                select[i][j] = j + 1
            else:
                result[i][j] = float('+inf')

            for k in range(i, j):
                value = result[i][k] + result[k + 1][j]
                if value < result[i][j]:
                    result[i][j] = value
                    select[i][j] = k + 1

    print_tidy_print(select, l_list, max_l_per_line, 1, n)
    return result[0][ n-1]


def print_tidy_print(select, l_list, max_l_per_line, start, end):
    spe = '{:*<' + str(max_l_per_line) + '}'
    if start == end:
        print(spe.format(l_list[start-1]), end='')
    else:
        if select[start-1][end-1] == end:
            # In this case, we should print all all str into a list, otherwise will occur error
            string = ' '.join(l_list[start-1: end])
            print(spe.format(string), end='')
        else:
            print_tidy_print(select, l_list, max_l_per_line, start, select[start-1][end-1])
            print("\n", end='')
            print_tidy_print(select, l_list, max_l_per_line, select[start-1][end-1] + 1, end)


class TestSolution(unittest.TestCase):

    def test_tidy_print(self):
        examples = (
            ((('hi', 'ha', 'who', 'are', 'you', 'ready'),
             7),
             (208,
              'hi ha**\nwho****\nare****\nyou****\nready**')
             ),
        )
        for first, second in examples:
            self.assert_tidy_print(first, second)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_tidy_print(self, first, second, mock_stdout=None):
        self.assertEqual(tidy_print(*first), second[0],
                         msg="first: {}; second: {}".format(first, second))
        self.assertEqual(mock_stdout.getvalue(), second[1])


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
