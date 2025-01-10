'''
You are given a string num consisting of only digits. A string of digits is called balanced if the sum of the digits at even indices is equal to the sum of digits at odd indices.

Return true if num is balanced, otherwise return false.

 

Example 1:

Input: num = "1234"

Output: false

Explanation:

The sum of digits at even indices is 1 + 3 == 4, and the sum of digits at odd indices is 2 + 4 == 6.
Since 4 is not equal to 6, num is not balanced.
Example 2:

Input: num = "24123"

Output: true

Explanation:

The sum of digits at even indices is 2 + 1 + 3 == 6, and the sum of digits at odd indices is 4 + 2 == 6.
Since both are equal the num is balanced.
 

Constraints:

2 <= num.length <= 100
num consists of digits only
'''
import unittest

from typing import *


class Solution:
    def isBalanced(self, num: str) -> bool:
        odd_sum = 0
        even_sum = 0
        for i in range(len(num)):
            if i % 2 == 0:
                even_sum += int(num[i])
            else:
                odd_sum += int(num[i])
        return odd_sum == even_sum


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("24123",),True),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().isBalanced(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
