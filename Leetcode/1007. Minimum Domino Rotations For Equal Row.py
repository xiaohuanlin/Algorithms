'''
In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

If it cannot be done, return -1.

 

Example 1:


Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
Example 2:

Input: tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
Output: -1
Explanation: 
In this case, it is not possible to rotate the dominoes to make one row of values equal.
 

Constraints:

2 <= tops.length <= 2 * 104
bottoms.length == tops.length
1 <= tops[i], bottoms[i] <= 6
'''
import unittest

from typing import *
from collections import OrderedDict

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        store = [[0, 0, 0] for _ in range(7)]
        for i in range(len(tops)):
            if tops[i] != bottoms[i]:
                store[tops[i]][0] += 1
                store[bottoms[i]][1] += 1
            else:
                store[tops[i]][2] += 1
                
        res = float('inf')
        for i in range(1, 7):
            if store[i][0] + store[i][1] + store[i][2] == len(tops):
                swaps = min(store[i][0], store[i][1])
                res = min(swaps, res)
        return res if res != float('inf') else -1

        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([3,5,1,2,3], [3,6,3,3,4]), -1),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minDominoRotations(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()


