'''

We are given two strings, A and B.

A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.

Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true

Example 2:
Input: A = 'abcde', B = 'abced'
Output: false
Note:

A and B will have length at most 100.

'''
import unittest


class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        # if A == '' and B == '':
        #     return True
        # D_A = A * 2
        # for i in range(len(A)):
        #     if D_A[i:i+len(A)] == B:
        #         return True
        # return False
        return B in A * 2 if len(A) == len(B) else False


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (('abcde', 'cdeab'), True),
            (('abcde', 'abced'), False),
            (('', ''), True)
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().rotateString(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
