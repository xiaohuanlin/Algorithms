'''
You are given an array nums, where each number in the array appears either once or twice.

Return the bitwise XOR of all the numbers that appear twice in the array, or 0 if no number appears twice.

 

Example 1:

Input: nums = [1,2,1,3]

Output: 1

Explanation:

The only number that appears twice in nums is 1.

Example 2:

Input: nums = [1,2,3]

Output: 0

Explanation:

No number appears twice in nums.

Example 3:

Input: nums = [1,2,2,1]

Output: 3

Explanation:

Numbers 1 and 2 appeared twice. 1 XOR 2 == 3.

 

Constraints:

1 <= nums.length <= 50
1 <= nums[i] <= 50
Each number in nums appears either once or twice.
'''
from typing import *
import unittest


from collections import Counter

class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        c = Counter(nums)        
        res = 0
        for k, v in c.items():
            if v == 2:
                res ^= k
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,2,1,3],),1),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().duplicateNumbersXOR(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()