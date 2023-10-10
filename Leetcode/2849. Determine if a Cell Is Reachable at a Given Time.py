'''
You are given four integers sx, sy, fx, fy, and a non-negative integer t.

In an infinite 2D grid, you start at the cell (sx, sy). Each second, you must move to any of its adjacent cells.

Return true if you can reach cell (fx, fy) after exactly t seconds, or false otherwise.

A cell's adjacent cells are the 8 cells around it that share at least one corner with it. You can visit the same cell several times.



Example 1:


Input: sx = 2, sy = 4, fx = 7, fy = 7, t = 6
Output: true
Explanation: Starting at cell (2, 4), we can reach cell (7, 7) in exactly 6 seconds by going through the cells depicted in the picture above.
Example 2:


Input: sx = 3, sy = 1, fx = 7, fy = 3, t = 3
Output: false
Explanation: Starting at cell (3, 1), it takes at least 4 seconds to reach cell (7, 3) by going through the cells depicted in the picture above. Hence, we cannot reach cell (7, 3) at the third second.


Constraints:

1 <= sx, sy, fx, fy <= 109
0 <= t <= 109
'''

from typing import *

import unittest


class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        dx = abs(fx - sx)
        dy = abs(fy - sy)
        if dx == 0 and dy == 0:
            return t >= 2
        elif dx == 0:
            return t == dy or t >= dy + 2
        elif dy == 0:
            return t == dy or t >= dy + 2
        else:
            return t >= max(dx, dy)


class TestSolution(unittest.TestCase):
    def test_case(self):
        examples = (
            ((2,4,7,7,6),True),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().isReachableAtTime(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
