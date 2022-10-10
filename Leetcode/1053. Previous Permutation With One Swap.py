'''
Given an array of positive integers arr (not necessarily distinct), return the lexicographically largest permutation that is smaller than arr, that can be made with exactly one swap (A swap exchanges the positions of two numbers arr[i] and arr[j]). If it cannot be done, then return the same array.

 

Example 1:

Input: arr = [3,2,1]
Output: [3,1,2]
Explanation: Swapping 2 and 1.
Example 2:

Input: arr = [1,1,5]
Output: [1,1,5]
Explanation: This is already the smallest permutation.
Example 3:

Input: arr = [1,9,4,6,7]
Output: [1,7,4,6,9]
Explanation: Swapping 9 and 7.
 

Constraints:

1 <= arr.length <= 104
1 <= arr[i] <= 104
'''
from typing import *

import unittest

from bisect import bisect_right
from bisect import bisect_left

class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        for i in range(1, len(arr))[::-1]:
            if arr[i-1] > arr[i]:
                p = bisect_right(arr, arr[i-1] - 1, i, len(arr)) - 1
                p = bisect_left(arr, arr[p], i, p + 1)
                arr[i-1], arr[p] = arr[p], arr[i-1]
                break
        return arr


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,1,5],), [1,1,5]),
        )

        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().prevPermOpt1(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()