'''
You are the manager of a basketball team. For the upcoming tournament, you want to choose the team with the highest overall score. The score of the team is the sum of scores of all the players in the team.

However, the basketball team is not allowed to have conflicts. A conflict exists if a younger player has a strictly higher score than an older player. A conflict does not occur between players of the same age.

Given two lists, scores and ages, where each scores[i] and ages[i] represents the score and age of the ith player, respectively, return the highest overall score of all possible basketball teams.

 

Example 1:

Input: scores = [1,3,5,10,15], ages = [1,2,3,4,5]
Output: 34
Explanation: You can choose all the players.
Example 2:

Input: scores = [4,5,6,5], ages = [2,1,2,1]
Output: 16
Explanation: It is best to choose the last 3 players. Notice that you are allowed to choose multiple people of the same age.
Example 3:

Input: scores = [1,2,3,5], ages = [8,9,10,1]
Output: 6
Explanation: It is best to choose the first 3 players. 
 

Constraints:

1 <= scores.length, ages.length <= 1000
scores.length == ages.length
1 <= scores[i] <= 106
1 <= ages[i] <= 1000
'''
import unittest

from typing import *

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        l = list(zip(ages, scores))
        l.sort()
        
        dp = [l[i][1] for i in range(len(ages))]
        res = 0
        for i in range(len(ages)):
            for j in range(i):
                if l[i][1] >= l[j][1]:
                    dp[i] = max(dp[i], dp[j] + l[i][1])
            res = max(res, dp[i])
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,3,5,10,15], [1,2,3,4,5]), 34),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().bestTeamScore(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
