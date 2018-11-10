'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: 
[−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer 
overflows.
'''
import unittest

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 2**31 -1 or x < -2**31:
            return 0
        result = str(abs(x))[::-1]
        actual_result = int(result) if x > 0 else -int(result)
        if actual_result > 2**31 -1 or actual_result < -2**31:
            return 0
        return actual_result

class TestSolution(unittest.TestCase):

    def test_reverse(self):
        examples = ((0,0),
                    (123,321),
                    (-123,-321),
                    (120,21))
        for first, second in examples:
            self.enter_word(first, second)
        
    
    def enter_word(self, first, second):
        self.assertEqual(second, Solution().reverse(first))

if __name__ == '__main__':
    unittest.main()
