'''
You are given an integer array ranks representing the ranks of some mechanics. ranksi is the rank of the ith mechanic. A mechanic with a rank r can repair n cars in r * n2 minutes.

You are also given an integer cars representing the total number of cars waiting in the garage to be repaired.

Return the minimum time taken to repair all the cars.

Note: All the mechanics can repair the cars simultaneously.



Example 1:

Input: ranks = [4,2,3,1], cars = 10
Output: 16
Explanation:
- The first mechanic will repair two cars. The time required is 4 * 2 * 2 = 16 minutes.
- The second mechanic will repair two cars. The time required is 2 * 2 * 2 = 8 minutes.
- The third mechanic will repair two cars. The time required is 3 * 2 * 2 = 12 minutes.
- The fourth mechanic will repair four cars. The time required is 1 * 4 * 4 = 16 minutes.
It can be proved that the cars cannot be repaired in less than 16 minutes.​​​​​
Example 2:

Input: ranks = [5,1,8], cars = 6
Output: 16
Explanation:
- The first mechanic will repair one car. The time required is 5 * 1 * 1 = 5 minutes.
- The second mechanic will repair four cars. The time required is 1 * 4 * 4 = 16 minutes.
- The third mechanic will repair one car. The time required is 8 * 1 * 1 = 8 minutes.
It can be proved that the cars cannot be repaired in less than 16 minutes.​​​​​


Constraints:

1 <= ranks.length <= 105
1 <= ranks[i] <= 100
1 <= cars <= 106
'''
import unittest

from typing import *

from math import sqrt

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def can_be_repaired(t):
            res = 0
            for rank in ranks:
                res += int(sqrt(t / rank))
            return res >= cars

        start = 0
        end = max(ranks) * cars ** 2

        while start < end:
            middle = start + (end - start) // 2
            if can_be_repaired(middle):
                end = middle
            else:
                start = middle + 1
        return start


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([4,2,3,1], 10), 16),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().repairCars(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
