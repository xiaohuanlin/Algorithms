'''
You are given a 0-indexed integer array nums.

We say that an integer x is expressible from nums if there exist some integers 0 <= index1 < index2 < ... < indexk < nums.length for which nums[index1] | nums[index2] | ... | nums[indexk] = x. In other words, an integer is expressible if it can be written as the bitwise OR of some subsequence of nums.

Return the minimum positive non-zero integer that is not expressible from nums.

 

Example 1:

Input: nums = [2,1]
Output: 4
Explanation: 1 and 2 are already present in the array. We know that 3 is expressible, since nums[0] | nums[1] = 2 | 1 = 3. Since 4 is not expressible, we return 4.
Example 2:

Input: nums = [5,3,2]
Output: 1
Explanation: We can show that 1 is the smallest number that is not expressible.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
'''
from typing import *

import unittest


class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        target = 1
        s = set(nums)
        while True:
            if target not in s:
                return target
            target *= 2
        
        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([5,3,2],), 1),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minImpossibleOR(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
