'''
You are given an array maximumHeight, where maximumHeight[i] denotes the maximum height the ith tower can be assigned.

Your task is to assign a height to each tower so that:

The height of the ith tower is a positive integer and does not exceed maximumHeight[i].
No two towers have the same height.
Return the maximum possible total sum of the tower heights. If it's not possible to assign heights, return -1.



Example 1:

Input: maximumHeight = [2,3,4,3]

Output: 10

Explanation:

We can assign heights in the following way: [1, 2, 4, 3].

Example 2:

Input: maximumHeight = [15,10]

Output: 25

Explanation:

We can assign heights in the following way: [15, 10].

Example 3:

Input: maximumHeight = [2,2,1]

Output: -1

Explanation:

It's impossible to assign positive heights to each index so that no two towers have the same height.



Constraints:

1 <= maximumHeight.length <= 105
1 <= maximumHeight[i] <= 109
'''
import unittest

from typing import *


class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort()
        res = 0
        prev = float('inf')
        for v in maximumHeight[::-1]:
            prev = min(v, prev)
            if prev <= 0:
                return -1
            res += prev
            prev -= 1

        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([2,3,4,3],),10),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maximumTotalSum(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
