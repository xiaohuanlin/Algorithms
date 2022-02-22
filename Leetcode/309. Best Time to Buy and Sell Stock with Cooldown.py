'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
Example 2:

Input: prices = [1]
Output: 0
 

Constraints:

1 <= prices.length <= 5000
0 <= prices[i] <= 1000
'''
from typing import *

import unittest
from pprint import pprint


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0 for _ in range(len(prices))]
        max_diff = -prices[0]
        for i in range(1, len(prices)):
            prev = dp[i - 2] if i >= 2 else 0
            max_diff = max(max_diff, prev - prices[i])
            dp[i] = max(dp[i - 1], max_diff + prices[i])
        return dp[-1]


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,2,3,0,2], ), 3),
            (([3], ), 0)
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maxProfit(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
