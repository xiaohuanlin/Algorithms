'''
There are an infinite amount of bags on a number line, one bag for each coordinate. Some of these bags contain coins.

You are given a 2D array coins, where coins[i] = [li, ri, ci] denotes that every bag from li to ri contains ci coins.

The segments that coins contain are non-overlapping.

You are also given an integer k.

Return the maximum amount of coins you can obtain by collecting k consecutive bags.

 

Example 1:

Input: coins = [[8,10,1],[1,3,2],[5,6,4]], k = 4

Output: 10

Explanation:

Selecting bags at positions [3, 4, 5, 6] gives the maximum number of coins: 2 + 0 + 4 + 4 = 10.

Example 2:

Input: coins = [[1,10,3]], k = 2

Output: 6

Explanation:

Selecting bags at positions [1, 2] gives the maximum number of coins: 3 + 3 = 6.

 

Constraints:

1 <= coins.length <= 105
1 <= k <= 109
coins[i] == [li, ri, ci]
1 <= li <= ri <= 109
1 <= ci <= 1000
The given segments are non-overlapping.
'''
import unittest

from typing import *


class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        def get_result(nums):
            nums.sort()
            left = 0
            res = 0
            cur = 0
            for right in range(len(nums)):
                cur += (nums[right][1] - nums[right][0] + 1) * nums[right][2]
                while nums[right][1] - k + 1 > nums[left][1]:
                    cur -= (nums[left][1] - nums[left][0] + 1) * nums[left][2]
                    left += 1
                part = max(0, (nums[right][1] - k + 1 - nums[left][0]) * nums[left][2])
                res = max(res, cur - part)
            return res
        return max(get_result(coins), get_result([[-r, -l, c] for l,r,c in coins]))

            
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([[8, 10, 1], [1, 3, 2], [5, 6, 4]], 4), 10),
            (([[1, 10, 3]], 2), 6),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maximumCoins(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
