'''
There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

You are given a string dominoes representing the initial state where:

dominoes[i] = 'L', if the ith domino has been pushed to the left,
dominoes[i] = 'R', if the ith domino has been pushed to the right, and
dominoes[i] = '.', if the ith domino has not been pushed.
Return a string representing the final state.

 

Example 1:

Input: dominoes = "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.
Example 2:


Input: dominoes = ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."
 

Constraints:

n == dominoes.length
1 <= n <= 105
dominoes[i] is either 'L', 'R', or '.'.
'''
from typing import *

import unittest
from pprint import pprint
from collections import defaultdict


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        prev_index = 0
        prev = None
        res = ['.' for _ in range(len(dominoes))]

        for i, cur in enumerate(dominoes):
            if cur == 'R':
                if prev == 'R':
                    for k in range(prev_index, i + 1):
                        res[k] = 'R'
                prev_index = i
                prev = cur
            elif cur == 'L':
                if prev == 'R':
                    right = i
                    while prev_index < right:
                        res[prev_index] = 'R'
                        res[right] = 'L'
                        prev_index += 1
                        right -= 1
                elif prev == 'L' or prev is None:
                    for k in range(prev_index, i + 1):
                        res[k] = 'L'

                prev_index = i
                prev = cur

        if prev == 'R':
            for k in range(prev_index, len(dominoes)):
                res[k] = 'R'
            
        return ''.join(res)

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("RR.L",), "RR.L"),
            (("LLL...L..R..R.RR..L",), "LLLLLLL..RRRRRRRRLL"),
            ((".L.R...LR..L..",), "LL.RR.LLRRLL.."),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().pushDominoes(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
