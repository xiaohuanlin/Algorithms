import unittest

'''
blurry sort for interval, and only give a rough result is ok
'''


def blurry_quick_sort(A, p, r):
    if p >= r - 1:
        return None
    q, t = blurry_element_partition(A, p, r)
    blurry_quick_sort(A, p, q)
    blurry_quick_sort(A, t, r)
    return A


def blurry_element_partition(A, p, r):
    # choose the last element as pivot element
    pivot_element = A[r-1]
    # cut the list into four parts: [0, i] is less than pivot part, [i, j] is the equal part, [j, k] is the same
    # part, and the last part is candidate part.
    i, j, k = p-1, p-1, p
    while k < r - 1:
        if A[k][1] < pivot_element[0]:
            # assume that the large value of A[k] < the small value of pivot_element means A[k] less than pivot_element
            j += 1
            A[k], A[j] = A[j], A[k]
            i += 1
            A[i], A[j] = A[j], A[i]
        elif A[k][0] > pivot_element[1]:
            # it means A[k] > pivot_element
            pass
        else:
            # which means the A[k] overlap with pivot_element
            j += 1
            A[k], A[j] = A[j], A[k]
        k += 1
    A[j+1], A[r-1] = A[r-1], A[j+1]
    return i + 1, j + 1


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([[2,4], [29,39], [30,32], [10, 20], [6,12]], 0, 5), [[2, 4], [10, 20], [6, 12], [29, 39], [30, 32]]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(blurry_quick_sort(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()