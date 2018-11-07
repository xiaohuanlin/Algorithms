'''

Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.

'''
import unittest


class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        time = len(B)//len(A)

        for time in (time, time + 1, time + 2):
            test_A = A * time
            for i in range(len(test_A)-len(B) + 1):
                # print(test_A[i: i+len(B)])
                if test_A[i: i+len(B)] == B:
                    return time
        return -1


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (('abcd', 'cdabcdab'), 3),
            (('a', 'aa'), 2),
            (('aa', 'a'), 1),
            (('abcd', 'dabcda'), 3),
            (("aaaaaaaaaaaaaaaaaaaaaab", "ba"), 2)
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().repeatedStringMatch(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
