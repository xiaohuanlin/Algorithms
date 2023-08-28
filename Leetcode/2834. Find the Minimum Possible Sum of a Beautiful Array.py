'''
You are given positive integers n and target.

An array nums is beautiful if it meets the following conditions:

nums.length == n.
nums consists of pairwise distinct positive integers.
There doesn't exist two distinct indices, i and j, in the range [0, n - 1], such that nums[i] + nums[j] == target.
Return the minimum possible sum that a beautiful array could have.

 

Example 1:

Input: n = 2, target = 3
Output: 4
Explanation: We can see that nums = [1,3] is beautiful.
- The array nums has length n = 2.
- The array nums consists of pairwise distinct positive integers.
- There doesn't exist two distinct indices, i and j, with nums[i] + nums[j] == 3.
It can be proven that 4 is the minimum possible sum that a beautiful array could have.
Example 2:

Input: n = 3, target = 3
Output: 8
Explanation: We can see that nums = [1,3,4] is beautiful.
- The array nums has length n = 3.
- The array nums consists of pairwise distinct positive integers.
- There doesn't exist two distinct indices, i and j, with nums[i] + nums[j] == 3.
It can be proven that 8 is the minimum possible sum that a beautiful array could have.
Example 3:

Input: n = 1, target = 1
Output: 1
Explanation: We can see, that nums = [1] is beautiful.
 

Constraints:

1 <= n <= 105
1 <= target <= 105
'''
from typing import *

import unittest

class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        s = set()
        c = 0
        res = 0
        start = 1

        while c < n:
            if start in s:
                start += 1
                continue
            c += 1
            s.add(target - start)
            res += start
            start += 1
        return res
        
        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((3,3),8),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minimumPossibleSum(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
