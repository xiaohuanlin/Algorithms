'''

An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.



Example 1:

Input: [1,2,2,3]
Output: true
Example 2:

Input: [6,5,4,4]
Output: true
Example 3:

Input: [1,3,2]
Output: false
Example 4:

Input: [1,2,4,5]
Output: true
Example 5:

Input: [1,1,1]
Output: true

'''
import unittest


class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) <= 2:
            return True
        pre = A[0]
        direct = A[1] - A[0]
        for num in A[1:]:
            if direct < 0 and num > pre:
                return False
            if direct > 0 and num < pre:
                return False
            if direct == 0 and num - pre != 0:
                direct = num - pre
            pre = num
        return True

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ([1,2,2,3], True),
            ([6,5,4,4], True),
            ([1,3,2], False),
            ([1,2,4,5], True),
            ([1,1,1], True),
            ([11,11,9,4,3,3,3,1,-1,-1,3,3,3,5,5,5], False),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().isMonotonic(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
