'''
You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation some number of times.

 

Example 1:

Input: nums = [3,4,2]
Output: 6
Explanation: You can perform the following operations:
- Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
- Delete 2 to earn 2 points. nums = [].
You earn a total of 6 points.
Example 2:

Input: nums = [2,2,3,3,3,4]
Output: 9
Explanation: You can perform the following operations:
- Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
- Delete a 3 again to earn 3 points. nums = [3].
- Delete a 3 once more to earn 3 points. nums = [].
You earn a total of 9 points.
 

Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i] <= 104
'''
from typing import *

import unittest


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        dp = [0 for _ in range(10001)]
        counts = {}
        max_v = 0

        for num in nums:
            counts[num] = counts.setdefault(num, 0) + num
            max_v = max(max_v, num)

        dp[1] = counts.get(1, 0)
        for i in range(2, max_v + 1):
            dp[i] = max(dp[i - 2] + counts.get(i, 0), dp[i - 1])
        return dp[max_v]


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([2,2,2,3,4,4,6],), 20),
            (([2,3,4,6],), 12),
            (([3,4,2],), 6),
            (([2,2,3,3,3,4],), 9),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().deleteAndEarn(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
