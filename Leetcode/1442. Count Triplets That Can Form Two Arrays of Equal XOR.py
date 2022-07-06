'''
Given an array of integers arr.

We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).

Let's define a and b as follows:

a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
Note that ^ denotes the bitwise-xor operation.

Return the number of triplets (i, j and k) Where a == b.

 

Example 1:

Input: arr = [2,3,1,6,7]
Output: 4
Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)
Example 2:

Input: arr = [1,1,1,1,1]
Output: 10
 

Constraints:

1 <= arr.length <= 300
1 <= arr[i] <= 108
'''
from typing import *
import unittest

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        maps = {0: [-1]}
        s = 0
        xor = 0
        for i in range(len(arr)):
            xor ^= arr[i]
            for j in maps.get(xor, []):
                s += (i - j - 1)
            maps.setdefault(xor, []).append(i)
        return s

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([2,3,1,6,7],),4),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().countTriplets(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()