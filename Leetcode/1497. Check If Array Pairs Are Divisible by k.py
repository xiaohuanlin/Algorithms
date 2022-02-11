'''
Given an array of integers arr of even length n and an integer k.

We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.

Return true If you can find a way to do that or false otherwise.

 

Example 1:

Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
Output: true
Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).
Example 2:

Input: arr = [1,2,3,4,5,6], k = 7
Output: true
Explanation: Pairs are (1,6),(2,5) and(3,4).
Example 3:

Input: arr = [1,2,3,4,5,6], k = 10
Output: false
Explanation: You can try all possible pairs to see that there is no way to divide arr into 3 pairs each with sum divisible by 10.
 

Constraints:

arr.length == n
1 <= n <= 105
n is even.
-109 <= arr[i] <= 109
1 <= k <= 105
'''
from typing import *
from collections import deque

import unittest
from collections import defaultdict


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        counts = [0 for _ in range(k + 1)]
        res = 0
        for num in arr:
            rem = num % k
            if rem == 0:
                continue

            if counts[k - rem] > 0:
                counts[k - rem] -= 1
                if counts[k - rem] == 0:
                    res -= 1
            else:
                if counts[rem] == 0:
                    res += 1
                counts[rem] += 1
        return res == 0

    
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,2,3,4,5,10,6,7,8,9], 5), True),
            (([1,2,3,4,5,6], 7), True),
            (([1,2,3,4,5,6], 10), False),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().canArrange(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

