'''

Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

Example 1:
Input: 5
Output: True
Explanation:
The binary representation of 5 is: 101
Example 2:
Input: 7
Output: False
Explanation:
The binary representation of 7 is: 111.
Example 3:
Input: 11
Output: False
Explanation:
The binary representation of 11 is: 1011.
Example 4:
Input: 10
Output: True
Explanation:
The binary representation of 10 is: 1010.

'''
import unittest


class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        bin_n = bin(n)[2:]
        pre = bin_n[0]
        for n in bin_n[1:]:
            if n != pre:
                pre = n
            else:
                return False
        return True


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (5, True),
            (7, False),
            (11, False),
            (10, True)
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().hasAlternatingBits(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()