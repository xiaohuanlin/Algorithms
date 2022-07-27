'''
Given a binary string s, return the minimum number of character swaps to make it alternating, or -1 if it is impossible.

The string is called alternating if no two adjacent characters are equal. For example, the strings "010" and "1010" are alternating, while the string "0100" is not.

Any two characters may be swapped, even if they are not adjacent.

 

Example 1:

Input: s = "111000"
Output: 1
Explanation: Swap positions 1 and 4: "111000" -> "101010"
The string is now alternating.
Example 2:

Input: s = "010"
Output: 0
Explanation: The string is already alternating, no swaps are needed.
Example 3:

Input: s = "1110"
Output: -1
 

Constraints:

1 <= s.length <= 1000
s[i] is either '0' or '1'.
'''

from typing import *

import unittest


class Solution:
    def minSwaps(self, s: str) -> int:
        res_odd = -1
        res_even = -1
        total_one = 0
        # odd
        count = 0
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] != '1':
                    count += 1
            if s[i] == '1':
                total_one += 1
        if total_one == (len(s) + 1) // 2:
            res_odd = count
        
        # even
        count = 0
        for i in range(len(s)):
            if i % 2 == 1:
                if s[i] != '1':
                    count += 1
        if total_one == len(s) // 2:
            res_even = count
        
        if res_odd != -1 and res_even != -1:
            return min(res_odd, res_even)
        elif res_odd == -1 and res_even == -1:
            return -1
        elif res_odd != -1:
            return res_odd
        return res_even
        
class TestSolution(unittest.TestCase):
    def test_case(self):
        examples = (
            (("111000",),1),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minSwaps(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

