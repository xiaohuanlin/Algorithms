'''
You are given an integer array values where values[i] represents the value of the ith sightseeing spot. Two sightseeing spots i and j have a distance j - i between them.

The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j: the sum of the values of the sightseeing spots, minus the distance between them.

Return the maximum score of a pair of sightseeing spots.

 

Example 1:

Input: values = [8,1,5,2,6]
Output: 11
Explanation: i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11
Example 2:

Input: values = [1,2]
Output: 2
 

Constraints:

2 <= values.length <= 5 * 104
1 <= values[i] <= 1000
'''

from typing import *

import unittest


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # change to (v[i] + i + v[j] + j) - 2 * j
        max_v = 0
        res = 0
        for i in range(len(values)):
            res = max(res, max_v + values[i] - i)
            max_v = max(max_v, values[i] + i)
        return res

        
class TestSolution(unittest.TestCase):
    def test_case(self):
        examples = (
            (([8,1,5,2,6],), 11),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maxScoreSightseeingPair(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

