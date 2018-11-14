import unittest


def reverse_insert_sorted(s):
    for i in range(1, (len(s))):
        # store the key value
        key = s[i]
        j = i - 1
        while j >= 0 and s[j] < key:
            s[j+1] = s[j]
            j -= 1
        s[j+1] = key
    return s


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ([1,3,5,2,6,4], [6,5,4,3,2,1]),
            ([], []),
            ([4,3,2,1], [4,3,2,1])
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(reverse_insert_sorted(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
