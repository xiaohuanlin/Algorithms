'''
The numeric value of a lowercase character is defined as its position (1-indexed) in the alphabet, so the numeric value of a is 1, the numeric value of b is 2, the numeric value of c is 3, and so on.

The numeric value of a string consisting of lowercase characters is defined as the sum of its characters' numeric values. For example, the numeric value of the string "abe" is equal to 1 + 2 + 5 = 8.

You are given two integers n and k. Return the lexicographically smallest string with length equal to n and numeric value equal to k.

Note that a string x is lexicographically smaller than string y if x comes before y in dictionary order, that is, either x is a prefix of y, or if i is the first position such that x[i] != y[i], then x[i] comes before y[i] in alphabetic order.

 

Example 1:

Input: n = 3, k = 27
Output: "aay"
Explanation: The numeric value of the string is 1 + 1 + 25 = 27, and it is the smallest string with such a value and length equal to 3.
Example 2:

Input: n = 5, k = 73
Output: "aaszz"
 

Constraints:

1 <= n <= 105
n <= k <= 26 * n
'''
from typing import *

import unittest
    
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        a_count = (n * 26 - k) // 25
        str_list = ['a' for _ in range(a_count)]
        if a_count == n:
            return ''.join(str_list)
        
        middle = k - a_count - (n - a_count - 1) * 26
        str_list.append(chr(middle - 1 + ord('a')))
        str_list.extend(['z' for _ in range(n - a_count - 1)])
        return ''.join(str_list)
        
        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((3, 27), "aay"),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().getSmallestString(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
