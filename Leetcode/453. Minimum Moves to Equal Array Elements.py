'''

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.

Example:

Input:
[1,2,3]

Output:
3

Explanation:
Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

'''
import unittest


class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_value = min(nums)
        # return sum(n-min_value for n in nums)
        return sum(nums) - min_value * len(nums)

class TestSolution(unittest.TestCase):

    def test_minMoves(self):
        examples = (
            ([1,2,3], 3),
            ([1,2], 1),
            ([0], 0),
            ([-100, 0, 100], 300),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minMoves(first), second, msg="first: {}; second: {}".format(first, second))

unittest.main()