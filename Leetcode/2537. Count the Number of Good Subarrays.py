'''
Given an integer array nums and an integer k, return the number of good subarrays of nums.

A subarray arr is good if it there are at least k pairs of indices (i, j) such that i < j and arr[i] == arr[j].

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1,1,1], k = 10
Output: 1
Explanation: The only good subarray is the array nums itself.
Example 2:

Input: nums = [3,1,4,3,2,2,4], k = 2
Output: 4
Explanation: There are 4 different good subarrays:
- [3,1,4,3,2,2] that has 2 pairs.
- [3,1,4,3,2,2,4] that has 3 pairs.
- [1,4,3,2,2,4] that has 2 pairs.
- [4,3,2,2,4] that has 2 pairs.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i], k <= 109
'''

from typing import *
import unittest

from collections import Counter

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        start = 0
        c = Counter()
        res = 0
        pairs = 0

        for right in range(len(nums)):
            pairs += c[nums[right]]
            c[nums[right]] += 1
            while pairs >= k:
                c[nums[start]] -= 1
                pairs -= c[nums[start]]
                start += 1
                res += (len(nums) - right)
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([3,1,4,3,2,2,4],2),4),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().countGood(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()