'''
You are given a
binary string
 s.

You can perform the following operation on the string any number of times:

Choose any index i from the string where i + 1 < s.length such that s[i] == '1' and s[i + 1] == '0'.
Move the character s[i] to the right until it reaches the end of the string or another '1'. For example, for s = "010010", if we choose i = 1, the resulting string will be s = "000110".
Return the maximum number of operations that you can perform.



Example 1:

Input: s = "1001101"

Output: 4

Explanation:

We can perform the following operations:

Choose index i = 0. The resulting string is s = "0011101".
Choose index i = 4. The resulting string is s = "0011011".
Choose index i = 3. The resulting string is s = "0010111".
Choose index i = 2. The resulting string is s = "0001111".
Example 2:

Input: s = "00111"

Output: 0



Constraints:

1 <= s.length <= 105
s[i] is either '0' or '1'.
'''
from typing import *
import unittest


class Solution:
    def maxOperations(self, s: str) -> int:
        count = 0
        with_zero = False
        result = 0
        for c in s:
            if c == '1':
                if with_zero:
                    result += count
                    count += 1
                    with_zero = False
                else:
                    count += 1
            else:
                with_zero = True

        if with_zero:
            result += count
        return result


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("1001101",),4),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maxOperations(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
