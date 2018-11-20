import unittest


def counting_sort(A, B, k):
    '''
    :param A: the origin list[]
    :param B: the result list[]
    :param k: the max value of A or larger than it
    :return: B
    complexity: Θ(n), which is a stable algo
    '''
    # generate C as counting value of number
    C = [0] * k

    for i in range(len(A)):
        # count the same value
        C[A[i]] += 1

    for i in range(1, k):
        # calculate the accumulate value
        C[i] = C[i - 1] + C[i]

    for i in range(len(A) - 1, -1, -1):
        # copy the A[i] to B according to count
        B[C[A[i]] - 1] = A[i]
        C[A[i]] -= 1
    return B


def radix_counting_sort(A, B, d, search_digit, base):
    '''
    :param A: the origin list[num]
    :param B: the result list[num]
    :param d: the length of num
    :param search_digit: using d-th number to sort list
    :param base: the max value of A
    :return: B
    complexity: Θ(n)
    '''

    def get_d_num(num, length, search_digit):
        '''
        :param num: num
        :param length: the length of num
        :return: the d-th num
        '''
        return (num // base ** (length - 1 - search_digit)) % base

    # generate C as counting value of number
    C = [0] * base

    for i in range(len(A)):
        # count the same value
        C[get_d_num(A[i], d, search_digit)] += 1  # only change this!

    for i in range(1, base):
        # calculate the accumulate value
        C[i] = C[i - 1] + C[i]

    for i in range(len(A) - 1, -1, -1):
        # copy the A[i] to B according to count
        B[C[get_d_num(A[i], d, search_digit)] - 1] = A[i]  # only change this!
        C[get_d_num(A[i], d, search_digit)] -= 1  # only change this!
    return B


def radix_sort(A, d):
    '''
    :param A: the list of number
    :param d: the length of number
    :return: None
    '''
    base = 10
    for i in range(d - 1, -1, -1):
        A = radix_counting_sort(A, [0] * len(A), d, i, base)
    return A


def no_length_radix_sort(A):
    '''
    :param A: the list of number
    :return: None
    '''
    d = max(len(str(num)) for num in A)
    base = 10
    for i in range(d - 1, -1, -1):
        A = radix_counting_sort(A, [0] * len(A), d, i, base)
    return A

# todo: implement counting sort in place


class TestSolution(unittest.TestCase):

    def test_counting_sort(self):
        examples = (
            (([2, 8, 7, 1, 3, 5, 6, 4], [0, 0, 0, 0, 0, 0, 0, 0], 10), [1, 2, 3, 4, 5, 6, 7, 8]),
            (([2, 2, 2, 2, 2, 2, 2, 2], [0, 0, 0, 0, 0, 0, 0, 0], 10), [2, 2, 2, 2, 2, 2, 2, 2]),
            (([2, 4, 3, 4, 5, 2, 1, 2], [0, 0, 0, 0, 0, 0, 0, 0], 10), [1, 2, 2, 2, 3, 4, 4, 5]),
        )
        for first, second in examples:
            self.assert_counting_sort(first, second)

    def assert_counting_sort(self, first, second):
        self.assertEqual(counting_sort(*first), second,
                         msg="first: {}; second: {}".format(first, second))

    def test_radix_sort(self):
        examples = (
            (([230, 125, 592, 121, 235, 663, 110, 533], 3), [110, 121, 125, 230, 235, 533, 592, 663]),
        )
        for first, second in examples:
            self.assert_radix_sort(first, second)

    def assert_radix_sort(self, first, second):
        self.assertEqual(radix_sort(*first), second,
                         msg="first: {}; second: {}".format(first, second))

    def test_no_length_radix_sort(self):
        examples = (
            ([230, 125, 592, 121, 235, 663, 110, 533], [110, 121, 125, 230, 235, 533, 592, 663]),
            ([30, 1225, 432592, 121, 2235, 3, 1110, 533], [3, 30, 121, 533, 1110, 1225, 2235, 432592]),
        )
        for first, second in examples:
            self.assert_no_length_radix_sort(first, second)

    def assert_no_length_radix_sort(self, first, second):
        self.assertEqual(no_length_radix_sort(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
