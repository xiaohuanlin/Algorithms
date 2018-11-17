import unittest
import random


def quick_sort(A, p, r):
    if p >= r - 1:
        return None
    q = partition(A, p, r)
    quick_sort(A, p, q)
    quick_sort(A, q, r)
    return A


def partition(A, p, r):
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


def random_partition(A, p, r):
    i = random.randint(p, r-1)
    A[r-1], A[i] = A[i], A[r-1]
    return partition(A, p, r)


def random_quick_sort(A, p, r):
    if p >= r - 1:
        return None
    q = random_partition(A, p, r)
    random_quick_sort(A, p, q)
    random_quick_sort(A, q, r)
    return A


def hoare_quick_sort(A, p, r):
    if p >= r - 1:
        return None
    q = hoare_partition(A, p, r)
    quick_sort(A, p, q)
    quick_sort(A, q, r)
    return A


def hoare_partition(A, p, r):
    # choose the last element as pivot element
    pivot_element = A[p]
    # cut the whole list into two part, with two points
    i, j = p, r-1
    while True:
        # consider that the equal element during whole list, so we can't assume A[j] > pivot_element and A[i] <
        # pivot_element
        while j >= i and A[j] > pivot_element:
            j -= 1
        while i <= j and A[i] <= pivot_element:
            i += 1

        if i < j:
            # swap the two element
            A[i], A[j] = A[j], A[i]
        else:
            return j


def same_element_quick_sort(A, p, r):
    if p >= r - 1:
        return None
    q, t = same_element_partition(A, p, r)
    same_element_quick_sort(A, p, q)
    same_element_quick_sort(A, t, r)
    return A


def same_element_partition(A, p, r):
    # choose the last element as pivot element
    pivot_element = A[r-1]
    # cut the list into four parts: [0, i] is less than pivot part, [i, j] is the equal part, [j, k] is the same
    # part, and the last part is candidate part.
    i, j, k = p-1, p-1, p
    while k < r - 1:
        if A[k] <= pivot_element:
            j += 1
            A[k], A[j] = A[j], A[k]
        if A[k] < pivot_element:
            # when A[k] less than pivot_element, we need exchange the element and set it to the another part
            i += 1
            A[i], A[j] = A[j], A[i]
        k += 1

    A[j+1], A[r-1] = A[r-1], A[j+1]
    return i + 1, j + 1


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([2, 8, 7, 1, 3, 5, 6, 4], 0, 8), [1, 2, 3, 4, 5, 6, 7, 8]),
            (([2, 2, 2, 2, 2, 2, 2, 2], 0, 8), [2, 2, 2, 2, 2, 2, 2, 2]),
            (([2, 4, 3, 4, 5, 2, 1, 2], 0, 8), [1, 2, 2, 2, 3, 4, 4, 5]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(quick_sort(*first), second,
                         msg="first: {}; second: {}".format(first, second))
        self.assertEqual(random_quick_sort(*first), second,
                         msg="first: {}; second: {}".format(first, second))
        self.assertEqual(hoare_quick_sort(*first), second,
                         msg="first: {}; second: {}".format(first, second))
        self.assertEqual(same_element_quick_sort(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
