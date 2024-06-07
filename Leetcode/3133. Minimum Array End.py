'''
You are given two integers n and x. You have to construct an array of positive integers nums of size n where for every 0 <= i < n - 1, nums[i + 1] is greater than nums[i], and the result of the bitwise AND operation between all elements of nums is x.

Return the minimum possible value of nums[n - 1].

 

Example 1:

Input: n = 3, x = 4

Output: 6

Explanation:

nums can be [4,5,6] and its last element is 6.

Example 2:

Input: n = 2, x = 7

Output: 15

Explanation:

nums can be [7,15] and its last element is 15.

 

Constraints:

1 <= n, x <= 108
'''
from typing import *
import unittest


class Solution:
    def minEnd(self, n: int, x: int) -> int:
        res = list(32 * '0' + bin(n-1)[2:])[::-1]
        count = 0
        while x:
            if x % 2:
                res.insert(count, '1')
            x //= 2
            count += 1
        return int(''.join(res[::-1]), 2)


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((3, 4), 6),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minEnd(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()