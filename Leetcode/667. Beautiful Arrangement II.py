'''
Given two integers n and k, construct a list answer that contains n different positive integers ranging from 1 to n and obeys the following requirement:

Suppose this list is answer = [a1, a2, a3, ... , an], then the list [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] has exactly k distinct integers.
Return the list answer. If there multiple valid answers, return any of them.



Example 1:

Input: n = 3, k = 1
Output: [1,2,3]
Explanation: The [1,2,3] has three different positive integers ranging from 1 to 3, and the [1,1] has exactly 1 distinct integer: 1
Example 2:

Input: n = 3, k = 2
Output: [1,3,2]
Explanation: The [1,3,2] has three different positive integers ranging from 1 to 3, and the [2,1] has exactly 2 distinct integers: 1 and 2.


Constraints:

1 <= k < n <= 104
'''
from typing import *

import unittest

class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        res = []
        for i in range(1,k+1):
            if i % 2 == 1:
                res.append(i//2+1)
            else:
                res.append(n+1-i//2)

        for i in range(n - k):
            if k % 2 == 1:
                res.append(k//2+2+i)
            else:
                res.append(n-k//2-i)
        return res



class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((3,1),[1,2,3]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().constructArray(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
