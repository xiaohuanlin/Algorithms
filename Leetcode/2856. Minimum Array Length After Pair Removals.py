'''
Given an integer array num sorted in non-decreasing order.

You can perform the following operation any number of times:

Choose two indices, i and j, where nums[i] < nums[j].
Then, remove the elements at indices i and j from nums. The remaining elements retain their original order, and the array is re-indexed.
Return the minimum length of nums after applying the operation zero or more times.

 

Example 1:

Input: nums = [1,2,3,4]

Output: 0

Explanation:



Example 2:

Input: nums = [1,1,2,2,3,3]

Output: 0

Explanation:



Example 3:

Input: nums = [1000000000,1000000000]

Output: 2

Explanation:

Since both numbers are equal, they cannot be removed.

Example 4:

Input: nums = [2,3,4,4,4]

Output: 1

Explanation:



 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
nums is sorted in non-decreasing order.
'''
import unittest

from typing import *


class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        c = Counter(nums)
        maxv, maxc = c.most_common(1)[0]
        if maxc <= len(nums) // 2:
            return 0 if len(nums) % 2 == 0 else 1
        return maxc * 2 - len(nums)
        
        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,2,3,4],), 0),
            (([1,1,2,2,3,3],), 0),
            (([1000000000,1000000000],), 2),
            (([2,3,4,4,4],), 1),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minLengthAfterRemovals(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
