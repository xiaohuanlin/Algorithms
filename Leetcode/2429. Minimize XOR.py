'''
Given two positive integers num1 and num2, find the positive integer x such that:

x has the same number of set bits as num2, and
The value x XOR num1 is minimal.
Note that XOR is the bitwise XOR operation.

Return the integer x. The test cases are generated such that x is uniquely determined.

The number of set bits of an integer is the number of 1's in its binary representation.



Example 1:

Input: num1 = 3, num2 = 5
Output: 3
Explanation:
The binary representations of num1 and num2 are 0011 and 0101, respectively.
The integer 3 has the same number of set bits as num2, and the value 3 XOR 3 = 0 is minimal.
Example 2:

Input: num1 = 1, num2 = 12
Output: 3
Explanation:
The binary representations of num1 and num2 are 0001 and 1100, respectively.
The integer 3 has the same number of set bits as num2, and the value 3 XOR 1 = 2 is minimal.


Constraints:

1 <= num1, num2 <= 109
'''
import unittest

from typing import *

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        def get_one(num):
            pos = 0
            res = []
            while num:
                if num % 2 == 1:
                    res.append(pos)
                num //= 2
                pos += 1
            return res[::-1]

        one_num2 = get_one(num2)
        one_num1 = get_one(num1)

        if len(one_num1) >= len(one_num2):
            # put one into left part
            res = 0
            for n in one_num1[:len(one_num2)]:
                res |= (1 << n)
            return res
        else:
            # remaining will be inserted into the gaps between neighbors
            remain = len(one_num2) - len(one_num1)
            res = 0
            for i in range(32):
                if i in one_num1:
                    res |= (1 << i)
                else:
                    if remain > 0:
                        res |= (1 << i)
                        remain -= 1
            return res

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((3,5),3),
            ((65,84),67),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minimizeXor(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
