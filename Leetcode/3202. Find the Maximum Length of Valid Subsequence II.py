'''
You are given an integer array nums and a positive integer k.
A subsequence sub of nums with length x is called valid if it satisfies:

(sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k == ... == (sub[x - 2] + sub[x - 1]) % k.
Return the length of the longest valid subsequence of nums.


Example 1:

Input: nums = [1,2,3,4,5], k = 2

Output: 5

Explanation:

The longest valid subsequence is [1, 2, 3, 4, 5].

Example 2:

Input: nums = [1,4,2,3,1,4], k = 3

Output: 4

Explanation:

The longest valid subsequence is [1, 4, 1, 4].



Constraints:

2 <= nums.length <= 103
1 <= nums[i] <= 107
1 <= k <= 103
'''
import unittest

from typing import *


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        l = [[] for _ in range(k)]
        for i, n in enumerate(nums):
            l[n % k].append(i)

        res = 0
        for i in range(len(l)):
            for j in range(len(l)):
                si = 0
                sj = 0
                cur = -1
                switch = True
                cnt = 0
                while si < len(l[i]) and sj < len(l[j]):
                    if switch:
                        while si < len(l[i]) and l[i][si] <= cur:
                            si += 1
                        if si >= len(l[i]):
                            break
                        cnt += 1
                        cur = l[i][si]
                        switch = False
                    else:
                        while sj < len(l[j]) and l[j][sj] <= cur:
                            sj += 1
                        if sj >= len(l[j]):
                            break
                        cnt += 1
                        cur = l[j][sj]
                        switch = True
                res = max(res, cnt)
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,4,2,3,1,4],3),4),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maximumLength(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
