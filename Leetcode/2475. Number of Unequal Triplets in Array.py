'''
You are given a 0-indexed array of positive integers nums. Find the number of triplets (i, j, k) that meet the following conditions:

0 <= i < j < k < nums.length
nums[i], nums[j], and nums[k] are pairwise distinct.
In other words, nums[i] != nums[j], nums[i] != nums[k], and nums[j] != nums[k].
Return the number of triplets that meet the conditions.

 

Example 1:

Input: nums = [4,4,2,4,3]
Output: 3
Explanation: The following triplets meet the conditions:
- (0, 2, 4) because 4 != 2 != 3
- (1, 2, 4) because 4 != 2 != 3
- (2, 3, 4) because 2 != 4 != 3
Since there are 3 triplets, we return 3.
Note that (2, 0, 4) is not a valid triplet because 2 > 0.
Example 2:

Input: nums = [1,1,1,1,1]
Output: 0
Explanation: No triplets meet the conditions so we return 0.
 

Constraints:

3 <= nums.length <= 100
1 <= nums[i] <= 1000
'''
import unittest

from typing import *

from collections import Counter

class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        c = Counter(nums)        
        v = list(c.values())

        res = 0
        for i in range(len(v)):
            for j in range(i+1, len(v)):
                for k in range(j+1, len(v)):
                    res += v[i] * v[j] * v[k]
        return res
            



class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([4,4,2,4,3],),3),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().unequalTriplets(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
