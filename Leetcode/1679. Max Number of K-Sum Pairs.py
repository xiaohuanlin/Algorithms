'''
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

 

Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= 109
'''
import unittest
from typing import *

from functools import lru_cache
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        maps = {}
        count = 0
        for n in nums:
            if k - n not in maps:
                maps[n] = maps.setdefault(n, 0) + 1
            else:
                maps[k - n] -= 1
                if maps[k - n] == 0:
                    del maps[k - n]
                count += 1
        return count

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,2,3,4],5),2),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maxOperations(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()