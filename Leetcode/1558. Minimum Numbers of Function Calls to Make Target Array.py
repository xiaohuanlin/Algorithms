'''
You are given an integer array nums. You have an integer array arr of the same length with all values set to 0 initially. You also have the following modify function:


You want to use the modify function to covert arr to nums using the minimum number of calls.

Return the minimum number of function calls to make nums from arr.

The test cases are generated so that the answer fits in a 32-bit signed integer.



Example 1:

Input: nums = [1,5]
Output: 5
Explanation: Increment by 1 (second element): [0, 0] to get [0, 1] (1 operation).
Double all the elements: [0, 1] -> [0, 2] -> [0, 4] (2 operations).
Increment by 1 (both elements)  [0, 4] -> [1, 4] -> [1, 5] (2 operations).
Total of operations: 1 + 2 + 2 = 5.
Example 2:

Input: nums = [2,2]
Output: 3
Explanation: Increment by 1 (both elements) [0, 0] -> [0, 1] -> [1, 1] (2 operations).
Double all the elements: [1, 1] -> [2, 2] (1 operation).
Total of operations: 2 + 1 = 3.
Example 3:

Input: nums = [4,2,5]
Output: 6
Explanation: (initial)[0,0,0] -> [1,0,0] -> [1,0,1] -> [2,0,2] -> [2,1,2] -> [4,2,4] -> [4,2,5](nums).


Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
'''
import unittest

from typing import *
from functools import cache

class Solution:
    def minOperations(self, nums: List[int]) -> int:

        @cache
        def counts(n):
            if n == 0:
                return 0, 0
            if n == 1:
                return 1, 0
            half_op0, half_op1 = counts(n // 2)
            if n % 2 == 0:
                return half_op0, half_op1 + 1
            return half_op0 + 1, half_op1 + 1

        res = 0
        op1_max = 0
        for n in nums:
            op0, op1 = counts(n)
            res += op0
            op1_max = max(op1_max, op1)
        return res + op1_max


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([4,2,5],), 6),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minOperations(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
