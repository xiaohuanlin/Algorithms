'''
An array is considered special if every pair of its adjacent elements contains two numbers with different parity.

You are given an array of integer nums and a 2D integer matrix queries, where for queries[i] = [fromi, toi] your task is to check that 
subarray
 nums[fromi..toi] is special or not.

Return an array of booleans answer such that answer[i] is true if nums[fromi..toi] is special.

 

Example 1:

Input: nums = [3,4,1,2,6], queries = [[0,4]]

Output: [false]

Explanation:

The subarray is [3,4,1,2,6]. 2 and 6 are both even.

Example 2:

Input: nums = [4,3,1,6], queries = [[0,2],[2,3]]

Output: [false,true]

Explanation:

The subarray is [4,3,1]. 3 and 1 are both odd. So the answer to this query is false.
The subarray is [1,6]. There is only one pair: (1,6) and it contains numbers with different parity. So the answer to this query is true.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105
1 <= queries.length <= 105
queries[i].length == 2
0 <= queries[i][0] <= queries[i][1] <= nums.length - 1
'''
from typing import *
import unittest


from bisect import bisect

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        all_list = []
        start = end = 0
        for i in range(1, len(nums)):
            if nums[i] % 2 + nums[i-1] % 2 == 1:
                end = i
            else:
                all_list.append([start, end])
                start = end = i
        all_list.append([start, end])

        res = []
        for query in queries:
            i = bisect(all_list, query)
            if i != 0 and all_list[i-1][0] <= query[0] and all_list[i-1][1] >= query[1]:
                res.append(True)
            elif i < len(all_list) and all_list[i][0] <= query[0] and all_list[i][1] >= query[1]:
                res.append(True)
            else:
                res.append(False)
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([3,4,1,2,6], [[0,4]]), [False]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().isArraySpecial(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()