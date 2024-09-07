'''
You are given an array nums consisting of positive integers.

We call two integers x and y in this problem almost equal if both integers can become equal after performing the following operation at most once:

Choose either x or y and swap any two digits within the chosen number.
Return the number of indices i and j in nums where i < j such that nums[i] and nums[j] are almost equal.

Note that it is allowed for an integer to have leading zeros after performing an operation.

 

Example 1:

Input: nums = [3,12,30,17,21]

Output: 2

Explanation:

The almost equal pairs of elements are:

3 and 30. By swapping 3 and 0 in 30, you get 3.
12 and 21. By swapping 1 and 2 in 12, you get 21.
Example 2:

Input: nums = [1,1,1,1,1]

Output: 10

Explanation:

Every two elements in the array are almost equal.

Example 3:

Input: nums = [123,231]

Output: 0

Explanation:

We cannot swap any two digits of 123 or 231 to reach the other.

 

Constraints:

2 <= nums.length <= 100
1 <= nums[i] <= 106
'''
from typing import *
import unittest

from collections import defaultdict


class Solution:
    def countPairs(self, nums: List[int]) -> int:
        maps = defaultdict(list)
        for n in nums:
            key = [0 for _ in range(10)]
            for c in str(n):
                if c != '0':
                    key[int(c)] += 1
            maps[tuple(key)].append(str(n))
        res = 0
        for l in maps.values():
            for i in range(len(l)):
                for j in range(i+1, len(l)):
                    length = max(len(l[i]), len(l[j]))
                    l[i] = l[i].zfill(length)
                    l[j] = l[j].zfill(length)
                    c = 0
                    for z in range(length):
                        if l[i][z] != l[j][z]:
                            c += 1
                    if c <= 2:
                        res += 1
        return res



class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([3,12,30,17,21],),2),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().countPairs(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()