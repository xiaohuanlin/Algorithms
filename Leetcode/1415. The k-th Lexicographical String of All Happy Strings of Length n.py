'''
A happy string is a string that:

consists only of letters of the set ['a', 'b', 'c'].
s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).
For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.

Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.

Return the kth string of this list or return an empty string if there are less than k happy strings of length n.

 

Example 1:

Input: n = 1, k = 3
Output: "c"
Explanation: The list ["a", "b", "c"] contains all happy strings of length 1. The third string is "c".
Example 2:

Input: n = 1, k = 4
Output: ""
Explanation: There are only 3 happy strings of length 1.
Example 3:

Input: n = 3, k = 9
Output: "cab"
Explanation: There are 12 different happy string of length 3 ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]. You will find the 9th string = "cab"
 

Constraints:

1 <= n <= 10
1 <= k <= 100
'''
import unittest

from typing import *

from math import ceil

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if k > 3 * 2 ** (n - 1):
            return ''
        res = []
        for i in range(n)[::-1]:
            x = ceil(k / 2**i)
            k = k % 2**i
            p = "abc"
            if i == n - 1:
                res.append(p[(x-1) % 3])
            else:
                p = p.replace(res[-1], '')
                res.append(p[(x-1) % 2])
        return ''.join(res)



class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((3, 9), "cab"),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().getHappyString(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
