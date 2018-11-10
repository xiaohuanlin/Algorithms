'''

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''
import unittest

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        if prices[0] < prices[1]:
            max_profit = prices[1] - prices[0]
        else:
            max_profit = 0
        min_price = min(prices[:2])

        for num in prices[2:]:
            max_profit = max(max_profit, num - min_price)
            min_price = min(min_price, num)
        return max_profit
        


class TestSolution(unittest.TestCase):

    def test_maxProfit(self):
        examples = (
            ([7,1,5,3,6,4], 5),
            ([7,6,4,3,1], 0),
            ([], 0)
        )
        for first,second in examples:
            self.assert_function(first, second)
        
    def assert_function(self, first, second):
        self.assertEqual(Solution().maxProfit(first), second)

unittest.main()