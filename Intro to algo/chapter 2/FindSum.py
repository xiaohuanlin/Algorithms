import unittest


def binary_search(A, v):
    '''
    :param A: sorted int list
    :param v: target value
    :return: the index of the value, the complex is O(lgn)
    '''
    if len(A) == 1:
        return 0 if A[0] == v else None
    q = len(A) // 2
    if A[q] > v:
        return binary_search(A[:q], v)
    else:
        return binary_search(A[q:], v) + q


def find_sum(S, num_sum):
    '''
    :param S: the set of n number
    :param num_sum: the target sum of two number
    :return: bool
    '''
    S = sorted(list(S))
    for i, n in enumerate(S):
        target = num_sum - n
        index = binary_search(S, target)
        if index and i != index:
            return True
    return False


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (({1, 5, 2, 4}, 5), True),
            (({1, 5, 2, 4}, 1), False),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(find_sum(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
