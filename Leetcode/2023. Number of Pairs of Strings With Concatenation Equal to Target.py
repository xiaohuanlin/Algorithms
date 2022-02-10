'''
Given an array of digit strings nums and a digit string target, return the number of pairs of indices (i, j) (where i != j) such that the concatenation of nums[i] + nums[j] equals target.

 

Example 1:

Input: nums = ["777","7","77","77"], target = "7777"
Output: 4
Explanation: Valid pairs are:
- (0, 1): "777" + "7"
- (1, 0): "7" + "777"
- (2, 3): "77" + "77"
- (3, 2): "77" + "77"
Example 2:

Input: nums = ["123","4","12","34"], target = "1234"
Output: 2
Explanation: Valid pairs are:
- (0, 1): "123" + "4"
- (2, 3): "12" + "34"
Example 3:

Input: nums = ["1","1","1"], target = "11"
Output: 6
Explanation: Valid pairs are:
- (0, 1): "1" + "1"
- (1, 0): "1" + "1"
- (0, 2): "1" + "1"
- (2, 0): "1" + "1"
- (1, 2): "1" + "1"
- (2, 1): "1" + "1"
 

Constraints:

2 <= nums.length <= 100
1 <= nums[i].length <= 100
2 <= target.length <= 100
nums[i] and target consist of digits.
nums[i] and target do not have leading zeros.
'''
from typing import *
from collections import deque

import unittest
from collections import defaultdict


class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        mem = defaultdict(int)
        res = 0
        for num in nums:
            if target.startswith(num):
                res += mem[target[len(num):]]
            if target.endswith(num):
                res += mem[target[:len(target) - len(num)]]
            mem[num] += 1
        return res

    
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((["777","7","77","77"], "7777"), 4),
            ((["123","4","12","34"], "1234"), 2),
            ((["1","1","1"], "11"), 6),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().numOfPairs(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

