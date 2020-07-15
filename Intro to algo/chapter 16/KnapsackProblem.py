import unittest
import unittest.mock
import io
from pprint import pprint


def find_most_value(value_list, weight_list, total_weight):
    dp = [[0 for _ in range(len(value_list)+1)] for _ in range(total_weight)]

    for col in range(1, len(value_list) + 1):
        for row in range(total_weight):
            if row - weight_list[col-1] >= 0:
                dp[row][col] = max(dp[row-weight_list[col-1]][col-1] + value_list[col-1], dp[row][col-1])
    
    return dp[total_weight-1][len(value_list)]


class TestSolution(unittest.TestCase):

    def test_string_split(self):
        examples = (
            (([3,5,7,10,12], [7,9,3,1,2], 10), 29),
        )
        for first, second in examples:
            self.assert_string_split(first, second)

    def assert_string_split(self, first, second):
        self.assertEqual(find_most_value(*first), second,
                         msg="first: {}; second: {}".format(first, second))



unittest.main()
