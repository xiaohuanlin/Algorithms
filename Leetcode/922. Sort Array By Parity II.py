'''

Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.



Example 1:

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.


Note:

2 <= A.length <= 20000
A.length % 2 == 0
0 <= A[i] <= 1000

'''
import unittest


class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        result = [0] * len(A)
        even_count = 0
        odd_count = 1
        for i in range(len(A)):
            if A[i] % 2 == 0:
                result[even_count] = A[i]
                even_count += 2
            else:
                result[odd_count] = A[i]
                odd_count += 2
        return result


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ([4,2,5,7], [4,5,2,7]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().sortArrayByParityII(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
