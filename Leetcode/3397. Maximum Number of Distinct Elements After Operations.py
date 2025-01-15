'''
You are given an integer array nums and an integer k.

You are allowed to perform the following operation on each element of the array at most once:

Add an integer in the range [-k, k] to the element.
Return the maximum possible number of distinct elements in nums after performing the operations.

 

Example 1:

Input: nums = [1,2,2,3,3,4], k = 2

Output: 6

Explanation:

nums changes to [-1, 0, 1, 2, 3, 4] after performing operations on the first four elements.

Example 2:

Input: nums = [4,4,4,4], k = 1

Output: 3

Explanation:

By adding -1 to nums[0] and 1 to nums[1], nums changes to [3, 5, 4, 4].

 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
0 <= k <= 109
'''
import unittest

from typing import *


from heapq import heappush, heappop
class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        l = []
        for n in nums:
            heappush(l, [n - k, n + k])
        
        res = 0
        current = float('-inf')
        while l:
            start, end = heappop(l)
            if end < current:
                continue
            current = max(start, current) + 1
            res += 1
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,2,2,3,3,4],2),6),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maxDistinctElements(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
