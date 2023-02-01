'''
You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt. This area is in the shape of a circle with the center as the location of the bomb.

The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri]. xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the radius of its range.

You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that lie in its range. These bombs will further detonate the bombs that lie in their ranges.

Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb.



Example 1:


Input: bombs = [[2,1,3],[6,1,4]]
Output: 2
Explanation:
The above figure shows the positions and ranges of the 2 bombs.
If we detonate the left bomb, the right bomb will not be affected.
But if we detonate the right bomb, both bombs will be detonated.
So the maximum bombs that can be detonated is max(1, 2) = 2.
Example 2:


Input: bombs = [[1,1,5],[10,10,5]]
Output: 1
Explanation:
Detonating either bomb will not detonate the other bomb, so the maximum number of bombs that can be detonated is 1.
Example 3:


Input: bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
Output: 5
Explanation:
The best bomb to detonate is bomb 0 because:
- Bomb 0 detonates bombs 1 and 2. The red circle denotes the range of bomb 0.
- Bomb 2 detonates bomb 3. The blue circle denotes the range of bomb 2.
- Bomb 3 detonates bomb 4. The green circle denotes the range of bomb 3.
Thus all 5 bombs are detonated.


Constraints:

1 <= bombs.length <= 100
bombs[i].length == 3
1 <= xi, yi, ri <= 105
'''
import unittest

from typing import *

from collections import defaultdict
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i1, p1 in enumerate(bombs):
            x1, y1, r1 = p1
            for i2, p2 in enumerate(bombs):
                x2, y2, r2 = p2
                if i1 == i2:
                    continue
                dis = (x1 - x2) ** 2 + (y1 - y2) ** 2
                if dis <= r1 ** 2:
                    graph[i1].append(i2)
                if dis <= r2 ** 2:
                    graph[i2].append(i1)

        visited = set()
        def dfs(p):
            if p in visited:
                return 0
            visited.add(p)
            s = 1
            for np in graph[p]:
                s += dfs(np)
            return s

        res = 0
        for p in range(len(bombs)):
            visited = set()
            res = max(res, dfs(p))
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]],),5),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maximumDetonation(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
