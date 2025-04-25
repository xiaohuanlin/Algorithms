'''
Convert a non-negative integer num to its English words representation.



Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"


Constraints:

0 <= num <= 231 - 1
'''
import unittest

from typing import *


class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        names = ['', ' Thousand ', ' Million ', ' Billion ']
        def convert(n):
            first = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
                    'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen',
                    'Nineteen']
            second = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
            res = []
            if n >= 100:
                res.append(first[n // 100] + ' Hundred')
                n = n % 100
            if n < 20:
                if first[n]:
                    res.append(first[n])
            else:
                w = second[n // 10 - 2]
                if first[n%10]:
                    w += ' ' + first[n % 10]
                res.append(w)
            return ' '.join(res)

        s = ''
        c = 0
        while num:
            n = num % 1000
            if n > 0:
                s = convert(n) + names[c] + s
            c += 1
            num //= 1000
        return s.strip()


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((12345,),"Twelve Thousand Three Hundred Forty Five"),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().numberToWords(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

