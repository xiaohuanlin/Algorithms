'''
Given an integer array arr and a target value target, return the integer value such that when we change all the integers larger than value in the given array to be equal to value, the sum of the array gets as close as possible (in absolute difference) to target.

In case of a tie, return the minimum such integer.

Notice that the answer is not neccesarilly a number from arr.

 

Example 1:

Input: arr = [4,9,3], target = 10
Output: 3
Explanation: When using 3 arr converts to [3, 3, 3] which sums 9 and that's the optimal answer.
Example 2:

Input: arr = [2,3,5], target = 10
Output: 5
Example 3:

Input: arr = [60864,25176,27249,21296,20204], target = 56803
Output: 11361
 

Constraints:

1 <= arr.length <= 104
1 <= arr[i], target <= 105
'''
from typing import *

import unittest

from bisect import bisect

class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        def cal(middle):
            pos = bisect(arr, middle)
            return sum(arr[:pos]) + middle * (len(arr) - pos)
            
        arr.sort()
        start = 0
        end = arr[-1]
        while start < end:
            middle = (start + end) // 2
            res = cal(middle)
            if res > target:
                end = middle - 1
            elif res == target:
                return middle
            else:
                start = middle + 1
        left = abs(cal(start - 1) - target)
        middle = abs(cal(start) - target)
        right = abs(cal(start + 1) - target)
        if left <= middle:
            return start - 1
        if right < middle:
            return start + 1
        return start



class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([4,9,3], 10), 3),
            (([2,3,5], 10), 5),
            (([60864,25176,27249,21296,20204], 56803), 11361),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().findBestValue(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
