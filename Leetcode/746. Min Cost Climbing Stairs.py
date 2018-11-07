'''

On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].

'''
import unittest


class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # if len(cost) == 1:
        #     return 0
        # if len(cost) == 2:
        #     return min(cost[0], cost[1])
        #
        # return min(self.minCostClimbingStairs(cost[:-1]) + cost[-1], self.minCostClimbingStairs(cost[:-2]) + cost[-2])
        # ----------------------------------------
        # this is a DP problem, you can store the result to reduce the calculate time
        pre, cur = cost[0], cost[1]
        for i in range(2, len(cost)):
            pre, cur = cur, min(pre, cur) + cost[i]
        return min(pre, cur)



class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ([10, 15, 20], 15),
            ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minCostClimbingStairs(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
