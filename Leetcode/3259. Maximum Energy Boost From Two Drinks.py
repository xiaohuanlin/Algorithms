'''
You are given two integer arrays energyDrinkA and energyDrinkB of the same length n by a futuristic sports scientist. These arrays represent the energy boosts per hour provided by two different energy drinks, A and B, respectively.

You want to maximize your total energy boost by drinking one energy drink per hour. However, if you want to switch from consuming one energy drink to the other, you need to wait for one hour to cleanse your system (meaning you won't get any energy boost in that hour).

Return the maximum total energy boost you can gain in the next n hours.

Note that you can start consuming either of the two energy drinks.



Example 1:

Input: energyDrinkA = [1,3,1], energyDrinkB = [3,1,1]

Output: 5

Explanation:

To gain an energy boost of 5, drink only the energy drink A (or only B).

Example 2:

Input: energyDrinkA = [4,1,1], energyDrinkB = [1,1,3]

Output: 7

Explanation:

To gain an energy boost of 7:

Drink the energy drink A for the first hour.
Switch to the energy drink B and we lose the energy boost of the second hour.
Gain the energy boost of the drink B in the third hour.


Constraints:

n == energyDrinkA.length == energyDrinkB.length
3 <= n <= 105
1 <= energyDrinkA[i], energyDrinkB[i] <= 105
'''
import unittest

from typing import *


class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        dp = [[0 for _ in range(len(energyDrinkA))] for _ in range(2)]
        dp[0][0] = energyDrinkA[0]
        dp[1][0] = energyDrinkB[0]

        for i in range(1, len(energyDrinkA)):
            dp[0][i] = max(dp[0][i-1], (dp[1][i-2] if i -2 >= 0 else 0)) + energyDrinkA[i]
            dp[1][i] = max(dp[1][i-1], (dp[0][i-2] if i -2 >= 0 else 0)) + energyDrinkB[i]
        return max(dp[0][-1], dp[1][-1])


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,3,1], [3,1,1]), 5),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maxEnergyBoost(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
