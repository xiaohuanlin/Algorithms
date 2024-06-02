'''
You are given an integer array nums, an integer array queries, and an integer x.

For each queries[i], you need to find the index of the queries[i]th occurrence of x in the nums array. If there are fewer than queries[i] occurrences of x, the answer should be -1 for that query.

Return an integer array answer containing the answers to all queries.

 

Example 1:

Input: nums = [1,3,1,7], queries = [1,3,2,4], x = 1

Output: [0,-1,2,-1]

Explanation:

For the 1st query, the first occurrence of 1 is at index 0.
For the 2nd query, there are only two occurrences of 1 in nums, so the answer is -1.
For the 3rd query, the second occurrence of 1 is at index 2.
For the 4th query, there are only two occurrences of 1 in nums, so the answer is -1.
Example 2:

Input: nums = [1,2,3], queries = [10], x = 5

Output: [-1]

Explanation:

For the 1st query, 5 doesn't exist in nums, so the answer is -1.
 

Constraints:

1 <= nums.length, queries.length <= 105
1 <= queries[i] <= 105
1 <= nums[i], x <= 104
'''
from typing import *
import unittest



class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        arr = []
        res = []

        for i in range(len(nums)):
            if nums[i] == x:
                arr.append(i)
        
        for q in queries:
            if q - 1 >= len(arr):
                res.append(-1)
            else:
                res.append(arr[q-1])
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,3,1,7], [1,3,2,4], 1), [0,-1,2,-1]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().occurrencesOfElement(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()