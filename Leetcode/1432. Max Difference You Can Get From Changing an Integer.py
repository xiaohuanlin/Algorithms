'''
You are given an integer num. You will apply the following steps exactly two times:

Pick a digit x (0 <= x <= 9).
Pick another digit y (0 <= y <= 9). The digit y can be equal to x.
Replace all the occurrences of x in the decimal representation of num by y.
The new integer cannot have any leading zeros, also the new integer cannot be 0.
Let a and b be the results of applying the operations to num the first and second times, respectively.

Return the max difference between a and b.

 

Example 1:

Input: num = 555
Output: 888
Explanation: The first time pick x = 5 and y = 9 and store the new integer in a.
The second time pick x = 5 and y = 1 and store the new integer in b.
We have now a = 999 and b = 111 and max difference = 888
Example 2:

Input: num = 9
Output: 8
Explanation: The first time pick x = 9 and y = 9 and store the new integer in a.
The second time pick x = 9 and y = 1 and store the new integer in b.
We have now a = 9 and b = 1 and max difference = 8
 

Constraints:

1 <= num <= 108
'''
from typing import *

import unittest

class Solution:
    def maxDiff(self, num: int) -> int:
        nums = []
        while num:
            nums.append(num % 10)
            num //= 10
        
        min_v = None
        min_res = 0
        min_one = True
        max_v = None
        max_res = 0
        for i, n in enumerate(nums[::-1]):
            if min_v == None:
                if i == 0:
                    if n != 1:
                        min_v = n
                elif n != 0 and n != 1:
                    min_v = n
                    min_one = False
                min_res = min_res * 10 + (min_one if min_v else n)
            else:
                if n == min_v:
                    min_res = min_res * 10 + min_one
                else:
                    min_res = min_res * 10 + n

            if max_v == None:
                if n != 9:
                    max_v = n
                max_res = max_res * 10 + 9
            else:
                if n == max_v:
                    max_res = max_res * 10 + 9
                else:
                    max_res = max_res * 10 + n
        return max_res - min_res

        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((555,),888),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maxDiff(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()


