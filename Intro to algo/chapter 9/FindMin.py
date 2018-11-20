import unittest


def find_max_and_min(A):
    # using pair compare to reduce time, it will cost about 3*(n/2)
    if len(A) % 2 == 1:
        # odd length will use the same value as origin value
        min_value, max_value = A[0], A[0]
        test_list = A[1:]
    else:
        min_value, max_value = min(A[0], A[1]), max(A[0], A[1])
        test_list = A[2:]

    for i in range(0, len(test_list), 2):
        test_min, test_max = min(test_list[i], test_list[i + 1]), max(test_list[i], test_list[i + 1])
        if test_min < min_value:
            min_value = test_min
        if test_max > max_value:
            max_value = test_max
    return min_value, max_value


def find_2ndmin(A):
    '''
    :param A: list[]
    :return: 2nd min value
    complexity: O(n + lg(n)), it will need space O(n)
    '''
    # we divide the list into two part, and compare with each other, so that we can get two list to using
    # for finding min value.
    # eg: a = [1, 2, 5, 7] --> (1, 2) and (5, 7) --> s = [1, 5] l = [2, 7]
    # record all pairs, because when we finally find the min value, the second min value must be compared
    # with it, otherwise it will locate on s list.
    s = []
    from collections import defaultdict
    record = defaultdict(list)
    while len(A) > 1:
        for i in range(0, len(A), 2):
            if i+1 < len(A):
                min_value = min(A[i], A[i+1])
                s.append(min_value)
                record[A[i]].append(A[i+1])
            else:
                # the last value of list
                s.append(A[i])
        A = s
        s = []

    min_value = A[0]
    # search the 2nd_min_value
    return min(record[min_value])


class TestSolution(unittest.TestCase):

    def test_find_max_and_min(self):
        examples = (
            ([1,3,5,6,12,3,5,23,4,61], (1, 61)),
        )
        for first, second in examples:
            self.assert_find_max_and_min(first, second)

    def assert_find_max_and_min(self, first, second):
        self.assertEqual(find_max_and_min(first), second,
                         msg="first: {}; second: {}".format(first, second))

    def test_find_2ndmin(self):
        examples = (
            ([1,3,5,6,12,3,5,23,4,61], 3),
        )
        for first, second in examples:
            self.assert_find_2ndmin(first, second)

    def assert_find_2ndmin(self, first, second):
        self.assertEqual(find_2ndmin(first), second,
                         msg="first: {}; second: {}".format(first, second))

unittest.main()
