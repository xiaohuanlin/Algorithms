'''
You are given two integer arrays nums and multipliers of size n and m respectively, where n >= m. The arrays are 1-indexed.

You begin with a score of 0. You want to perform exactly m operations. On the ith operation (1-indexed), you will:

Choose one integer x from either the start or the end of the array nums.
Add multipliers[i] * x to your score.
Remove x from the array nums.
Return the maximum score after performing m operations.

 

Example 1:

Input: nums = [1,2,3], multipliers = [3,2,1]
Output: 14
Explanation: An optimal solution is as follows:
- Choose from the end, [1,2,3], adding 3 * 3 = 9 to the score.
- Choose from the end, [1,2], adding 2 * 2 = 4 to the score.
- Choose from the end, [1], adding 1 * 1 = 1 to the score.
The total score is 9 + 4 + 1 = 14.
Example 2:

Input: nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]
Output: 102
Explanation: An optimal solution is as follows:
- Choose from the start, [-5,-3,-3,-2,7,1], adding -5 * -10 = 50 to the score.
- Choose from the start, [-3,-3,-2,7,1], adding -3 * -5 = 15 to the score.
- Choose from the start, [-3,-2,7,1], adding -3 * 3 = -9 to the score.
- Choose from the end, [-2,7,1], adding 1 * 4 = 4 to the score.
- Choose from the end, [-2,7], adding 7 * 6 = 42 to the score. 
The total score is 50 + 15 - 9 + 4 + 42 = 102.
 

Constraints:

n == nums.length
m == multipliers.length
1 <= m <= 103
m <= n <= 105
-1000 <= nums[i], multipliers[i] <= 1000
'''
from typing import *

import unittest


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        length = len(nums)
        mul_length = len(multipliers)

        dp = [[0 for _ in range(mul_length)] for _ in range(mul_length + 1)]
        
        for i in reversed(range(mul_length)):
            for j in range(i, mul_length):
                k = i + mul_length - j - 1
                dp[i][j] = max(
                    dp[i + 1][j] + nums[i] * multipliers[k],
                    dp[i][j - 1] + nums[j - mul_length + length] * multipliers[k],
                )
        
        return dp[0][-1]

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,2,3], [3]), 9),
            (([1,2,3], [3,2,1]), 14),
            (([-5,-3,-3,-2,7,1], [-10,-5,3,4,6]), 102),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maximumScore(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
