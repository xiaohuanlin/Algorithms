'''
You are given a binary string s. You are allowed to perform two types of operations on the string in any sequence:

Type-1: Remove the character at the start of the string s and append it to the end of the string.
Type-2: Pick any character in s and flip its value, i.e., if its value is '0' it becomes '1' and vice-versa.
Return the minimum number of type-2 operations you need to perform such that s becomes alternating.

The string is called alternating if no two adjacent characters are equal.

For example, the strings "010" and "1010" are alternating, while the string "0100" is not.
 

Example 1:

Input: s = "111000"
Output: 2
Explanation: Use the first operation two times to make s = "100011".
Then, use the second operation on the third and sixth elements to make s = "101010".
Example 2:

Input: s = "010"
Output: 0
Explanation: The string is already alternating.
Example 3:

Input: s = "1110"
Output: 1
Explanation: Use the second operation on the second element to make s = "1010".
 

Constraints:

1 <= s.length <= 105
s[i] is either '0' or '1'.
'''
from typing import *

import unittest

class Solution:
    def minFlips(self, s: str) -> int:
        res = [[0, 0]  for _ in range(len(s)+1)]
        rev_res = [[0, 0]  for _ in range(len(s)+1)]
        for i in range(len(s)):
            res[i+1] = [i for i in res[i]]
            res[i+1][(int(s[i]) + i) % 2] += 1

            rev_res[i+1] = [i for i in rev_res[i]]
            rev_res[i+1][(int(s[len(s) -1 - i]) + i) % 2] += 1

        ans = float('inf')
        for i in range(len(s)):
            ans = min(ans, 
                res[i][1] + rev_res[len(s) - i][0],
                res[i][0] + rev_res[len(s) - i][1]
            )
        return ans
        

class TestSolution(unittest.TestCase):
    def test_case(self):
        examples = (
            (("111000",),2),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minFlips(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()