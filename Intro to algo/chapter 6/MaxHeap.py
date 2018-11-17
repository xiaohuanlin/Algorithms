import unittest
import math


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * (i + 1)


def parent(i):
    return (i - 1) // 2


def judge_heap(A):
    i = 0
    while i < math.ceil(len(A) / 2):
        l, r = left(i), right(i)
        candidate = [(i, A[i])]
        # consider if the l larger than length of A
        if l < len(A):
            candidate += [(l, A[l])]

        if r < len(A):
            candidate += [(r, A[r])]

        if max(candidate, key=lambda x: x[1])[0] != i:
            return False
        i += 1
    return True


def max_heapify(A, i, heap_size):
    '''
    :param A: list[int]
    :param i: adjust element A[i]
    :param heap_size: the size of heap
    :return: None, change the A in place. And only if there are almost heap, we can get the max heap
    complexity: O(lgn)
    '''
    # l = left(i)
    # r = right(i)
    # # consider if the l larger than length of A
    # if l < len(A) and A[l] > A[i]:
    #     largest = l
    # else:
    #     largest = i
    #
    # if r < len(A) and A[r] > A[largest]:
    #     largest = r
    #
    # if largest != i:
    #     # swap the value with A[i]
    #     A[i], A[largest] = A[largest], A[i]
    #     max_heapify(A, largest)
    # return A
    # ------------------------------------------------
    l = left(i)
    r = right(i)

    candidate = [(i, A[i])]
    # consider if the l larger than length of A
    if l < heap_size:
        candidate += [(l, A[l])]

    if r < heap_size:
        candidate += [(r, A[r])]

    # get the max record for in candidate
    largest, value = max(candidate, key=lambda x: x[1])

    if largest != i:
        # swap the value with A[i]
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest, heap_size)
    return A


def build_max_heap(A, heap_size):
    '''
    :param A: list[]
    :param heap_size: the size of heap
    :return: None
    complexity: O(n)
    '''
    # the leaf won't be changed to maintain max heap feature, so we only start at len(A)//2.
    for i in range(heap_size//2, -1, -1):
        max_heapify(A, i, heap_size)
    return A


def heap_sort(A):
    heap_size = len(A)
    build_max_heap(A, heap_size)
    for i in range(len(A)-1, 0, -1):
        # remove the answer to right place and change the heap size of A
        A[i], A[0] = A[0], A[i]
        heap_size -= 1
        max_heapify(A, 0, heap_size)
    return A


# ---------------------------------------------------------------------------------------------
# about heap operations
def heap_maximum(A):
    # O(1)
    return A[0]


def heap_extract_max(A, heap_size):
    # O(lgn)
    if heap_size < 1:
        raise ValueError('No data in heap')
    # swap with the last one
    max_value, A[0] = A[0], A[heap_size-1]
    heap_size -= 1
    max_heapify(A, 0, heap_size)
    return max_value


def heap_increase_key(A, i, key):
    # O(lgn)
    if key < A[i]:
        raise ValueError('New key small than current key')
    A[i] = key
    while i > 0 and A[i] > A[parent(i)]:
        # from bottom to top
        parent_index = parent(i)
        A[i], A[parent_index] = A[parent_index], A[i]
        i = parent_index
    return A


def heap_insert(A, key):
    # O(lgn)
    # append -inf to the tail and increase it to key
    A += [float('-inf')]
    heap_increase_key(A, len(A)-1, key)
    return A


def heap_delete(A, i):
    # todo: check how to write a correct delete function
    # O(lgn)
    A[i] = float('-inf')
    max_heapify(A, i, len(A))

    # check the last two element, swap the -inf to the end
    if len(A) > 1 and A[-2] < A[-1]:
        A[-1], A[-2] = A[-2], A[-1]
    A.pop()
    return A


class TestSolution(unittest.TestCase):

    def test_max_heapify(self):
        examples = (
            (([16,4,10,14,7,9,3,2,8,1], 1, 10), [16,14,10,8,7,9,3,2,4,1]),
            (([27,17,3,16,13,10,1,5,7,12,4,8,9,0], 2, 14), [27, 17, 10, 16, 13, 9, 1, 5, 7, 12, 4, 8, 3, 0])
        )
        for first, second in examples:
            self.assert_max_heapify(first, second)

    def assert_max_heapify(self, first, second):
        self.assertEqual(max_heapify(*first), second,
                         msg="first: {}; second: {}".format(first, second))

    def test_build_max_heap(self):
        examples = (
            (([4,1,3,2,16,9,10,14,8,7], 10), [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]),
            (([5,3,17,10,84,19,6,22,9], 9), [84, 22, 19, 10, 3, 17, 6, 5, 9])
        )
        for first, second in examples:
            self.assert_build_max_heap(first, second)

    def assert_build_max_heap(self, first, second):
        self.assertEqual(build_max_heap(*first), second,
                         msg="first: {}; second: {}".format(first, second))

    def test_heap_sort(self):
        examples = (
            ([4,1,3,2,16,9,10,14,8,7], [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]),
            ([5,3,17,10,84,19,6,22,9], [3, 5, 6, 9, 10, 17, 19, 22, 84])
        )
        for first, second in examples:
            self.assert_heap_sort(first, second)

    def assert_heap_sort(self, first, second):
        self.assertEqual(heap_sort(first), second,
                         msg="first: {}; second: {}".format(first, second))

    def test_heap_extract_max(self):
        examples = (
            ([4,1,3,2,16,9,10,14,8,7], 16),
            ([5,3,17,10,84,19,6,22,9], 84)
        )
        for first, second in examples:
            self.assert_heap_extract_max(first, second)

    def assert_heap_extract_max(self, first, second):
        build_max_heap(first, len(first))
        self.assertEqual(heap_extract_max(first, len(first)), second,
                         msg="first: {}; second: {}".format(first, second))
        self.assertEqual(judge_heap(first[:-1]), True,
                         msg="first: {}; second: {}".format(first, second))

    def test_heap_increase_key(self):
        examples = (
            (([4,1,3,2,16,9,10,14,8,7], 3, 50), [50, 16, 10, 14, 7, 9, 3, 2, 4, 1]),
            (([5,3,17,10,84,19,6,22,9], 4, 25), [84, 25, 19, 10, 22, 17, 6, 5, 9])
        )
        for first, second in examples:
            self.assert_heap_increase_key(first, second)

    def assert_heap_increase_key(self, first, second):
        build_max_heap(first[0], len(first[0]))
        ori_list = first[0].copy()
        increased_value = ori_list[first[1]]
        self.assertEqual(heap_increase_key(*first), second,
                         msg="first: {}; second: {}".format(first, second))
        # check the increased_value has been increased
        self.assertEqual(increased_value, (set(ori_list) - set(first[0])).pop())
        self.assertEqual(first[2], (set(first[0]) - set(ori_list)).pop())

        self.assertEqual(judge_heap(first[0]), True,
                         msg="first: {}; second: {}".format(first, second))

    def test_heap_insert(self):
        examples = (
            (([4,1,3,2,16,9,10,14,8,7], 5), [16, 14, 10, 8, 7, 9, 3, 2, 4, 1, 5]),
            (([5,3,17,10,84,19,6,22,9], 25), [84, 25, 19, 10, 22, 17, 6, 5, 9, 3])
        )
        for first, second in examples:
            self.assert_heap_insert(first, second)

    def assert_heap_insert(self, first, second):
        build_max_heap(first[0], len(first[0]))

        self.assertEqual(heap_insert(*first), second,
                         msg="first: {}; second: {}".format(first, second))

        self.assertEqual(judge_heap(first[0]), True,
                         msg="first: {}; second: {}".format(first, second))

    def test_heap_delete(self):
        examples = (
            (([4,1,3,2,16,9,10,14,8,7], 4), [16, 14, 10, 8, 1, 9, 3, 2, 4]),
            (([5,3,17,10,84,19,6,22,9], 7), [84, 22, 19, 10, 3, 17, 6, 9])
        )
        for first, second in examples:
            self.assert_heap_delete(first, second)

    def assert_heap_delete(self, first, second):
        build_max_heap(first[0], len(first[0]))

        self.assertEqual(heap_delete(*first), second,
                         msg="first: {}; second: {}".format(first, second))

        self.assertEqual(judge_heap(first[0]), True,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
