'''

Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:
Input: 3
Output: False

'''
import unittest


class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        a = int(c ** 0.5)
        while a >= 0:
            b = (c - a ** 2) ** 0.5
            # print(a, b)
            if int(b) == b:
                return True
            a -= 1
        return False



class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (5, True),
            (3, False),
            (0, True),
            (25, True)
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().judgeSquareSum(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
