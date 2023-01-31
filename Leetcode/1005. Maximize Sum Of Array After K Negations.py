'''
Given an integer array nums and an integer k, modify the array in the following way:

choose an index i and replace nums[i] with -nums[i].
You should apply this process exactly k times. You may choose the same index i multiple times.

Return the largest possible sum of the array after modifying it in this way.

 

Example 1:

Input: nums = [4,2,3], k = 1
Output: 5
Explanation: Choose index 1 and nums becomes [4,-2,3].
Example 2:

Input: nums = [3,-1,0,2], k = 3
Output: 6
Explanation: Choose indices (1, 2, 2) and nums becomes [3,1,0,2].
Example 3:

Input: nums = [2,-3,-1,5,-4], k = 2
Output: 13
Explanation: Choose indices (1, 4) and nums becomes [2,3,-1,5,4].
 

Constraints:

1 <= nums.length <= 104
-100 <= nums[i] <= 100
1 <= k <= 104
'''

from typing import *
import unittest


from heapq import heappush, heappop
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        q = []
        min_v = float('inf')
        s = 0

        for n in nums:
            if n < 0:
                heappush(q, n)
            min_v = min(min_v, abs(n))
            s += n
            
        q_len = len(q)
        for _ in range(min(len(q), k)):
            s -= 2 * heappop(q)
        
        if k > q_len and (k - q_len) % 2 == 1:
            s -= 2 * min_v
        return s
        
        

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([2,-3,-1,5,-4], 2), 13),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().largestSumAfterKNegations(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()