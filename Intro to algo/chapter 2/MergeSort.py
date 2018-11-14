import unittest


def merge_sorted(A, p, r):
    if p < r - 1:
        q = (p+r) // 2
        merge_sorted(A, p, q)
        merge_sorted(A, q, r)
        merge(A, p, q, r)
    return A


def merge(A, p, q, r):
    '''
    :param A: sorted int list
    :param p: group index1
    :param q: group index2
    :param r: group index3
    :return: sorted int list
    there are two group A[p, q] and A[q, r]
    '''
    # L = A[p:q]
    # R = A[q:r]
    #
    # i, j, c = 0, 0, 0
    # while i < len(L) and j < len(R):
    #     if L[i] < R[j]:
    #         A[p+c] = L[i]
    #         i += 1
    #     else:
    #         A[p+c] = R[j]
    #         j += 1
    #     c += 1
    #
    # if i == len(L):
    #     A[p+c:r] = R[j:r]
    # else:
    #     A[p+c:r] = L[i:r]
    # ------------------------------------------
    # add an end value to avoid comparing i or j with the final value
    L = A[p:q] + [float('+inf')]
    R = A[q:r] + [float('+inf')]
    i, j = 0, 0
    for k in range(p, r):
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,3,5,2,6,4], 0, 6), [1,2,3,4,5,6]),
            (([], 0, 0), []),
            (([4,3,2,1], 0, 4), [1,2,3,4])
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(merge_sorted(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
