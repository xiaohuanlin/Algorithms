'''
An integer x is numerically balanced if for every digit d in the number x, there are exactly d occurrences of that digit in x.

Given an integer n, return the smallest numerically balanced number strictly greater than n.



Example 1:

Input: n = 1
Output: 22
Explanation:
22 is numerically balanced since:
- The digit 2 occurs 2 times.
It is also the smallest numerically balanced number strictly greater than 1.
Example 2:

Input: n = 1000
Output: 1333
Explanation:
1333 is numerically balanced since:
- The digit 1 occurs 1 time.
- The digit 3 occurs 3 times.
It is also the smallest numerically balanced number strictly greater than 1000.
Note that 1022 cannot be the answer because 0 appeared more than 0 times.
Example 3:

Input: n = 3000
Output: 3133
Explanation:
3133 is numerically balanced since:
- The digit 1 occurs 1 time.
- The digit 3 occurs 3 times.
It is also the smallest numerically balanced number strictly greater than 3000.


Constraints:

0 <= n <= 106
'''
import unittest

from typing import *
from itertools import permutations


class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        total = [1, 22, 333, 4444, 55555, 666666, 7777777,
                 221, 3331, 44441, 555551, 6666661,
                 33322, 444422, 5555522,
                 4444333,
                 333221, 4444221]

        def find_all(num):
            all = str(num)
            return set(int(''.join(i)) for i in permutations(all))

        res = float('inf')

        for i in total:
            if i <= n:
                continue

            for v in find_all(i):
                if v > n and v < res:
                    res = v
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((1,),22),
            ((1000,),1333),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().nextBeautifulNumber(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
