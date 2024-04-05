'''
You are given a
binary array
 nums.

We call a
subarray
 alternating if no two adjacent elements in the subarray have the same value.

Return the number of alternating subarrays in nums.



Example 1:

Input: nums = [0,1,1,1]

Output: 5

Explanation:

The following subarrays are alternating: [0], [1], [1], [1], and [0,1].

Example 2:

Input: nums = [1,0,1,0]

Output: 10

Explanation:

Every subarray of the array is alternating. There are 10 possible subarrays that we can choose.



Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
'''
import unittest

from typing import *


class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        count = 0
        res = 0
        prev = None
        for n in nums:
            if count == 0:
                count = 1
            else:
                if prev + n == 1:
                    count += 1
                else:
                    res += (1 + count) * count // 2
                    count = 1
            prev = n
        res += (1 + count) * count // 2
        return res



class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([0,1,1,1],),5),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().countAlternatingSubarrays(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
