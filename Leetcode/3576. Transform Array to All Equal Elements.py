'''
You are given an integer array nums of size n containing only 1 and -1, and an integer k.

You can perform the following operation at most k times:

Choose an index i (0 <= i < n - 1), and multiply both nums[i] and nums[i + 1] by -1.

Note that you can choose the same index i more than once in different operations.

Return true if it is possible to make all elements of the array equal after at most k operations, and false otherwise.

 

Example 1:

Input: nums = [1,-1,1,-1,1], k = 3

Output: true

Explanation:

We can make all elements in the array equal in 2 operations as follows:

Choose index i = 1, and multiply both nums[1] and nums[2] by -1. Now nums = [1,1,-1,-1,1].
Choose index i = 2, and multiply both nums[2] and nums[3] by -1. Now nums = [1,1,1,1,1].
Example 2:

Input: nums = [-1,-1,-1,1,1,1], k = 5

Output: false

Explanation:

It is not possible to make all array elements equal in at most 5 operations.

 

Constraints:

1 <= n == nums.length <= 105
nums[i] is either -1 or 1.
1 <= k <= n
'''
import unittest
from typing import *


class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        prev_one = prev_neg = -1
        sum_one = sum_neg = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                if prev_one == -1:
                    prev_one = i
                else:
                    sum_one += (i - prev_one)
                    prev_one = -1
            else:
                if prev_neg == -1:
                    prev_neg = i
                else:
                    sum_neg += (i - prev_neg)
                    prev_neg = -1
        res = float('inf')
        if prev_neg == -1:
            res = min(res, sum_neg)
        if prev_one == -1:
            res = min(res, sum_one)
        return res <= k
        
        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,-1,1,-1,1], 3), True),
            (([-1,-1,-1,1,1,1], 5), False),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().canMakeEqual(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
