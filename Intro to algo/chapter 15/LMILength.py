'''
this is the longest monotonically increasing sequence
'''

import unittest


def lmi_length(x):
    """
    :param x: list
    :return: result and select
    """
    x_len = len(x)
    result = [None] * (x_len + 1)
    select = []

    # initial data
    result[0] = float('-inf'), 0

    lmi_length_pro(result, select, x, x_len)

    return result, select


def lmi_length_pro(result, select, x, i):

    if result[i] is not None:
        return result[i]

    max_value, length = lmi_length_pro(result, select, x, i - 1)

    if x[i-1] >= max_value:
        result[i] = x[i-1], length + 1
        select.append(x[i-1])
    else:
        result[i] = result[i-1]

    return result[i]


class TestSolution(unittest.TestCase):

    def test_lcs_length(self):
        examples = (
            ([1, 5, 2, 6, 1, 7, 5, 9, 7, 2, 5],
             ([(float('-inf'), 0),
              (1, 1),
              (5, 2),
              (5, 2),
              (6, 3),
              (6, 3),
              (7, 4),
              (7, 4),
              (9, 5),
              (9, 5),
              (9, 5),
              (9, 5)],
              [1, 5, 6, 7, 9]
              )
             ),
        )
        for first, second in examples:
            self.assert_lcs_length(first, second)

    def assert_lcs_length(self, first, second):
        self.assertEqual(lmi_length(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
