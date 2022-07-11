'''
Given an array of integers, return the maximum sum for a non-empty subarray (contiguous elements) with at most one element deletion. In other words, you want to choose a subarray and optionally delete one element from it so that there is still at least one element left and the sum of the remaining elements is maximum possible.

Note that the subarray needs to be non-empty after deleting one element.

 

Example 1:

Input: arr = [1,-2,0,3]
Output: 4
Explanation: Because we can choose [1, -2, 0, 3] and drop -2, thus the subarray [1, 0, 3] becomes the maximum value.
Example 2:

Input: arr = [1,-2,-2,3]
Output: 3
Explanation: We just choose [3] and it's the maximum sum.
Example 3:

Input: arr = [-1,-1,-1,-1]
Output: -1
Explanation: The final subarray needs to be non-empty. You can't choose [-1] and delete -1 from it, then get an empty subarray to make the sum equals to 0.
 

Constraints:

1 <= arr.length <= 105
-104 <= arr[i] <= 104
'''
from typing import *
import unittest

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        dp_all = arr[0]
        dp_one = arr[0]
        res = arr[0]
        for i in range(1, len(arr)):
            dp_one = max(dp_all, dp_one + arr[i], arr[i])
            dp_all = max(dp_all + arr[i], arr[i])
            res = max(res, dp_one)

        return res

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([-1,-1,-1,-1],),-1),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maximumSum(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()