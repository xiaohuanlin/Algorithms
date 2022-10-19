'''
You are given a 0-indexed array nums comprising of n non-negative integers.

In one operation, you must:

Choose an integer i such that 1 <= i < n and nums[i] > 0.
Decrease nums[i] by 1.
Increase nums[i - 1] by 1.
Return the minimum possible value of the maximum integer of nums after performing any number of operations.

 

Example 1:

Input: nums = [3,7,1,6]
Output: 5
Explanation:
One set of optimal operations is as follows:
1. Choose i = 1, and nums becomes [4,6,1,6].
2. Choose i = 3, and nums becomes [4,6,2,5].
3. Choose i = 1, and nums becomes [5,5,2,5].
The maximum integer of nums is 5. It can be shown that the maximum number cannot be less than 5.
Therefore, we return 5.
Example 2:

Input: nums = [10,1]
Output: 10
Explanation:
It is optimal to leave nums as is, and since 10 is the maximum value, we return 10.
 

Constraints:

n == nums.length
2 <= n <= 105
0 <= nums[i] <= 109
'''
from typing import *

import unittest

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        def suit(x):
            remain = 0
            for n in nums[::-1]:
                if n > x:
                    remain += (n - x)
                else:
                    remain -= (x - n)
                    remain = max(remain, 0)
            return remain == 0
        
        start = 0
        end = max(nums)
        
        while start < end:
            middle = (start + end) // 2
            if suit(middle):
                end = middle
            else:
                start = middle + 1
        return start
    
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([3,7,1,6],),5),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minimizeArrayValue(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
