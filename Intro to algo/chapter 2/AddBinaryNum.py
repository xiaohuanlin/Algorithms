import unittest


def add_binary_num(A, B):
    '''
    :param A: n-length array of binary
    :param B: n-length array of binary
    :return: n+1-lenght array of binary
    '''
    length = len(A)
    C = [0] * (length + 1)
    carry = 0
    while length > 0:
        res = A[length-1] + B[length-1] + carry
        carry, C[length] = res >> 1, res & 1
        length -= 1
    # maybe there are still have carry
    C[0] = carry
    return C


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,0,1,0,1], [1,1,1,1,1]), [1,1,0,1,0,0]),
            (([0,0,1], [0,1,0]), [0,0,1,1]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(add_binary_num(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
