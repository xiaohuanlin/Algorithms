'''
Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. Otherwise, return false.

 

Example 1:

Input: s = "00110110", k = 2
Output: true
Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indices 0, 1, 3 and 2 respectively.
Example 2:

Input: s = "0110", k = 1
Output: true
Explanation: The binary codes of length 1 are "0" and "1", it is clear that both exist as a substring. 
Example 3:

Input: s = "0110", k = 2
Output: false
Explanation: The binary code "00" is of length 2 and does not exist in the array.
 

Constraints:

1 <= s.length <= 5 * 105
s[i] is either '0' or '1'.
1 <= k <= 20
'''
import unittest
from typing import *

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        sets = set()
        
        for i in range(len(s)):
            if i + k <= len(s):
                sets.add(s[i:i+k])
            
        return len(sets) == 2 ** k

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("00110110", 2), True),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().hasAllCodes(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()