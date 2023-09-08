'''
There is a street with n * 2 plots, where there are n plots on each side of the street. The plots on each side are numbered from 1 to n. On each plot, a house can be placed.

Return the number of ways houses can be placed such that no two houses are adjacent to each other on the same side of the street. Since the answer may be very large, return it modulo 109 + 7.

Note that if a house is placed on the ith plot on one side of the street, a house can also be placed on the ith plot on the other side of the street.

 

Example 1:

Input: n = 1
Output: 4
Explanation: 
Possible arrangements:
1. All plots are empty.
2. A house is placed on one side of the street.
3. A house is placed on the other side of the street.
4. Two houses are placed, one on each side of the street.
Example 2:


Input: n = 2
Output: 9
Explanation: The 9 possible arrangements are shown in the diagram above.
 

Constraints:

1 <= n <= 104
'''
from typing import *

import unittest

class Solution:
    def countHousePlacements(self, n: int) -> int:
        mod = int(1e9 + 7)
        a = 1
        b = 2
        for _ in range(n):
            a, b = b, a+b
            a %= mod
        return (a ** 2) % mod

        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((2,),9),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().countHousePlacements(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
