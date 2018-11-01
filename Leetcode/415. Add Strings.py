'''

Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

'''
import unittest


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        carry = 0
        result = []

        num1 = num1[::-1]
        num2 = num2[::-1]
        if len(num1) < len(num2):
            num1 = num1 + '0'*(len(num2)-len(num1))
        else:
            num2 = num2 + '0' * (len(num1) - len(num2))

        for x, y in zip(num1, num2):
            x, y = int(x) if x is not None else 0, int(y) if y is not None else 0
            value = (x + y + carry) % 10
            carry = (x + y + carry) // 10
            result.append(str(value))
        if carry:
            result.extend(str(carry))
        return ''.join(result[::-1])


class TestSolution(unittest.TestCase):

    def test_addStrings(self):
        examples = (
            (('9', '99'), '108'),
            (('1', '9'), '10'),
            (('19', '191'), '210'),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().addStrings(*first), second, msg="first: {}; second: {}".format(first, second))


unittest.main()