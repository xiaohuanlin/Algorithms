'''

Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = -2, b = 3
Output: 1

'''
import unittest


class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # todo: to understand what's behind this algo
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        print(int(MAX), int(MIN), int(mask))
        while b != 0:
            # ^ get different bits and & gets double 1s, << moves carry
            # a ^ b get the answer, and mask get the carry
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        return a if a <= MAX else ~(a ^ mask)


class TestSolution(unittest.TestCase):

    def test_getSum(self):
        examples = (
            ((1, 2), 3),
            ((8, 4), 12),
            ((-2, 3), 1),
            ((-12, -30), -42)
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().getSum(*first), second, msg="first: {}; second: {}".format(first, second))


unittest.main()