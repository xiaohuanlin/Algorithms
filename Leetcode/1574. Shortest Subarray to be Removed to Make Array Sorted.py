'''
Given an integer array arr, remove a subarray (can be empty) from arr such that the remaining elements in arr are non-decreasing.

Return the length of the shortest subarray to remove.

A subarray is a contiguous subsequence of the array.

 

Example 1:

Input: arr = [1,2,3,10,4,2,3,5]
Output: 3
Explanation: The shortest subarray we can remove is [10,4,2] of length 3. The remaining elements after that will be [1,2,3,3,5] which are sorted.
Another correct solution is to remove the subarray [3,10,4].
Example 2:

Input: arr = [5,4,3,2,1]
Output: 4
Explanation: Since the array is strictly decreasing, we can only keep a single element. Therefore we need to remove a subarray of length 4, either [5,4,3,2] or [4,3,2,1].
Example 3:

Input: arr = [1,2,3]
Output: 0
Explanation: The array is already non-decreasing. We do not need to remove any elements.
 

Constraints:

1 <= arr.length <= 105
0 <= arr[i] <= 109
'''
import unittest

from typing import *

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        right = len(arr) - 1
        
        for i in range(len(arr) - 1)[::-1]:
            if arr[i] > arr[i+1]:
                break
            right = i
    
        res = len(arr) - right
        # two pointers
        for left in range(len(arr)):
            if left > 0 and arr[left] < arr[left - 1]:
                break
            
            while right < len(arr) and arr[left] > arr[right]:
                right += 1
                
            if left >= right:
                break
            res = max(res, left + 1 + len(arr) - right)
        return len(arr) - res

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,2,3,10,4,2,3,5],), 3),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().findLengthOfShortestSubarray(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()