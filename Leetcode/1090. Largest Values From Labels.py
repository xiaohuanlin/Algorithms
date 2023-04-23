'''
There is a set of n items. You are given two integer arrays values and labels where the value and the label of the ith element are values[i] and labels[i] respectively. You are also given two integers numWanted and useLimit.

Choose a subset s of the n elements such that:

The size of the subset s is less than or equal to numWanted.
There are at most useLimit items with the same label in s.
The score of a subset is the sum of the values in the subset.

Return the maximum score of a subset s.

 

Example 1:

Input: values = [5,4,3,2,1], labels = [1,1,2,2,3], numWanted = 3, useLimit = 1
Output: 9
Explanation: The subset chosen is the first, third, and fifth items.
Example 2:

Input: values = [5,4,3,2,1], labels = [1,3,3,3,2], numWanted = 3, useLimit = 2
Output: 12
Explanation: The subset chosen is the first, second, and third items.
Example 3:

Input: values = [9,8,8,7,6], labels = [0,0,0,1,1], numWanted = 3, useLimit = 1
Output: 16
Explanation: The subset chosen is the first and fourth items.
 

Constraints:

n == values.length == labels.length
1 <= n <= 2 * 104
0 <= values[i], labels[i] <= 2 * 104
1 <= numWanted, useLimit <= n
'''
from typing import *
import unittest

from collections import Counter
from heapq import heappop, heapify

class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        h = [(-v, l) for v, l in zip(values, labels)]
        heapify(h)
        limit = Counter()
        res = 0

        while h and numWanted > 0:
            v, l = heappop(h)
            if limit[l] == useLimit:
                continue
            else:
                numWanted -= 1
                res -= v
                limit[l] += 1
        return res
                    

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([9,8,8,7,6], [0,0,0,1,1], 3, 1), 16),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().largestValsFromLabels(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
