'''
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
'''
import unittest

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # if x == 1:
        #     return 1

        # start = 0
        # end = x
        # esti_sqrt_x = x//2
        # while True:

        #     esti_sqrt_x = (start+end)//2

        #     if esti_sqrt_x**2 == x:
        #         return esti_sqrt_x

        #     elif esti_sqrt_x**2 > x:
        #         end = esti_sqrt_x

        #     else:
        #         start = esti_sqrt_x
            
        #     if esti_sqrt_x == (start+end)//2:
        #         return esti_sqrt_x
        
        # use Newton method

        if x == 0:
            return 0
            
        def Newton_method(x_):
            new_x_ = x_/2 + x/2/x_
            print(x_, new_x_)
            if int(new_x_) == int(x_):
                return int(new_x_)
            return Newton_method(new_x_)

        return Newton_method(x)



class TestSolution(unittest.TestCase):

    def test_mySqrt(self):
        examples = ((4, 2),
                    (8, 2),
                    (0, 0),
                    (1, 1)
        )
        for first,second in examples:
            self.assert_function(first, second)
        
    def assert_function(self, first, second):
        self.assertEqual(Solution().mySqrt(first), second)

unittest.main()