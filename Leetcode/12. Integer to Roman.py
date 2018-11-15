'''

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: 3
Output: "III"
Example 2:

Input: 4
Output: "IV"
Example 3:

Input: 9
Output: "IX"
Example 4:

Input: 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
Example 5:

Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

'''
import unittest


class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # from collections import OrderedDict
        # answer_table = OrderedDict({
        #     (1000, float('+inf')): 'M',
        #     (900, 1000): 'CM',
        #     (500, 900): 'D',
        #     (400, 500): 'CD',
        #     (100, 400): 'C',
        #     (90, 100): 'XC',
        #     (50, 90): 'L',
        #     (40, 50): 'XL',
        #     (10, 40): 'X',
        #     (9, 10): 'IX',
        #     (5, 9): 'V',
        #     (4, 5): 'IV',
        #     (1, 4): 'I',
        # })
        # answer = ''
        # while num > 0:
        #     for value_range, char in answer_table.items():
        #         if value_range[0] <= num < value_range[1]:
        #             answer += char
        #             num -= value_range[0]
        #             break
        # return answer
        # -------------------------------------------------
        answer_tuple = ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'),
                        (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))
        answer = ''

        for value, char in answer_tuple:
            answer += char * (num // value)
            num %= value

        return answer



class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            # (40, 'XL'),
            # (3, "III"),
            (4, "IV"),
            (9, "IX"),
            (58, "LVIII"),
            (1994, "MCMXCIV")
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().intToRoman(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
