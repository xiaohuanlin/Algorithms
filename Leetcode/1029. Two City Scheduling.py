'''
A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.

Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.

 

Example 1:

Input: costs = [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
Example 2:

Input: costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
Output: 1859
Example 3:

Input: costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
Output: 3086
 

Constraints:

2 * n == costs.length
2 <= costs.length <= 100
costs.length is even.
1 <= aCosti, bCosti <= 1000
'''

import enum
from typing import *

import unittest



class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        deltas = []
        for i, cost in enumerate(costs):
            deltas.append((cost[0] - cost[1], i))

        deltas.sort()
        res = 0
        for i, delta in enumerate(deltas):
            if i < len(costs) // 2:
                res += costs[delta[1]][0]
            else:
                res += costs[delta[1]][1]
            
        return res


    
class TestSolution(unittest.TestCase):
    def test_case(self):
        examples = (
            (([[10,20],[30,200],[400,50],[30,20]], ), 110),
            (([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]], ), 1859),
            (([[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]], ), 3086),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().twoCitySchedCost(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

