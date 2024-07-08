'''
You are given a positive integer n.

A binary string x is valid if all 
substrings
 of x of length 2 contain at least one "1".

Return all valid strings with length n, in any order.

 

Example 1:

Input: n = 3

Output: ["010","011","101","110","111"]

Explanation:

The valid strings of length 3 are: "010", "011", "101", "110", and "111".

Example 2:

Input: n = 1

Output: ["0","1"]

Explanation:

The valid strings of length 1 are: "0" and "1".

 

Constraints:

1 <= n <= 18
'''
from typing import *
import unittest


class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = []

        def dfs(prev, remain):
            if remain == 0:
                res.append(prev)
                return
            
            if prev[-1] == '1':
                dfs(prev + '0', remain - 1)

            dfs(prev + '1', remain - 1)
        
        dfs('0', n - 1)
        dfs('1', n - 1)
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((3,), ["010","011","101","110","111"]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().validStrings(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()