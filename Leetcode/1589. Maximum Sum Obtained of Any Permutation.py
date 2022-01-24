'''
We have an array of integers, nums, and an array of requests where requests[i] = [starti, endi]. The ith request asks for the sum of nums[starti] + nums[starti + 1] + ... + nums[endi - 1] + nums[endi]. Both starti and endi are 0-indexed.

Return the maximum total sum of all requests among all permutations of nums.

Since the answer may be too large, return it modulo 109 + 7.

 

Example 1:

Input: nums = [1,2,3,4,5], requests = [[1,3],[0,1]]
Output: 19
Explanation: One permutation of nums is [2,1,3,4,5] with the following result: 
requests[0] -> nums[1] + nums[2] + nums[3] = 1 + 3 + 4 = 8
requests[1] -> nums[0] + nums[1] = 2 + 1 = 3
Total sum: 8 + 3 = 11.
A permutation with a higher total sum is [3,5,4,2,1] with the following result:
requests[0] -> nums[1] + nums[2] + nums[3] = 5 + 4 + 2 = 11
requests[1] -> nums[0] + nums[1] = 3 + 5  = 8
Total sum: 11 + 8 = 19, which is the best that you can do.
Example 2:

Input: nums = [1,2,3,4,5,6], requests = [[0,1]]
Output: 11
Explanation: A permutation with the max total sum is [6,5,4,3,2,1] with request sums [11].
Example 3:

Input: nums = [1,2,3,4,5,10], requests = [[0,2],[1,3],[1,1]]
Output: 47
Explanation: A permutation with the max total sum is [4,10,5,3,2,1] with request sums [19,18,10].
 

Constraints:

n == nums.length
1 <= n <= 105
0 <= nums[i] <= 105
1 <= requests.length <= 105
requests[i].length == 2
0 <= starti <= endi < n
'''
from typing import *

import unittest


class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        counts = [0 for _ in range(len(nums))]
        for request in requests:
            counts[request[0]] += 1
            if request[1] + 1 < len(nums):
                counts[request[1] + 1] -= 1
        
        for i in range(1, len(counts)):
            counts[i] += counts[i - 1]
        
        counts.sort(reverse=True)
        nums.sort(reverse=True)
        res = 0

        for c in counts:
            res += (nums[0] * c)
            nums.pop(0)

        return res % (10**9 + 7)


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,2,3,4,5], [[1,3],[0,1]]), 19),
            (([1,2,3,4,5,6], [[0,1]]), 11),
            (([1,2,3,4,5,10], [[0,2],[1,3],[1,1]]), 47),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maxSumRangeQuery(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
