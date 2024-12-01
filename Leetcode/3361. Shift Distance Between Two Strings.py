'''
You are given two strings s and t of the same length, and two integer arrays nextCost and previousCost.

In one operation, you can pick any index i of s, and perform either one of the following actions:

Shift s[i] to the next letter in the alphabet. If s[i] == 'z', you should replace it with 'a'. This operation costs nextCost[j] where j is the index of s[i] in the alphabet.
Shift s[i] to the previous letter in the alphabet. If s[i] == 'a', you should replace it with 'z'. This operation costs previousCost[j] where j is the index of s[i] in the alphabet.
The shift distance is the minimum total cost of operations required to transform s into t.

Return the shift distance from s to t.

 

Example 1:

Input: s = "abab", t = "baba", nextCost = [100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], previousCost = [1,100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

Output: 2

Explanation:

We choose index i = 0 and shift s[0] 25 times to the previous character for a total cost of 1.
We choose index i = 1 and shift s[1] 25 times to the next character for a total cost of 0.
We choose index i = 2 and shift s[2] 25 times to the previous character for a total cost of 1.
We choose index i = 3 and shift s[3] 25 times to the next character for a total cost of 0.
Example 2:

Input: s = "leet", t = "code", nextCost = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], previousCost = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

Output: 31

Explanation:

We choose index i = 0 and shift s[0] 9 times to the previous character for a total cost of 9.
We choose index i = 1 and shift s[1] 10 times to the next character for a total cost of 10.
We choose index i = 2 and shift s[2] 1 time to the previous character for a total cost of 1.
We choose index i = 3 and shift s[3] 11 times to the next character for a total cost of 11.
 

Constraints:

1 <= s.length == t.length <= 105
s and t consist only of lowercase English letters.
nextCost.length == previousCost.length == 26
0 <= nextCost[i], previousCost[i] <= 109
'''
import unittest

from typing import *


class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        next_presum = [0 for _ in range(len(nextCost) + 1)]
        prev_presum = [0 for _ in range(len(previousCost) + 1)]
        for i in range(1, len(next_presum)):
            next_presum[i] = next_presum[i-1] + nextCost[i-1] # [a->a, a->b, a->c, ...]
        for i in range(len(prev_presum) - 1):
            prev_presum[i] = prev_presum[i-1] + previousCost[i] # [a->z, b->z, c->z, ..., z->z]

        total = 0
        for i in range(len(s)):
            s_index = ord(s[i]) - ord('a')
            t_index = ord(t[i]) - ord('a')
            next_cost = (next_presum[t_index] - next_presum[s_index]) if t_index >= s_index else (next_presum[-1] - next_presum[s_index] + next_presum[t_index])
            prev_cost = (prev_presum[s_index] - prev_presum[t_index]) if t_index <= s_index else (prev_presum[-2] - prev_presum[t_index] + prev_presum[s_index])
            min_v = min(next_cost, prev_cost)
            total += min_v
        return total


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("abab", "baba", [100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [1,100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]), 2),
            (("leet", "code", [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]), 31),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().shiftDistance(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
