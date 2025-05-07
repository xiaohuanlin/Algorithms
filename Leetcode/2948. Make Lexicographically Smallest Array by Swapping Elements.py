'''
You are given a 0-indexed array of positive integers nums and a positive integer limit.

In one operation, you can choose any two indices i and j and swap nums[i] and nums[j] if |nums[i] - nums[j]| <= limit.

Return the lexicographically smallest array that can be obtained by performing the operation any number of times.

An array a is lexicographically smaller than an array b if in the first position where a and b differ, array a has an element that is less than the corresponding element in b. For example, the array [2,10,3] is lexicographically smaller than the array [10,2,3] because they differ at index 0 and 2 < 10.

 

Example 1:

Input: nums = [1,5,3,9,8], limit = 2
Output: [1,3,5,8,9]
Explanation: Apply the operation 2 times:
- Swap nums[1] with nums[2]. The array becomes [1,3,5,9,8]
- Swap nums[3] with nums[4]. The array becomes [1,3,5,8,9]
We cannot obtain a lexicographically smaller array by applying any more operations.
Note that it may be possible to get the same result by doing different operations.
Example 2:

Input: nums = [1,7,6,18,2,1], limit = 3
Output: [1,6,7,18,1,2]
Explanation: Apply the operation 3 times:
- Swap nums[1] with nums[2]. The array becomes [1,6,7,18,2,1]
- Swap nums[0] with nums[4]. The array becomes [2,6,7,18,1,1]
- Swap nums[0] with nums[5]. The array becomes [1,6,7,18,1,2]
We cannot obtain a lexicographically smaller array by applying any more operations.
Example 3:

Input: nums = [1,7,28,19,10], limit = 3
Output: [1,7,28,19,10]
Explanation: [1,7,28,19,10] is the lexicographically smallest array we can obtain because we cannot apply the operation on any two indices.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= limit <= 109
'''
import unittest

from typing import *


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        l = sorted([[n, i] for i, n in enumerate(nums)])
        res = [0 for _ in range(len(l))]
        idx = [l[0][1]]
        values = [l[0][0]]
        for i in range(1, len(l)):
            if l[i][0] - l[i-1][0] <= limit:
                idx.append(l[i][1])
                values.append(l[i][0])
                continue
            idx.sort()
            for e, index in enumerate(idx):
                res[index] = values[e]
            idx = [l[i][1]]
            values = [l[i][0]]
        
        idx.sort()
        for i, index in enumerate(idx):
            res[index] = values[i]
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,7,6,18,2,1], 3), [1,6,7,18,1,2]),
            (([1,5,3,9,8], 2), [1,3,5,8,9]),
            (([1,7,28,19,10], 3), [1,7,28,19,10]),
            (([1], 1), [1]),
            (([1,2], 1), [1,2]),
            (([2,1], 1), [1,2]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().lexicographicallySmallestArray(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

