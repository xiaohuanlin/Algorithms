'''
There is a circle of red and blue tiles. You are given an array of integers colors. The color of tile i is represented by colors[i]:

colors[i] == 0 means that tile i is red.
colors[i] == 1 means that tile i is blue.
Every 3 contiguous tiles in the circle with alternating colors (the middle tile has a different color from its left and right tiles) is called an alternating group.

Return the number of alternating groups.

Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.

 

Example 1:

Input: colors = [1,1,1]

Output: 0

Explanation:



Example 2:

Input: colors = [0,1,0,0,1]

Output: 3

Explanation:



Alternating groups:



 

Constraints:

3 <= colors.length <= 100
0 <= colors[i] <= 1
'''
import unittest

from typing import *


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        res = int(colors[-2] != colors[-1] and colors[-1] != colors[0]) + int(colors[-1] != colors[0] and colors[0] != colors[1])
        for i in range(len(colors) - 2):
            if colors[i] != colors[i+1] and colors[i+1] != colors[i+2]:
                res += 1
        return res
        
        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([0,1,0,0,1],),3),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().numberOfAlternatingGroups(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
