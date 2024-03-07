'''
You are given an integer num. You know that Bob will sneakily remap one of the 10 possible digits (0 to 9) to another digit.

Return the difference between the maximum and minimum values Bob can make by remapping exactly one digit in num.

Notes:

When Bob remaps a digit d1 to another digit d2, Bob replaces all occurrences of d1 in num with d2.
Bob can remap a digit to itself, in which case num does not change.
Bob can remap different digits for obtaining minimum and maximum values respectively.
The resulting number after remapping can contain leading zeroes.
 

Example 1:

Input: num = 11891
Output: 99009
Explanation: 
To achieve the maximum value, Bob can remap the digit 1 to the digit 9 to yield 99899.
To achieve the minimum value, Bob can remap the digit 1 to the digit 0, yielding 890.
The difference between these two numbers is 99009.
Example 2:

Input: num = 90
Output: 99
Explanation:
The maximum value that can be returned by the function is 99 (if 0 is replaced by 9) and the minimum value that can be returned by the function is 0 (if 9 is replaced by 0).
Thus, we return 99.
 

Constraints:

1 <= num <= 108
'''
import unittest

from typing import *


class Solution:
    def minMaxDifference(self, num: int) -> int:
        min_v = float('inf')
        max_v = float('-inf')

        def change(n, to):
            return int(str(num).replace(str(n), str(to)))
            
        for i in range(10):
            min_v = min(min_v, change(i, 0))
            max_v = max(max_v, change(i, 9))
        return max_v - min_v
                

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((11891,),99009),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minMaxDifference(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
