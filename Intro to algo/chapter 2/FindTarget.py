import unittest


def find_target(A, v):
    '''
    :param A: int list
    :param v: target value
    :return: the index of the value, the complex is O(n)
    '''
    for i in range(len(A)):
        if A[i] == v:
            return i
    return None


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
        self.assertEqual(find_target(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
