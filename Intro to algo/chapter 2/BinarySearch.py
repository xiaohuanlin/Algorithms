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


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([3], 3), 0),
            (([1,2,3,4,5], 3), 2),
            (([5,1,3,4,1], 3), 2),
            (([1,5,2], 3), None)
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(binary_search(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
