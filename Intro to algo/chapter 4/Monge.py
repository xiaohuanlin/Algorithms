import unittest

def monge_min(A):
    '''
    :param A: list[list[num]] a monge list
    :return: list[num] min value of every row
    '''
    # todo: write the next
    i = 0
    while i < len(A) // 2:
        pass


class TestSolution(unittest.TestCase):


    def test_case(self):
        examples = (
            (([[1]], [[2]]), [[2]]),
            (([[1, 2],
               [3, 4]], [[4, 3],
                         [2, 1]]), [[8, 5],
                                    [20, 13]]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(monge_min(*first), second,
                         msg="first: {}; second: {}".format(first, second))



unittest.main()
