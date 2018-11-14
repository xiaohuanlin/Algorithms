import unittest


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


def recursion_insert_sorted(s):
    if len(s) < 1:
        return s

    key = s[-1]
    recursion_insert_sorted(s[:-1])
    j = len(s) - 2
    while j >= 0 and s[j] > key:
        s[j + 1] = s[j]
        j -= 1
    s[j + 1] = key
    return s


def bs_insert_sorted(s):
    # todo: check the error

    def binary_search(s, l, r, key):
        if r - l == 0:
            return 0
        if r - l == 1:
            return l+1 if s[l] < key else l
        m = (l + r) // 2
        if s[m] > key:
            return binary_search(s, l, m, key)
        else:
            return binary_search(s, m, r, key) + m - l

    for i in range(1, (len(s))):
        # store the key value
        j = i - 1
        print(s)
        index = binary_search(s, 0, j, s[i])
        print(i, j, index)
        s[index:i+1] = [s[i]] + s[index:i]
    return s




class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ([1,3,5,2,6,4], [1,2,3,4,5,6]),
            ([], []),
            ([4,3,2,1], [1,2,3,4])
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(insert_sorted(first), second,
                         msg="first: {}; second: {}".format(first, second))
        self.assertEqual(recursion_insert_sorted(first), second,
                         msg="first: {}; second: {}".format(first, second))
        self.assertEqual(bs_insert_sorted(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
