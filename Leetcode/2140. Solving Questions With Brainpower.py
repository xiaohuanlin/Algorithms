'''
You are given a 0-indexed 2D integer array questions where questions[i] = [pointsi, brainpoweri].

The array describes the questions of an exam, where you have to process the questions in order (i.e., starting from question 0) and make a decision whether to solve or skip each question. Solving question i will earn you pointsi points but you will be unable to solve each of the next brainpoweri questions. If you skip question i, you get to make the decision on the next question.

For example, given questions = [[3, 2], [4, 3], [4, 4], [2, 5]]:
If question 0 is solved, you will earn 3 points but you will be unable to solve questions 1 and 2.
If instead, question 0 is skipped and question 1 is solved, you will earn 4 points but you will be unable to solve questions 2 and 3.
Return the maximum points you can earn for the exam.

 

Example 1:

Input: questions = [[3,2],[4,3],[4,4],[2,5]]
Output: 5
Explanation: The maximum points can be earned by solving questions 0 and 3.
- Solve question 0: Earn 3 points, will be unable to solve the next 2 questions
- Unable to solve questions 1 and 2
- Solve question 3: Earn 2 points
Total points earned: 3 + 2 = 5. There is no other way to earn 5 or more points.
Example 2:

Input: questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]
Output: 7
Explanation: The maximum points can be earned by solving questions 1 and 4.
- Skip question 0
- Solve question 1: Earn 2 points, will be unable to solve the next 2 questions
- Unable to solve questions 2 and 3
- Solve question 4: Earn 5 points
Total points earned: 2 + 5 = 7. There is no other way to earn 7 or more points.
 

Constraints:

1 <= questions.length <= 105
questions[i].length == 2
1 <= pointsi, brainpoweri <= 105
'''

from typing import *

import unittest


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [questions[i][0] for i in range(len(questions))]
        for i in range(len(questions))[::-1]:
            right_point = questions[i][0]
            if i + questions[i][1] + 1 < len(questions):
                right_point += dp[i + questions[i][1] + 1]
            dp[i] = right_point
            if i + 1 < len(questions):
                dp[i] = max(dp[i], dp[i+1])
        return dp[0]

        
class TestSolution(unittest.TestCase):
    def test_case(self):
        examples = (
            (([[3,2],[4,3],[4,4],[2,5]],),5),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().mostPoints(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

