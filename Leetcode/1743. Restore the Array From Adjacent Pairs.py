'''
There is an integer array nums that consists of n unique elements, but you have forgotten it. However, you do remember every pair of adjacent elements in nums.

You are given a 2D integer array adjacentPairs of size n - 1 where each adjacentPairs[i] = [ui, vi] indicates that the elements ui and vi are adjacent in nums.

It is guaranteed that every adjacent pair of elements nums[i] and nums[i+1] will exist in adjacentPairs, either as [nums[i], nums[i+1]] or [nums[i+1], nums[i]]. The pairs can appear in any order.

Return the original array nums. If there are multiple solutions, return any of them.

 

Example 1:

Input: adjacentPairs = [[2,1],[3,4],[3,2]]
Output: [1,2,3,4]
Explanation: This array has all its adjacent pairs in adjacentPairs.
Notice that adjacentPairs[i] may not be in left-to-right order.
Example 2:

Input: adjacentPairs = [[4,-2],[1,4],[-3,1]]
Output: [-2,4,1,-3]
Explanation: There can be negative numbers.
Another solution is [-3,1,4,-2], which would also be accepted.
Example 3:

Input: adjacentPairs = [[100000,-100000]]
Output: [100000,-100000]
 

Constraints:

nums.length == n
adjacentPairs.length == n - 1
adjacentPairs[i].length == 2
2 <= n <= 105
-105 <= nums[i], ui, vi <= 105
There exists some nums that has adjacentPairs as its pairs.
'''
from collections import defaultdict
from typing import *

import unittest


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        mapping = defaultdict(list) 
        points = set()

        for pair in adjacentPairs:
            mapping[pair[0]].append(pair[1])
            if len(mapping[pair[0]]) == 1:
                points.add(pair[0])
            if len(mapping[pair[0]]) == 2:
                points.remove(pair[0])
                
            mapping[pair[1]].append(pair[0])
            if len(mapping[pair[1]]) == 1:
                points.add(pair[1])
            if len(mapping[pair[1]]) == 2:
                points.remove(pair[1])
        
        start = points.pop()
        end = points.pop()
        visited = {start}
        res = [start]
        while start != end:

            for next in mapping[start]:
                if next in visited:
                    continue

                visited.add(next)
                start = next
                res.append(next)

        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ([[2,1],[3,4],[3,2]], [1,2,3,4]),
            ([[4,-2],[1,4],[-3,1]], [-3,1,4,-2]),
            ([[100000,-100000]], [100000,-100000]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().restoreArray(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
