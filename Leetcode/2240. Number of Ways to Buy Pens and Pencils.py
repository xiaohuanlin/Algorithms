'''
You are given an integer total indicating the amount of money you have. You are also given two integers cost1 and cost2 indicating the price of a pen and pencil respectively. You can spend part or all of your money to buy multiple quantities (or none) of each kind of writing utensil.

Return the number of distinct ways you can buy some number of pens and pencils.

 

Example 1:

Input: total = 20, cost1 = 10, cost2 = 5
Output: 9
Explanation: The price of a pen is 10 and the price of a pencil is 5.
- If you buy 0 pens, you can buy 0, 1, 2, 3, or 4 pencils.
- If you buy 1 pen, you can buy 0, 1, or 2 pencils.
- If you buy 2 pens, you cannot buy any pencils.
The total number of ways to buy pens and pencils is 5 + 3 + 1 = 9.
Example 2:

Input: total = 5, cost1 = 10, cost2 = 10
Output: 1
Explanation: The price of both pens and pencils are 10, which cost more than total, so you cannot buy any writing utensils. Therefore, there is only 1 way: buy 0 pens and 0 pencils.
 

Constraints:

1 <= total, cost1, cost2 <= 106
'''

from typing import *

import unittest


class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        max1 = total // cost1
        max2 = total // cost2
        max_v = 0
        cost = 0
        other_cost = 0
        if max1 > max2:
            # use 2
            max_v = max2
            cost = cost2
            other_cost = cost1
        else:
            # use 1
            max_v = max1
            cost = cost1
            other_cost = cost2
            
        res = 0
        for i in range(max_v + 1):
            res += (total - i * cost) // other_cost + 1
        return res

        
class TestSolution(unittest.TestCase):
    def test_case(self):
        examples = (
            ((5,10,10),1),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().waysToBuyPensPencils(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

