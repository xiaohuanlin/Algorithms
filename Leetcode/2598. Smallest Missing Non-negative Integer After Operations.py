'''
You are given a 0-indexed integer array nums and an integer value.

In one operation, you can add or subtract value from any element of nums.

For example, if nums = [1,2,3] and value = 2, you can choose to subtract value from nums[0] to make nums = [-1,2,3].
The MEX (minimum excluded) of an array is the smallest missing non-negative integer in it.

For example, the MEX of [-1,2,3] is 0 while the MEX of [1,0,3] is 2.
Return the maximum MEX of nums after applying the mentioned operation any number of times.

 

Example 1:

Input: nums = [1,-10,7,13,6,8], value = 5
Output: 4
Explanation: One can achieve this result by applying the following operations:
- Add value to nums[1] twice to make nums = [1,0,7,13,6,8]
- Subtract value from nums[2] once to make nums = [1,0,2,13,6,8]
- Subtract value from nums[3] twice to make nums = [1,0,2,3,6,8]
The MEX of nums is 4. It can be shown that 4 is the maximum MEX we can achieve.
Example 2:

Input: nums = [1,-10,7,13,6,8], value = 7
Output: 2
Explanation: One can achieve this result by applying the following operation:
- subtract value from nums[2] once to make nums = [1,-10,0,13,6,8]
The MEX of nums is 2. It can be shown that 2 is the maximum MEX we can achieve.
 

Constraints:

1 <= nums.length, value <= 105
-109 <= nums[i] <= 109
'''
import unittest

from typing import *

from collections import defaultdict
class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        remains = defaultdict(int)
        for n in nums:
            remains[n % value] += 1
        
        minv = remains[0]
        minv_idx = 0
        for i in range(value):
            if remains[i] < minv:
                minv= remains[i]
                minv_idx = i
        return minv_idx + value * remains[minv_idx]


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,-10,7,13,6,8], 7), 2),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().findSmallestInteger(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
