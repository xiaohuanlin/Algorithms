import unittest
import math


def insert_sorted(s):
    for i in range(1, (len(s))):
        # store the key value
        key = s[i]
        j = i - 1
        while j >= 0 and s[j] > key:
            s[j+1] = s[j]
            j -= 1
        s[j+1] = key
    return s


def bucket_sort(A):
    '''
    :param A: list[num], num of which all in [0, 1]
    :return: None
    complexity: Θ(n)
    It similar to use the hash table store the value, and sort every list.
    '''
    n = len(A)
    B = [[] for _ in range(n)]
    for i in range(n):
        B[math.floor(n * A[i])].append(A[i])
    for i in range(n):
        insert_sorted(B[i])
    return [ele for row in B for ele in row]


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ([.2, .8, .7, .1, .3, .5, .6, .4], [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]),
            ([.2, .4, .3, .4, .5, .2, .1, .2], [0.1, 0.2, 0.2, 0.2, 0.3, 0.4, 0.4, 0.5]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(bucket_sort(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
