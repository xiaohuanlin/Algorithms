'''
You are given an integer array nums and an integer k. Append k unique positive integers that do not appear in nums to nums such that the resulting total sum is minimum.

Return the sum of the k integers appended to nums.



Example 1:

Input: nums = [1,4,25,10,25], k = 2
Output: 5
Explanation: The two unique positive integers that do not appear in nums which we append are 2 and 3.
The resulting sum of nums is 1 + 4 + 25 + 10 + 25 + 2 + 3 = 70, which is the minimum.
The sum of the two integers appended is 2 + 3 = 5, so we return 5.
Example 2:

Input: nums = [5,6], k = 6
Output: 25
Explanation: The six unique positive integers that do not appear in nums which we append are 1, 2, 3, 4, 7, and 8.
The resulting sum of nums is 5 + 6 + 1 + 2 + 3 + 4 + 7 + 8 = 36, which is the minimum.
The sum of the six integers appended is 1 + 2 + 3 + 4 + 7 + 8 = 25, so we return 25.


Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= 108
'''

from typing import *
import unittest


from bisect import bisect

class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums = sorted(list(set(nums)))
        start = 0
        end = 10**9
        index = 0

        while start < end:
            middle = (start + end) // 2
            index = bisect(nums, middle)
            if middle - index >= k:
                end = middle
            else:
                start = middle + 1
        return (1 + start) * start // 2 - sum(nums[:index])


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,4,25,10,25],2,),5),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minimalKSum(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
