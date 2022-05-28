'''
You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.

You can swap the characters at any pair of indices in the given pairs any number of times.

Return the lexicographically smallest string that s can be changed to after using the swaps.

 

Example 1:

Input: s = "dcab", pairs = [[0,3],[1,2]]
Output: "bacd"
Explaination: 
Swap s[0] and s[3], s = "bcad"
Swap s[1] and s[2], s = "bacd"
Example 2:

Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
Output: "abcd"
Explaination: 
Swap s[0] and s[3], s = "bcad"
Swap s[0] and s[2], s = "acbd"
Swap s[1] and s[2], s = "abcd"
Example 3:

Input: s = "cba", pairs = [[0,1],[1,2]]
Output: "abc"
Explaination: 
Swap s[0] and s[1], s = "bca"
Swap s[1] and s[2], s = "bac"
Swap s[0] and s[1], s = "abc"
 

Constraints:

1 <= s.length <= 10^5
0 <= pairs.length <= 10^5
0 <= pairs[i][0], pairs[i][1] < s.length
s only contains lower case English letters.
'''
import unittest
from typing import *

from bisect import bisect_left

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        graph = {}
        for u, v in pairs:
            graph.setdefault(u, []).append(v)
            graph.setdefault(v, []).append(u)
        
        def dfs(x, visit):
            if x in visit:
                return
            
            visit.add(x)
            for v in graph.setdefault(x, []):
                dfs(v, visit)
        
        visited = set()
        res = [s[i] for i in range(len(s))]
        for i in range(len(s)):
            if i not in visited:
                origin = set()
                dfs(i, origin)
                visited |= origin
                chars = sorted([s[i] for i in origin])
                for i, n in enumerate(sorted(origin)):
                    res[n] = chars[i]
        return "".join(res)

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("dcab", [[0,3],[1,2],[0,2]]), "abcd"),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().smallestStringWithSwaps(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()