'''
You are given a binary string s, and a 2D integer array queries where queries[i] = [firsti, secondi].

For the ith query, find the shortest substring of s whose decimal value, val, yields secondi when bitwise XORed with firsti. In other words, val ^ firsti == secondi.

The answer to the ith query is the endpoints (0-indexed) of the substring [lefti, righti] or [-1, -1] if no such substring exists. If there are multiple answers, choose the one with the minimum lefti.

Return an array ans where ans[i] = [lefti, righti] is the answer to the ith query.

A substring is a contiguous non-empty sequence of characters within a string.

 

Example 1:

Input: s = "101101", queries = [[0,5],[1,2]]
Output: [[0,2],[2,3]]
Explanation: For the first query the substring in range [0,2] is "101" which has a decimal value of 5, and 5 ^ 0 = 5, hence the answer to the first query is [0,2]. In the second query, the substring in range [2,3] is "11", and has a decimal value of 3, and 3 ^ 1 = 2. So, [2,3] is returned for the second query. 

Example 2:

Input: s = "0101", queries = [[12,8]]
Output: [[-1,-1]]
Explanation: In this example there is no substring that answers the query, hence [-1,-1] is returned.
Example 3:

Input: s = "1", queries = [[4,5]]
Output: [[0,0]]
Explanation: For this example, the substring in range [0,0] has a decimal value of 1, and 1 ^ 4 = 5. So, the answer is [0,0].
 

Constraints:

1 <= s.length <= 104
s[i] is either '0' or '1'.
1 <= queries.length <= 105
0 <= firsti, secondi <= 109
'''
from typing import *

import unittest


class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        dic = {}
        for i in range(len(s)):
            for size in range(1, 31):
                key = s[i:i+size]
                if key not in dic:
                    dic[key] = i
                else:
                    dic[key] = min(dic[key], i)
        res = []
        for first, second in queries:
            target = bin(first ^ second)[2:]
            if target not in dic:
                res.append([-1, -1])
            else:
                i = dic[target]
                res.append([i, i + len(target) - 1])
        return res
        
        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("101101", [[0,5],[1,2]]), [[0,2],[2,3]]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().substringXorQueries(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
