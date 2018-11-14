'''

Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
Example 1:

Input: "42"
Output: 42
Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.

'''
import unittest


class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        sign = 1
        result = 0
        i = 0
        max_int = 2 ** 31 - 1
        min_int = - 2 ** 31
        str = str.lstrip(' ')

        if len(str) == 0:
            return result

        if str[0] == '+':
            sign = 1
            i += 1
        elif str[0] == '-':
            sign = -1
            i += 1

        while i < len(str) and str[i].isdigit():
            result = result * 10 + int(str[i])
            i += 1
            if result * sign > max_int:
                return max_int
            if result * sign < min_int:
                return min_int
        return result * sign


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ('', 0),
            ('+', 0),
            ('42', 42),
            ("   -42", -42),
            ("4193 with words", 4193),
            ("words and 987", 0),
            ("-91283472332", -2147483648),
            ("+-2", 0),
            ('1', 1)
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().myAtoi(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
