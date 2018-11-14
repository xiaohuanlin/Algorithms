import unittest


def get_inversion(A, p, r):
    count = 0
    if p < r - 1:
        q = (p + r) // 2
        count += get_inversion(A, p, q)
        count += get_inversion(A, q, r)
        count += merge(A, p, q, r)
    return count


def merge(A, p, q, r):
    '''
    :param A: sorted int list
    :param p: group index1
    :param q: group index2
    :param r: group index3
    :return: sorted int list
    there are two group A[p, q] and A[q, r]
    '''
    L = A[p:q]
    R = A[q:r]
    # print(L, R)

    i, j, c = 0, 0, 0
    inversion_count = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            A[p+c] = L[i]
            i += 1
        else:
            inversion_count += len(L) - i  # the only change code compare with merge-sort
            A[p+c] = R[j]
            j += 1
        c += 1

    if i == len(L):
        A[p+c:r] = R[j:r]
    else:
        A[p+c:r] = L[i:r]
    # print(inversion_count)
    return inversion_count


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([2,3,8,6,1], 0, 5), 5),
            (([], 0, 0), 0),
            (([4,3,2,1], 0, 4), 6),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(get_inversion(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
