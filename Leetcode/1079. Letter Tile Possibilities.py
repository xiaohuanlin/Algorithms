'''
You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

 

Example 1:

Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:

Input: tiles = "AAABBC"
Output: 188
Example 3:

Input: tiles = "V"
Output: 1
 

Constraints:

1 <= tiles.length <= 7
tiles consists of uppercase English letters.
'''
from typing import *
import unittest

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        c = [0 for i in range(26)]
        for t in tiles:
            c[ord(t) - ord('A')] += 1
            
        def dfs(counts):
            total = 0
            for i in range(26):
                if counts[i] == 0:
                    continue
                counts[i] -= 1
                total += (dfs(counts) + 1)
                counts[i] += 1
            return total
            
        return dfs(c)
        


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("AAB",),8),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().numTilePossibilities(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
