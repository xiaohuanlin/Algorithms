'''

Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

Example 1:

Input: [0,1,0]
Output: 1
Example 2:

Input: [0,2,1,0]
Output: 1
Note:

3 <= A.length <= 10000
0 <= A[i] <= 10^6
A is a mountain, as defined above.

'''
import unittest


class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        left = 0
        right = len(A) - 1
        while left < right:
            mid = (left + right) // 2
            # print(left, right, mid)
            if A[mid-1] < A[mid] and A[mid] > A[mid+1]:
                return mid
            elif A[mid-1] > A[mid]:
                right = mid
            else:
                left = mid


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ([0,1,0], 1),
            ([0,2,1,0], 1),
            ([0,1,2,1], 2)
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().peakIndexInMountainArray(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
