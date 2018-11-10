'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"

'''
import unittest

class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        b_list = []
        while n > 0:
            n,b = divmod(n-1, 26)
            b_list.append(b)
        ord_a = ord('A')
        a_list = []
        
        for b in b_list[::-1]:
            char_a = chr(ord_a + b)
            a_list.append(char_a)
        return ''.join(a_list)


class TestSolution(unittest.TestCase):

    def test_convertToTitle(self):
        examples = (
            (1, "A"),
            (28, "AB"),
            (701, "ZY")
        )
        for first,second in examples:
            self.assert_function(first, second)
        
    def assert_function(self, first, second):
        self.assertEqual(Solution().convertToTitle(first), second)

unittest.main()