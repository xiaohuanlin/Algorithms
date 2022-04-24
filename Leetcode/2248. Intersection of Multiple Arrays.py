'''
Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers, return the list of integers that are present in each array of nums sorted in ascending order.
 

Example 1:

Input: nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
Output: [3,4]
Explanation: 
The only integers present in each of nums[0] = [3,1,2,4,5], nums[1] = [1,2,3,4], and nums[2] = [3,4,5,6] are 3 and 4, so we return [3,4].
Example 2:

Input: nums = [[1,2,3],[4,5,6]]
Output: []
Explanation: 
There does not exist any integer present both in nums[0] and nums[1], so we return an empty list [].
 

Constraints:

1 <= nums.length <= 1000
1 <= sum(nums[i].length) <= 1000
1 <= nums[i][j] <= 1000
All the values of nums[i] are unique.
'''
from typing import *
import unittest

from collections import Counter
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        l = Counter([a for num in nums for a in num])
        res = []
        for k, v in l.items():
            if v == len(nums):
                res.append(k)
        return sorted(res)
        


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([[3,1,2,4,5],[1,2,3,4],[3,4,5,6]],), [3,4]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().intersection(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
