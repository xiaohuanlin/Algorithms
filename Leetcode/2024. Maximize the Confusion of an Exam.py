'''
A teacher is writing a test with n true/false questions, with 'T' denoting true and 'F' denoting false. He wants to confuse the students by maximizing the number of consecutive questions with the same answer (multiple trues or multiple falses in a row).

You are given a string answerKey, where answerKey[i] is the original answer to the ith question. In addition, you are given an integer k, the maximum number of times you may perform the following operation:

Change the answer key for any question to 'T' or 'F' (i.e., set answerKey[i] to 'T' or 'F').
Return the maximum number of consecutive 'T's or 'F's in the answer key after performing the operation at most k times.

 

Example 1:

Input: answerKey = "TTFF", k = 2
Output: 4
Explanation: We can replace both the 'F's with 'T's to make answerKey = "TTTT".
There are four consecutive 'T's.
Example 2:

Input: answerKey = "TFFT", k = 1
Output: 3
Explanation: We can replace the first 'T' with an 'F' to make answerKey = "FFFT".
Alternatively, we can replace the second 'T' with an 'F' to make answerKey = "TFFF".
In both cases, there are three consecutive 'F's.
Example 3:

Input: answerKey = "TTFTTFTT", k = 1
Output: 5
Explanation: We can replace the first 'F' to make answerKey = "TTTTTFTT"
Alternatively, we can replace the second 'F' to make answerKey = "TTFTTTTT". 
In both cases, there are five consecutive 'T's.
 

Constraints:

n == answerKey.length
1 <= n <= 5 * 104
answerKey[i] is either 'T' or 'F'
1 <= k <= n
'''
from typing import *

import unittest

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        t_left = 0
        t_count = 0
        f_left = 0
        f_count = 0
        res = 0
        for right in range(len(answerKey)):
            t_count += answerKey[right] == 'T'
            f_count += answerKey[right] == 'F'

            while t_count > k:
                t_count -= answerKey[t_left] == 'T'
                t_left += 1

            while f_count > k:
                f_count -= answerKey[f_left] == 'F'
                f_left += 1

            res = max(res, right - t_left + 1)
            res = max(res, right - f_left + 1)

        return res

        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("TTFTTFTT", 1), 5),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maxConsecutiveAnswers(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()


