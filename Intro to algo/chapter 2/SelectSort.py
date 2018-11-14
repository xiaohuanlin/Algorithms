import unittest


def select_sorted(s):
    for i in range(len(s)):
        min_value_index = j = i
        min_value = s[min_value_index]
        while j < len(s):
            if s[j] < min_value:
                min_value = s[j]
                min_value_index = j
            j += 1
        s[i], s[min_value_index] = s[min_value_index], s[i]
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
        self.assertEqual(select_sorted(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
