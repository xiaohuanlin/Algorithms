'''
You are given three positive integers: n, index, and maxSum. You want to construct an array nums (0-indexed) that satisfies the following conditions:

nums.length == n
nums[i] is a positive integer where 0 <= i < n.
abs(nums[i] - nums[i+1]) <= 1 where 0 <= i < n-1.
The sum of all the elements of nums does not exceed maxSum.
nums[index] is maximized.
Return nums[index] of the constructed array.

Note that abs(x) equals x if x >= 0, and -x otherwise.

 

Example 1:

Input: n = 4, index = 2,  maxSum = 6
Output: 2
Explanation: nums = [1,2,2,1] is one array that satisfies all the conditions.
There are no arrays that satisfy all the conditions and have nums[2] == 3, so 2 is the maximum nums[2].
Example 2:

Input: n = 6, index = 1,  maxSum = 10
Output: 3
 

Constraints:

1 <= n <= maxSum <= 109
0 <= index < n
'''
import unittest

from typing import *

class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def get_result(x):
            left_p = max(x - index, 1)
            left_len = x - left_p + 1
            left = (left_p + x) * left_len // 2
            
            right_p = max(x - (n - index - 1), 1)
            right_len = x - right_p + 1
            right = (right_p + x) * right_len // 2
            return left + right + (n - (left_len + right_len - 1)) - x
        
        start = 1
        end = maxSum
        while start < end:
            middle = start + (end - start) // 2
            if get_result(middle) < maxSum:
                start = middle + 1
            elif get_result(middle) > maxSum:
                end = middle - 1
            else:
                return middle
        return start if get_result(start) <= maxSum else start - 1

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((4, 2, 6), 2),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maxValue(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()