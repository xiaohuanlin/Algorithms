'''
You are given an array of positive integers price where price[i] denotes the price of the ith candy and a positive integer k.

The store sells baskets of k distinct candies. The tastiness of a candy basket is the smallest absolute difference of the prices of any two candies in the basket.

Return the maximum tastiness of a candy basket.



Example 1:

Input: price = [13,5,1,8,21,2], k = 3
Output: 8
Explanation: Choose the candies with the prices [13,5,21].
The tastiness of the candy basket is: min(|13 - 5|, |13 - 21|, |5 - 21|) = min(8, 8, 16) = 8.
It can be proven that 8 is the maximum tastiness that can be achieved.
Example 2:

Input: price = [1,3,1], k = 2
Output: 2
Explanation: Choose the candies with the prices [1,3].
The tastiness of the candy basket is: min(|1 - 3|) = min(2) = 2.
It can be proven that 2 is the maximum tastiness that can be achieved.
Example 3:

Input: price = [7,7,7,7], k = 2
Output: 0
Explanation: Choosing any two distinct candies from the candies we have will result in a tastiness of 0.


Constraints:

2 <= k <= price.length <= 105
1 <= price[i] <= 109
'''
import unittest

from typing import *
from math import ceil

class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        def is_ok(n):
            cur = float('-inf')
            cnt = 0
            for p in price:
                if p >= cur + n:
                    cnt += 1
                    cur = p
                if cnt >= k:
                    return True
            return cnt >= k

        start = 0
        end = int(1e9)
        while start < end:
            middle = ceil((start + end) / 2)
            if is_ok(middle):
                start = middle
            else:
                end = middle - 1
        return start



class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([13,5,1,8,21,2], 3), 8),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maximumTastiness(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
