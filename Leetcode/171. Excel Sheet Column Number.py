'''
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701

'''
import unittest

class Solution:
    def titleToNumber(self, s):
        """
        :type n: int
        :rtype: str
        """
        sum_num = 0
        for ele in s:
            sum_num = sum_num*26 + ord(ele) - 64
        return sum_num


class TestSolution(unittest.TestCase):

    def test_titleToNumber(self):
        examples = (
            # ("A", 1),
            ("AB", 28),
            ("ZY", 701)
        )
        for first,second in examples:
            self.assert_function(first, second)
        
    def assert_function(self, first, second):
        self.assertEqual(Solution().titleToNumber(first), second)

unittest.main()