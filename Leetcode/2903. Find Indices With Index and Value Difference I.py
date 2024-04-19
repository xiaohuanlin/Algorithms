'''
You are given a 0-indexed integer array nums having length n, an integer indexDifference, and an integer valueDifference.

Your task is to find two indices i and j, both in the range [0, n - 1], that satisfy the following conditions:

abs(i - j) >= indexDifference, and
abs(nums[i] - nums[j]) >= valueDifference
Return an integer array answer, where answer = [i, j] if there are two such indices, and answer = [-1, -1] otherwise. If there are multiple choices for the two indices, return any of them.

Note: i and j may be equal.



Example 1:

Input: nums = [5,1,4,1], indexDifference = 2, valueDifference = 4
Output: [0,3]
Explanation: In this example, i = 0 and j = 3 can be selected.
abs(0 - 3) >= 2 and abs(nums[0] - nums[3]) >= 4.
Hence, a valid answer is [0,3].
[3,0] is also a valid answer.
Example 2:

Input: nums = [2,1], indexDifference = 0, valueDifference = 0
Output: [0,0]
Explanation: In this example, i = 0 and j = 0 can be selected.
abs(0 - 0) >= 0 and abs(nums[0] - nums[0]) >= 0.
Hence, a valid answer is [0,0].
Other valid answers are [0,1], [1,0], and [1,1].
Example 3:

Input: nums = [1,2,3], indexDifference = 2, valueDifference = 4
Output: [-1,-1]
Explanation: In this example, it can be shown that it is impossible to find two indices that satisfy both conditions.
Hence, [-1,-1] is returned.


Constraints:

1 <= n == nums.length <= 100
0 <= nums[i] <= 50
0 <= indexDifference <= 100
0 <= valueDifference <= 50
'''
import unittest

from typing import *


class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        # min_i, min_v, max_i, max_v
        endpoint_list = [[0, 0, 0, 0] for _ in range(len(nums))]
        endpoint_list[-1] = [len(nums) - 1, nums[-1], len(nums) - 1, nums[-1]]
        for i in range(len(nums)-1)[::-1]:
            endpoint_list[i] = [n for n in endpoint_list[i+1]]
            if nums[i] < endpoint_list[i+1][1]:
                endpoint_list[i][0] = i
                endpoint_list[i][1] = nums[i]
            if nums[i] > endpoint_list[i+1][3]:
                endpoint_list[i][2] = i
                endpoint_list[i][3] = nums[i]

        for i in range(len(nums)):
            if i+indexDifference < len(nums):
                min_i, min_v, max_i, max_v = endpoint_list[i+indexDifference]
                if abs(min_v - nums[i]) >= valueDifference:
                    return [min_i, i]
                if abs(max_v - nums[i]) >= valueDifference:
                    return [max_i, i]
        return [-1, -1]



class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([5,1,4,1],2,4),[3,0]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().findIndices(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
