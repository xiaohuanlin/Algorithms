'''
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

 

Example 1:

Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Example 2:

Input: nums = [-1]
Output: [0]
Example 3:

Input: nums = [-1,-1]
Output: [0,0]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
'''
import unittest
from typing import *

from bisect import bisect_left

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        back = []
        res = []
        for i in range(len(nums))[::-1]:
            p = bisect_left(back, nums[i])
            res.append(p)
            back.insert(p, nums[i])
        return res[::-1]

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([5,2,6,1],),[2,1,1,0]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().countSmaller(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()