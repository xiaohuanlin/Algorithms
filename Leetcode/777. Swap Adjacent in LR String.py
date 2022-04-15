'''
In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string end, return True if and only if there exists a sequence of moves to transform one string to the other.

 

Example 1:

Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
Output: true
Explanation: We can transform start to end following these steps:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX
Example 2:

Input: start = "X", end = "L"
Output: false
 

Constraints:

1 <= start.length <= 104
start.length == end.length
Both start and end will only consist of characters in 'L', 'R', and 'X'.
'''
from typing import *

import unittest
    
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        i = 0
        j = 0
        while i < len(start) and j < len(start):
            while i < len(start) and start[i] == 'X':
                i += 1
            while j < len(end) and end[j] == 'X':
                j += 1
            
            if i == len(start) or j == len(end):
                break
                
            if start[i] == end[j] and \
                ((start[i] == 'R' and i <= j) or (start[i] == 'L' and i >= j)):
                pass
            else:
                return False
            i += 1
            j += 1
        
        for k in range(i, len(start)):
            if start[k] != 'X':
                return False
        for k in range(j, len(end)):
            if end[k] != 'X':
                return False
        return True
        
        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("RXXLRXRXL", "XRLXXRRLX"), True),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().canTransform(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
