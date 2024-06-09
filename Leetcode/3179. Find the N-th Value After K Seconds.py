'''
You are given two integers n and k.

Initially, you start with an array a of n integers where a[i] = 1 for all 0 <= i <= n - 1. After each second, you simultaneously update each element to be the sum of all its preceding elements plus the element itself. For example, after one second, a[0] remains the same, a[1] becomes a[0] + a[1], a[2] becomes a[0] + a[1] + a[2], and so on.

Return the value of a[n - 1] after k seconds.

Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: n = 4, k = 5

Output: 56

Explanation:

Second	State After
0	[1,1,1,1]
1	[1,2,3,4]
2	[1,3,6,10]
3	[1,4,10,20]
4	[1,5,15,35]
5	[1,6,21,56]
Example 2:

Input: n = 5, k = 3

Output: 35

Explanation:

Second	State After
0	[1,1,1,1,1]
1	[1,2,3,4,5]
2	[1,3,6,10,15]
3	[1,4,10,20,35]
 

Constraints:

1 <= n, k <= 1000
'''
from typing import *
import unittest


class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        pre = [1 for _ in range(n+1)]
        mod = int(1e9 + 7)
        for _ in range(k):
            cur = [0 for _ in range(n+1)]
            for i in range(1, len(cur)):
                cur[i] = cur[i-1] + pre[i]
                cur[i] %= mod
            pre = cur
        return pre[-1]
        


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((4, 5), 56),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().valueAfterKSeconds(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()