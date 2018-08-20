'''
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true 
Explanation: 20 = 1
Example 2:

Input: 16
Output: true
Explanation: 24 = 16
Example 3:

Input: 218
Output: false
'''
import unittest

class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # if n == 1:
        #     return True
        # if n == 0:
        #     return False

        # if n % 2 > 0:
        #     return False
        # else:
        #     return self.isPowerOfTwo(n/2)
        # ---------------------------------
        if n == 0:
            return False
        while n:
            if n == 1:
                return True
            if n & 1:
                return False
            else:
                n >>= 1
        return True


class TestSolution(unittest.TestCase):
    
    def test_isPowerOfTwo(self):
        examples = (
            (1, True),
            (16, True),
            (218, False),
            (0, False)
        )
        for first,second in examples:
            self.assert_function(first, second)
        
    def assert_function(self, first, second):
        self.assertEqual(Solution().isPowerOfTwo(first), second)

unittest.main()