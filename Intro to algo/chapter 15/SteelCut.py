import unittest
import unittest.mock
import io


def memorized_cut_rod(p, n):
    """
    :param p: price_table
    :param n: the length of steel
    :return: the max value
    """
    result = [float('-inf')] * (n + 1)
    return memorized_cut_rod_aux(p, n, result)


def memorized_cut_rod_aux(p, n, result):
    if result[n] >= 0:
        return result[n]
    if n == 0:
        max_sum = 0
    else:
        max_sum = float('-inf')
        for i in range(n):
            max_sum = max(max_sum, p[i] + memorized_cut_rod_aux(p, n - i - 1, result))
    result[n] = max_sum
    return max_sum


def bottom_up_cut_rod(p, n):
    result = [float('-inf')] * (n + 1)
    result[0] = 0
    # update remaining result
    for j in range(1, n+1):
        max_sum = float('-inf')
        for i in range(j):
            max_sum = max(max_sum, p[i] + result[j - i - 1])
        result[j] = max_sum
    return result[n]


def extended_bottom_up_cut_rod(p, n):
    result = [float('-inf')] * (n + 1)
    select = [float('-inf')] * (n + 1)
    result[0] = select[0] = 0
    for j in range(1, n+1):
        max_sum = float('-inf')
        for i in range(j):
            if max_sum < p[i] + result[j - i - 1]:
                max_sum = p[i] + result[j - i - 1]
                # store the length
                select[j] = i + 1
        result[j] = max_sum
    return result, select


def print_cut_rod_solution(p, n):
    result, select = extended_bottom_up_cut_rod(p, n)
    while n > 0:
        print(select[n])
        n = n - select[n]


class TestSolution(unittest.TestCase):

    def test_cut_rod(self):
        examples = (
            ([[1, 5, 8, 9, 10, 17, 17, 20, 24, 30], 8], 22),
        )
        for first, second in examples:
            self.assert_cut_rod(first, second)

    def assert_cut_rod(self, first, second):
        self.assertEqual(memorized_cut_rod(*first), second,
                         msg="first: {}; second: {}".format(first, second))
        self.assertEqual(bottom_up_cut_rod(*first), second,
                         msg="first: {}; second: {}".format(first, second))

    def test_extended_bottom_up_cut_rod(self):
        examples = (
            ([[1, 5, 8, 9, 10, 17, 17, 20, 24, 30], 8], ([0, 1, 5, 8, 10, 13, 17, 18, 22], [0, 1, 2, 3, 2, 2, 6, 1, 2])),
        )
        for first, second in examples:
            self.assert_extended_bottom_up_cut_rod(first, second)

    def assert_extended_bottom_up_cut_rod(self, first, second):
        self.assertEqual(extended_bottom_up_cut_rod(*first), second,
                         msg="first: {}; second: {}".format(first, second))

    def test_print_cut_rod_solution(self):
        examples = (
            ([[1, 5, 8, 9, 10, 17, 17, 20, 24, 30], 8], '2\n6\n'),
        )
        for first, second in examples:
            self.assert_print_cut_rod_solution(first, second)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_print_cut_rod_solution(self, first, second, mock_stdout=None):
        print_cut_rod_solution(*first)
        self.assertEqual(mock_stdout.getvalue(), second)


unittest.main()
