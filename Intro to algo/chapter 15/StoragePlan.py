import unittest
import unittest.mock
import io
from pprint import pprint


def storage_plan(demand, month_num, pro_ability, extra_fee, storage_func):
    # we transfer the demand list to a demand list because of the striation of this
    # problem.
    sum_demand = [0] * len(demand)
    for i in range(len(demand)):
        sum_demand[i] = sum_demand[i-1] + demand[i]

    # result table consists of months and sum_pro
    result = [[float('-inf')] * sum_demand[-1] for _ in range(month_num)]
    select = [[None] * sum_demand[-1] for _ in range(month_num)]

    # initial data: the first mouth will produce all demand
    for j in range(len(result[0])):
        # j means the number of product since month 1
        storage_fee = storage_func(j - sum_demand[0]) if j >= sum_demand[0] else 0
        result[0][j] = storage_fee + extra_fee * max(j - pro_ability, 0)
        select[0][j] = j

    for i in range(1, month_num):
        for j in range(sum_demand[i-1], sum_demand[-1]):
            result[i][j] = float('+inf')
            for k in range(j - sum_demand[i-1]):
                # make sure meet the requirement
                storage_fee = storage_func(j - sum_demand[i]) if j >= sum_demand[i] else 0
                min_value = result[i-1][j-k] + storage_fee + extra_fee * max(k-pro_ability, 0)
                if min_value < result[i][j]:
                    result[i][j] = min_value
                    select[i][j] = k

    pprint(select, width=200)
    print_select(select, month_num - 1, sum_demand[-1] - 1)
    return result, select


def print_select(select, i, j):
    if i >= 0:
        print_select(select, i-1, j-select[i][j])
        print(select[i][j])


class TestSolution(unittest.TestCase):

    def test_string_split(self):
        # todo: check why the answer is wrong
        examples = (
            (([3, 5, 8, 7, 4], 5, 4, 2, lambda x: x),
             []
             ),
        )
        for first, second in examples:
            self.assert_string_split(first, second)

    def assert_string_split(self, first, second):
        self.assertEqual(storage_plan(*first), second,
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
