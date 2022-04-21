'''
You are playing a game that contains multiple characters, and each of the characters has two main properties: attack and defense. You are given a 2D integer array properties where properties[i] = [attacki, defensei] represents the properties of the ith character in the game.

A character is said to be weak if any other character has both attack and defense levels strictly greater than this character's attack and defense levels. More formally, a character i is said to be weak if there exists another character j where attackj > attacki and defensej > defensei.

Return the number of weak characters.

 

Example 1:

Input: properties = [[5,5],[6,3],[3,6]]
Output: 0
Explanation: No character has strictly greater attack and defense than the other.
Example 2:

Input: properties = [[2,2],[3,3]]
Output: 1
Explanation: The first character is weak because the second character has a strictly greater attack and defense.
Example 3:

Input: properties = [[1,5],[10,4],[4,3]]
Output: 1
Explanation: The third character is weak because the second character has a strictly greater attack and defense.
 

Constraints:

2 <= properties.length <= 105
properties[i].length == 2
1 <= attacki, defensei <= 105
'''
from typing import *

import unittest
    
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (x[0], -x[1]))
        max_v = 0
        res = 0
        for i in range(len(properties) - 1, -1, -1):
            if properties[i][1] < max_v:
                res += 1
            max_v = max(properties[i][1], max_v)
        return res
        
        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([[1,5],[10,4],[4,3]],),1),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().numberOfWeakCharacters(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()