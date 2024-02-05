'''
You are given a 2D integer array stockPrices where stockPrices[i] = [dayi, pricei] indicates the price of the stock on day dayi is pricei. A line chart is created from the array by plotting the points on an XY plane with the X-axis representing the day and the Y-axis representing the price and connecting adjacent points. One such example is shown below:


Return the minimum number of lines needed to represent the line chart.



Example 1:


Input: stockPrices = [[1,7],[2,6],[3,5],[4,4],[5,4],[6,3],[7,2],[8,1]]
Output: 3
Explanation:
The diagram above represents the input, with the X-axis representing the day and Y-axis representing the price.
The following 3 lines can be drawn to represent the line chart:
- Line 1 (in red) from (1,7) to (4,4) passing through (1,7), (2,6), (3,5), and (4,4).
- Line 2 (in blue) from (4,4) to (5,4).
- Line 3 (in green) from (5,4) to (8,1) passing through (5,4), (6,3), (7,2), and (8,1).
It can be shown that it is not possible to represent the line chart using less than 3 lines.
Example 2:


Input: stockPrices = [[3,4],[1,2],[7,8],[2,3]]
Output: 1
Explanation:
As shown in the diagram above, the line chart can be represented with a single line.


Constraints:

1 <= stockPrices.length <= 105
stockPrices[i].length == 2
1 <= dayi, pricei <= 109
All dayi are distinct.
'''
import unittest

from typing import *


class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        stockPrices.sort()
        res = 0
        start_day = stockPrices[0][0]
        start_price = stockPrices[0][1]
        previous_day = None
        previous_price = None

        for day, price in stockPrices[1:]:
            if previous_day is None:
                previous_day = day
                previous_price = price
                res += 1
            else:
                if (previous_day - start_day) * (price - previous_price) != (previous_price - start_price) * (day - previous_day):
                    res += 1
                    start_day = previous_day
                    start_price = previous_price
                previous_day = day
                previous_price = price

        return res



class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([[1,1],[500000000,499999999],[1000000000,999999998]],),2),
            (([[72,98],[62,27],[32,7],[71,4],[25,19],[91,30],[52,73],[10,9],[99,71],[47,22],[19,30],[80,63],[18,15],[48,17],[77,16],[46,27],[66,87],[55,84],[65,38],[30,9],[50,42],[100,60],[75,73],[98,53],[22,80],[41,61],[37,47],[95,8],[51,81],[78,79],[57,95]],), 29),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minimumLines(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
