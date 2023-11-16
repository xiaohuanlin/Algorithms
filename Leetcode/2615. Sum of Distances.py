'''
You are given a 0-indexed integer array nums. There exists an array arr of length nums.length, where arr[i] is the sum of |i - j| over all j such that nums[j] == nums[i] and j != i. If there is no such j, set arr[i] to be 0.

Return the array arr.



Example 1:

Input: nums = [1,3,1,1,2]
Output: [5,0,3,4,0]
Explanation:
When i = 0, nums[0] == nums[2] and nums[0] == nums[3]. Therefore, arr[0] = |0 - 2| + |0 - 3| = 5.
When i = 1, arr[1] = 0 because there is no other index with value 3.
When i = 2, nums[2] == nums[0] and nums[2] == nums[3]. Therefore, arr[2] = |2 - 0| + |2 - 3| = 3.
When i = 3, nums[3] == nums[0] and nums[3] == nums[2]. Therefore, arr[3] = |3 - 0| + |3 - 2| = 4.
When i = 4, arr[4] = 0 because there is no other index with value 2.

Example 2:

Input: nums = [0,5,3]
Output: [0,0,0]
Explanation: Since each element in nums is distinct, arr[i] = 0 for all i.


Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
'''

from typing import *

import unittest

from collections import defaultdict

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        maps = defaultdict(list)
        index_map = defaultdict(int)

        for i in range(len(nums)):
            index_map[i] = len(maps[nums[i]])
            maps[nums[i]].append(i)

        left_s = [0 for _ in range(len(nums))]
        left_map = defaultdict(int)
        right_s = [0 for _ in range(len(nums))]
        right_map = defaultdict(int)

        for i in range(len(nums)):
            left_s[i] = left_map[nums[i]] + i
            left_map[nums[i]] = left_s[i]

            right_s[-i-1] = right_map[nums[-i-1]] + (len(nums) - i - 1)
            right_map[nums[-i-1]] = right_s[-i-1]

        res = [0 for _ in range(len(nums))]
        for i in range(len(res)):
            index = index_map[i]
            m = maps[nums[i]]
            res[i] = ((index + 1) * m[index] - left_s[m[index]]) + (right_s[m[index]] - (len(m) - index) * m[index])

        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,3,1,1,2],), [5,0,3,4,0]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().distance(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
