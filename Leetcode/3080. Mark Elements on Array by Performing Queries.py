'''
You are given a 0-indexed array nums of size n consisting of positive integers.

You are also given a 2D array queries of size m where queries[i] = [indexi, ki].

Initially all elements of the array are unmarked.

You need to apply m queries on the array in order, where on the ith query you do the following:

Mark the element at index indexi if it is not already marked.
Then mark ki unmarked elements in the array with the smallest values. If multiple such elements exist, mark the ones with the smallest indices. And if less than ki unmarked elements exist, then mark all of them.
Return an array answer of size m where answer[i] is the sum of unmarked elements in the array after the ith query.

 

Example 1:

Input: nums = [1,2,2,1,2,3,1], queries = [[1,2],[3,3],[4,2]]

Output: [8,3,0]

Explanation:

We do the following queries on the array:

Mark the element at index 1, and 2 of the smallest unmarked elements with the smallest indices if they exist, the marked elements now are nums = [1,2,2,1,2,3,1]. The sum of unmarked elements is 2 + 2 + 3 + 1 = 8.
Mark the element at index 3, since it is already marked we skip it. Then we mark 3 of the smallest unmarked elements with the smallest indices, the marked elements now are nums = [1,2,2,1,2,3,1]. The sum of unmarked elements is 3.
Mark the element at index 4, since it is already marked we skip it. Then we mark 2 of the smallest unmarked elements with the smallest indices if they exist, the marked elements now are nums = [1,2,2,1,2,3,1]. The sum of unmarked elements is 0.
Example 2:

Input: nums = [1,4,2,3], queries = [[0,1]]

Output: [7]

Explanation: We do one query which is mark the element at index 0 and mark the smallest element among unmarked elements. The marked elements will be nums = [1,4,2,3], and the sum of unmarked elements is 4 + 3 = 7.

 

Constraints:

n == nums.length
m == queries.length
1 <= m <= n <= 105
1 <= nums[i] <= 105
queries[i].length == 2
0 <= indexi, ki <= n - 1
'''
from typing import *

import unittest

from heapq import heappush, heappop


class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        h = []
        for i, n in enumerate(nums):
            heappush(h, (n, i))
        
        total = set()
        sum_v = sum(nums)
        res = []
        for i, c in queries:
            if i not in total:
                total.add(i)
                sum_v -= nums[i]
            for _ in range(c):
                while h:
                    n, index = heappop(h)
                    if index in total:
                        continue
                    total.add(index)
                    sum_v -= nums[index]
                    break
            res.append(sum_v)
        return res
            

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,2,2,1,2,3,1], [[1,2],[3,3],[4,2]]), [8,3,0]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().unmarkedSumArray(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
