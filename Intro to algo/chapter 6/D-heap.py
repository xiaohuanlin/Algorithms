import unittest
import math


def left(i, d):
    '''
    :param i: the parent index
    :param d: the number of children
    :return: the left child of all children
    '''
    return i * d + 1


def right(i, d):
    '''
    :param i: the parent index
    :param d: the number of children
    :return: the right child of all children
    '''
    return (i + 1) * d


def parent(i, d):
    '''
    :param i: the child index
    :param d: the number of children
    :return: the index of parent
    '''
    return (i - 1) // d


def judge_heap(A, d):
    i = 0
    while i < math.ceil(len(A) / d):
        l, r = left(i, d), right(i, d)

        candidate = [(i, A[i])]
        # consider if the index out of range
        candidate.extend([(index, A[index]) for index in range(l, r + 1) if index < len(A)])

        if max(candidate, key=lambda x: x[1])[0] != i:
            return False
        i += 1
    return True


def max_heapify(A, d, i, heap_size):
    '''
    :param A: list[int]
    :param d: the number of children
    :param i: adjust element A[i]
    :param heap_size: the size of heap
    :return: None, change the A in place. And only if there are almost heap, we can get the max heap
    complexity: O(lgn)
    '''
    l = left(i, d)
    r = right(i, d)

    candidate = [(i, A[i])]
    candidate.extend([(index, A[index]) for index in range(l, r + 1) if index < heap_size])

    # get the max record for in candidate
    largest, value = max(candidate, key=lambda x: x[1])

    if largest != i:
        # swap the value with A[i]
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, d, largest, heap_size)
    return A


def build_max_heap(A, d, heap_size):
    '''
    :param A: list[]
    :param d: the number of children
    :param heap_size: the size of heap
    :return: None
    complexity: O(n)
    '''
    # the leaf won't be changed to maintain max heap feature, so we only start at len(A)//d.
    for i in range(heap_size//d, -1, -1):
        max_heapify(A, d, i, heap_size)
    return A


# ---------------------------------------------------------------------------------------------
# about heap operations
def heap_maximum(A):
    # O(1)
    return A[0]


def heap_extract_max(A, d, heap_size):
    # O(lgn)
    if heap_size < 1:
        raise ValueError('No data in heap')
    # swap with the last one
    max_value, A[0] = A[0], A[heap_size-1]
    heap_size -= 1
    max_heapify(A, d, 0, heap_size)
    return max_value


def heap_increase_key(A, d, i, key):
    # O(lgn)
    if key < A[i]:
        raise ValueError('New key small than current key')
    A[i] = key
    while i > 0 and A[i] > A[parent(i, d)]:
        # from bottom to top
        parent_index = parent(i, d)
        A[i], A[parent_index] = A[parent_index], A[i]
        i = parent_index
    return A


def heap_insert(A, d, key):
    # O(lgn)
    # append -inf to the tail and increase it to key
    A += [float('-inf')]
    heap_increase_key(A, d, len(A)-1, key)
    return A


def heap_delete(A, d, i):
    # todo: check how to write a correct delete function
    # O(lgn)
    A[i] = float('-inf')
    max_heapify(A, d, i, len(A))
    print(A)
    # check the last d element, swap the -inf to the end
    candidate = [(index, A[index]) for index in range(-d, 0, 1) if abs(index) <= len(A)]
    smallest, value = min(candidate, key=lambda x: x[1])

    A[-1], A[smallest] = A[smallest], A[-1]

    A.pop()
    return A


class TestSolution(unittest.TestCase):

    def test_max_heapify(self):
        examples = (
            (([16,4,10,14,7,9,3,2,8,1], 3, 1, 10), [16, 9, 10, 14, 7, 4, 3, 2, 8, 1]),
            (([27,17,3,16,13,10,1,5,7,12,4,8,9,0], 4, 2, 14), [27, 17, 12, 16, 13, 10, 1, 5, 7, 3, 4, 8, 9, 0])
        )
        for first, second in examples:
            self.assert_max_heapify(first, second)

    def assert_max_heapify(self, first, second):
        self.assertEqual(max_heapify(*first), second,
                         msg="first: {}; second: {}".format(first, second))

    def test_build_max_heap(self):
        examples = (
            (([4,1,3,2,16,9,10,14,8,7], 3, 10), [16, 10, 14, 2, 1, 9, 4, 3, 8, 7]),
            (([5,3,17,10,84,19,6,22,9], 3, 9), [84, 19, 22, 10, 3, 5, 6, 17, 9])
        )
        for first, second in examples:
            self.assert_build_max_heap(first, second)

    def assert_build_max_heap(self, first, second):
        self.assertEqual(build_max_heap(*first), second,
                         msg="first: {}; second: {}".format(first, second))
        self.assertEqual(judge_heap(first[0], first[1]), True,
                         msg="first: {}; second: {}".format(first, second))

    def test_heap_extract_max(self):
        examples = (
            (([4,1,3,2,16,9,10,14,8,7], 3), 16),
            (([5,3,17,10,84,19,6,22,9], 3), 84)
        )
        for first, second in examples:
            self.assert_heap_extract_max(first, second)

    def assert_heap_extract_max(self, first, second):
        build_max_heap(first[0], first[1], len(first[0]))
        self.assertEqual(heap_extract_max(first[0], first[1], len(first[0])), second,
                         msg="first: {}; second: {}".format(first, second))
        self.assertEqual(judge_heap(first[0][:-1], first[1]), True,
                         msg="first: {}; second: {}".format(first, second))

    def test_heap_increase_key(self):
        examples = (
            (([4,1,3,2,16,9,10,14,8,7], 3, 3, 50), [50, 10, 14, 16, 1, 9, 4, 3, 8, 7]),
            (([5,3,17,10,84,19,6,22,9], 3, 4, 25), [84, 25, 22, 10, 19, 5, 6, 17, 9])
        )
        for first, second in examples:
            self.assert_heap_increase_key(first, second)

    def assert_heap_increase_key(self, first, second):
        build_max_heap(first[0], first[1], len(first[0]))
        ori_list = first[0].copy()
        increased_value = ori_list[first[2]]
        self.assertEqual(heap_increase_key(*first), second,
                         msg="first: {}; second: {}".format(first, second))
        # check the increased_value has been increased
        self.assertEqual(increased_value, (set(ori_list) - set(first[0])).pop())
        self.assertEqual(first[3], (set(first[0]) - set(ori_list)).pop())

        self.assertEqual(judge_heap(first[0], first[1]), True,
                         msg="first: {}; second: {}".format(first, second))

    def test_heap_insert(self):
        examples = (
            (([4,1,3,2,16,9,10,14,8,7], 3, 5), [16, 10, 14, 5, 1, 9, 4, 3, 8, 7, 2]),
            (([5,3,17,10,84,19,6,22,9], 3, 25), [84, 19, 25, 10, 3, 5, 6, 17, 9, 22])
        )
        for first, second in examples:
            self.assert_heap_insert(first, second)

    def assert_heap_insert(self, first, second):
        build_max_heap(first[0], first[1], len(first[0]))

        self.assertEqual(heap_insert(*first), second,
                         msg="first: {}; second: {}".format(first, second))

        self.assertEqual(judge_heap(first[0], first[1]), True,
                         msg="first: {}; second: {}".format(first, second))

    def test_heap_delete(self):
        examples = (
            (([4,1,3,2,16,9,10,14,8,7], 3, 4), [16, 14, 10, 8, 1, 9, 3, 2, 4]),
            (([5,3,17,10,84,19,6,22,9], 3, 7), [84, 22, 19, 10, 3, 17, 6, 9])
        )
        for first, second in examples:
            self.assert_heap_delete(first, second)

    def assert_heap_delete(self, first, second):
        build_max_heap(first[0], first[1], len(first[0]))

        self.assertEqual(heap_delete(*first), second,
                         msg="first: {}; second: {}".format(first, second))

        self.assertEqual(judge_heap(first[0], first[1]), True,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
