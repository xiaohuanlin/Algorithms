'''

Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.

'''
import unittest


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first, second, third = (float('-inf'), float('-inf'), float('-inf'))
        for i in nums:
            if i == first or i == second or i == third:
                continue
            elif i > first:
                first, second, third = i, first, second
            elif i > second:
                first, second, third = first, i, second
            elif i > third:
                first, second, third = first, second, i
            # print(first, second, third)
        return third if third > float('-inf') else first


class TestSolution(unittest.TestCase):

    def test_thirdMax(self):
        examples = (
            # ([3, 2, 1], 1),
            # ([1, 2], 2),
            # ([2, 2, 3, 1], 1),
            ([5,2,4,1,3,6,0], 4),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().thirdMax(first), second, msg="first: {}; second: {}".format(first, second))


unittest.main()