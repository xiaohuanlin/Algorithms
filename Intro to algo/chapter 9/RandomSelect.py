import unittest


def random_select(A, p, r, i):
    '''
    :param A: list[]
    :param p: start point
    :param r: end point
    :param i: the i-th, starts from 1.
    :return: the number of i-th
    '''
    if p == r - 1:
        return A[p]
    q = random_partition(A, p, r)
    # that is the relative position compare to p, and add 1 because of the i-th.
    k = q - p + 1
    if i == k:
        return A[q]
    elif i < k:
        return random_select(A, p, q, i)
    else:
        return random_select(A, q, r, i - k)


def random_partition(A, p, r):
    # choose the last element as pivot element
    pivot_element = A[r-1]
    # cut the list into three parts: [0, i] is less than pivot part, [i, j] is great than pivot part, and the
    # last part is candidate part.
    i, j = p-1, p
    while j < r - 1:
        if A[j] <= pivot_element:
            i += 1
            # now the A[i] actually is the first element of large part. After swapping with A[j], A[i] become the
            # part of less
            A[i], A[j] = A[j], A[i]
        j += 1

    A[i+1], A[r-1] = A[r-1], A[i+1]
    return i + 1


def kth_quantile():
    # todo: implement the algo
    pass


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([2, 8, 7, 1, 3, 5, 6, 4], 0, 8, 3), 3),
            (([2, 2, 2, 2, 2, 2, 2, 2], 0, 8, 1), 2),
            (([2, 4, 3, 4, 5, 2, 1, 2], 0, 8, 4), 2),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(random_select(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
