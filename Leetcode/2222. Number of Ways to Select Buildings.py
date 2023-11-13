'''
You are given a 0-indexed binary string s which represents the types of buildings along a street where:

s[i] = '0' denotes that the ith building is an office and
s[i] = '1' denotes that the ith building is a restaurant.
As a city official, you would like to select 3 buildings for random inspection. However, to ensure variety, no two consecutive buildings out of the selected buildings can be of the same type.

For example, given s = "001101", we cannot select the 1st, 3rd, and 5th buildings as that would form "011" which is not allowed due to having two consecutive buildings of the same type.
Return the number of valid ways to select 3 buildings.

 

Example 1:

Input: s = "001101"
Output: 6
Explanation: 
The following sets of indices selected are valid:
- [0,2,4] from "001101" forms "010"
- [0,3,4] from "001101" forms "010"
- [1,2,4] from "001101" forms "010"
- [1,3,4] from "001101" forms "010"
- [2,4,5] from "001101" forms "101"
- [3,4,5] from "001101" forms "101"
No other selection is valid. Thus, there are 6 total ways.
Example 2:

Input: s = "11100"
Output: 0
Explanation: It can be shown that there are no valid selections.
 

Constraints:

3 <= s.length <= 105
s[i] is either '0' or '1'.
'''
import unittest

from typing import *


class Solution:
    def numberOfWays(self, s: str) -> int:
        left = [[0, 0] for _ in range(len(s))]            
        right = [[0, 0] for _ in range(len(s))]

        for i in range(len(s)):
            left[i][0] = left[i-1][0] + (s[i] == '0')
            left[i][1] = left[i-1][1] + (s[i] == '1')

            right[-i-1][0] = right[-i][0] + (s[-i-1] == '0')
            right[-i-1][1] = right[-i][1] + (s[-i-1] == '1')

        res = 0
        for i in range(1, len(s)-1):
            if s[i] == '1':
                res += left[i][0] * right[i][0]
            else:
                res += left[i][1] * right[i][1]
        return res
        


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("001101",),6),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().numberOfWays(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
