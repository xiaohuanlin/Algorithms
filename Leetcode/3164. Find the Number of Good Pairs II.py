'''
You are given 2 integer arrays nums1 and nums2 of lengths n and m respectively. You are also given a positive integer k.

A pair (i, j) is called good if nums1[i] is divisible by nums2[j] * k (0 <= i <= n - 1, 0 <= j <= m - 1).

Return the total number of good pairs.

 

Example 1:

Input: nums1 = [1,3,4], nums2 = [1,3,4], k = 1

Output: 5

Explanation:

The 5 good pairs are (0, 0), (1, 0), (1, 1), (2, 0), and (2, 2).
Example 2:

Input: nums1 = [1,2,4,12], nums2 = [2,4], k = 3

Output: 2

Explanation:

The 2 good pairs are (3, 0) and (3, 1).

 

Constraints:

1 <= n, m <= 105
1 <= nums1[i], nums2[j] <= 106
1 <= k <= 103
'''
from typing import *
import unittest


from collections import Counter, defaultdict

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        c2 = Counter(n*k for n in nums2)
        max_v = max(nums1)
        d = defaultdict(int)

        for k2, v2 in c2.items():
            for n in range(k2, max_v + 1, k2):
                d[n] += v2

        return sum(d[i] for i in nums1 if i in d)


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,2,4,12], [2,4], 3), 2),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().numberOfPairs(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()