'''
There are several consecutive houses along a street, each of which has some money inside. There is also a robber, who wants to steal money from the homes, but he refuses to steal from adjacent homes.

The capability of the robber is the maximum amount of money he steals from one house of all the houses he robbed.

You are given an integer array nums representing how much money is stashed in each house. More formally, the ith house from the left has nums[i] dollars.

You are also given an integer k, representing the minimum number of houses the robber will steal from. It is always possible to steal at least k houses.

Return the minimum capability of the robber out of all the possible ways to steal at least k houses.

 

Example 1:

Input: nums = [2,3,5,9], k = 2
Output: 5
Explanation: 
There are three ways to rob at least 2 houses:
- Rob the houses at indices 0 and 2. Capability is max(nums[0], nums[2]) = 5.
- Rob the houses at indices 0 and 3. Capability is max(nums[0], nums[3]) = 9.
- Rob the houses at indices 1 and 3. Capability is max(nums[1], nums[3]) = 9.
Therefore, we return min(5, 9, 9) = 5.
Example 2:

Input: nums = [2,7,9,3,1], k = 2
Output: 2
Explanation: There are 7 ways to rob the houses. The way which leads to minimum capability is to rob the house at index 0 and 4. Return max(nums[0], nums[4]) = 2.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= (nums.length + 1)/2
'''
import unittest

from typing import *

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def is_ok(n):
            s = 0
            res = 0 
            for i in range(len(nums)):
                if n >= nums[i] and i >= s:
                    s = i + 2
                    res += 1
            return res >= k

        start = 0
        end = max(nums)
        while start < end:
            middle = start + (end - start) // 2
            if is_ok(middle):
                end = middle
            else:
                start = middle + 1
        return start

        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([2,7,9,3,1],2),2),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minCapability(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
