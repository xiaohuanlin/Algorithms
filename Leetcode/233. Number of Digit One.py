'''
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

 

Example 1:

Input: n = 13
Output: 6
Example 2:

Input: n = 0
Output: 0
 

Constraints:

0 <= n <= 109
'''
import unittest

from typing import *


class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        i = 0
        visited = set()
        value = 0
        while 0 <= i < len(instructions) and i not in visited:
            visited.add(i)
            if instructions[i] == 'add':
                value += values[i]
                i += 1
            else:
                i += values[i]
        return value


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (())
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().calculateScore(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
