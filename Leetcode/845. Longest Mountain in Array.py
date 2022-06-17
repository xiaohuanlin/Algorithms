'''
You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given an integer array arr, return the length of the longest subarray, which is a mountain. Return 0 if there is no mountain subarray.

 

Example 1:

Input: arr = [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
Example 2:

Input: arr = [2,2,2]
Output: 0
Explanation: There is no mountain.
 

Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 104
 

Follow up:

Can you solve it using only one pass?
Can you solve it in O(1) space?
'''
import unittest
from typing import *

from heapq import heappush, heappop

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        increase = True
        count = 0
        res = 0
        for i in range(len(arr) - 1):
            if increase:
                if arr[i] < arr[i+1]:
                    count += 1
                elif arr[i] == arr[i+1]:
                    count = 0
                else:
                    if count == 0:
                        continue
                    increase = False
                    count += 1
            else:
                if arr[i] > arr[i+1]:
                    count += 1
                else:
                    res = max(res, count + 1)
                    increase = True
                    if arr[i] == arr[i+1]:
                        count = 0
                    else:
                        count = 1
        if not increase:
            res = max(res, count + 1)
        return res

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([2,1,4,7,3,2,5],),5),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().longestMountain(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()