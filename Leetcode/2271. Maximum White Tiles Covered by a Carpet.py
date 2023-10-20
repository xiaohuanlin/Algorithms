'''
You are given a 2D integer array tiles where tiles[i] = [li, ri] represents that every tile j in the range li <= j <= ri is colored white.

You are also given an integer carpetLen, the length of a single carpet that can be placed anywhere.

Return the maximum number of white tiles that can be covered by the carpet.



Example 1:


Input: tiles = [[1,5],[10,11],[12,18],[20,25],[30,32]], carpetLen = 10
Output: 9
Explanation: Place the carpet starting on tile 10.
It covers 9 white tiles, so we return 9.
Note that there may be other places where the carpet covers 9 white tiles.
It can be shown that the carpet cannot cover more than 9 white tiles.
Example 2:


Input: tiles = [[10,11],[1,1]], carpetLen = 2
Output: 2
Explanation: Place the carpet starting on tile 10.
It covers 2 white tiles, so we return 2.


Constraints:

1 <= tiles.length <= 5 * 104
tiles[i].length == 2
1 <= li <= ri <= 109
1 <= carpetLen <= 109
The tiles are non-overlapping.
'''
from typing import *

import unittest


class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        s = []
        i = 0
        j = 0
        res = 0
        cover = 0
        while i < len(tiles) and res < carpetLen:
            if tiles[j][0] + carpetLen > tiles[i][1]:
                cover += (tiles[i][1] - tiles[i][0] + 1)
                res = max(res, cover)
                i += 1
            else:
                partical = max(0, tiles[j][0] + carpetLen - tiles[i][0])
                res = max(res, cover + partical)
                cover -= (tiles[j][1] - tiles[j][0] + 1)
                j += 1
        return res



class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([[3745,3757],[3663,3681],[3593,3605],[3890,3903],[3529,3539],[3684,3686],[3023,3026],[2551,2569],[3776,3789],[3243,3256],[3477,3497],[2650,2654],[2264,2266],[2582,2599],[2846,2863],[2346,2364],[3839,3842],[3926,3935],[2995,3012],[3152,3167],[4133,4134],[4048,4058],[3719,3730],[2498,2510],[2277,2295],[4117,4128],[3043,3054],[3394,3402],[3921,3924],[3500,3514],[2789,2808],[3291,3294],[2873,2881],[2760,2760],[3349,3362],[2888,2899],[3802,3822],[3540,3542],[3128,3142],[2617,2632],[3979,3994],[2780,2781],[3213,3233],[3099,3113],[3646,3651],[3956,3963],[2674,2691],[3860,3873],[3363,3370],[2727,2737],[2453,2471],[4011,4031],[3566,3577],[2705,2707],[3560,3565],[3454,3456],[3655,3660],[4100,4103],[2382,2382],[4032,4033],[2518,2531],[2739,2749],[3067,3079],[4068,4074],[2297,2312],[2489,2490],[2954,2974],[2400,2418],[3271,3272],[3628,3632],[3372,3377],[2920,2940],[3315,3330],[3417,3435],[4146,4156],[2324,2340],[2426,2435],[2373,2376],[3621,3626],[2826,2832],[3937,3949],[3178,3195],[4081,4082],[4092,4098],[3688,3698]], 1638), 822),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maximumWhiteTiles(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
