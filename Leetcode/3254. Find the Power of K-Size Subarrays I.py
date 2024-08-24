'''
You are given an array of integers nums of length n and a positive integer k.

The power of an array is defined as:

Its maximum element if all of its elements are consecutive and sorted in ascending order.
-1 otherwise.
You need to find the power of all 
subarrays
 of nums of size k.

Return an integer array results of size n - k + 1, where results[i] is the power of nums[i..(i + k - 1)].

 

Example 1:

Input: nums = [1,2,3,4,3,2,5], k = 3

Output: [3,4,-1,-1,-1]

Explanation:

There are 5 subarrays of nums of size 3:

[1, 2, 3] with the maximum element 3.
[2, 3, 4] with the maximum element 4.
[3, 4, 3] whose elements are not consecutive.
[4, 3, 2] whose elements are not sorted.
[3, 2, 5] whose elements are not consecutive.
Example 2:

Input: nums = [2,2,2,2,2], k = 4

Output: [-1,-1]

Example 3:

Input: nums = [3,2,3,2,3,2], k = 2

Output: [-1,3,-1,3,-1]

 

Constraints:

1 <= n == nums.length <= 500
1 <= nums[i] <= 105
1 <= k <= n
'''
import unittest

from typing import *


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        delta = []
        count = Counter()
        left = 0
        res = []
        for right in range(1, len(nums)):
            value = nums[right] - nums[right - 1]
            delta.append(value)
            count[value] += 1
            if len(delta) > k - 1:
                left += 1
                v = delta.pop(0)
                count[v] -= 1
            if len(delta) == k - 1:
                if count[1] == len(delta):
                    res.append(nums[right])
                else:
                    res.append(-1)
        return res
            
            
            
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([3,2,3,2,3,2],2),[-1,3,-1,3,-1]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().resultsArray(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
