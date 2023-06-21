'''
You are given a positive integer n.

Let even denote the number of even indices in the binary representation of n (0-indexed) with value 1.

Let odd denote the number of odd indices in the binary representation of n (0-indexed) with value 1.

Return an integer array answer where answer = [even, odd].



Example 1:

Input: n = 17
Output: [2,0]
Explanation: The binary representation of 17 is 10001.
It contains 1 on the 0th and 4th indices.
There are 2 even and 0 odd indices.
Example 2:

Input: n = 2
Output: [0,1]
Explanation: The binary representation of 2 is 10.
It contains 1 on the 1st index.
There are 0 even and 1 odd indices.


Constraints:

1 <= n <= 1000
'''
import unittest

from typing import *


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even = 0
        odd = 0
        count = 0
        while n:
            if count % 2 == 0:
                even += (n % 2)
            else:
                odd += (n % 2)
            n //= 2
            count += 1
        return [even, odd]



class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((17,),[2,0]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().evenOddBit(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
