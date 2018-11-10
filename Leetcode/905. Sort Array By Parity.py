'''

Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.



Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.


Note:

1 <= A.length <= 5000
0 <= A[i] <= 5000

'''
import unittest


class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i = 0
        j = len(A) - 1
        while i < j:
            if A[i] % 2 == 1 and A[j] % 2 == 0:
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1
            elif A[i] % 2 == 0 and A[j] % 2 == 1:
                i += 1
                j -= 1
            elif A[i] % 2 == 1:
                j -= 1
            else:
                i += 1
        return A



class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ([3,1,2,4], [4, 2, 1, 3]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().sortArrayByParity(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
