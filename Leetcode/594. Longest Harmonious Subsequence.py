'''

We define a harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:
Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
Note: The length of the input array will not exceed 20,000.

'''
import unittest


class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        if nums == []:
            return 0
        nums_dict = Counter(nums)
        nums = sorted(nums)
        pre = nums[0]
        result = []
        for num in nums:
            if num != pre:
                if num - pre == 1:
                    result.append((pre, num))
                pre = num
        return max((nums_dict[record[0]] + nums_dict[record[1]] for record in result), default=0)


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ([1,3,2,2,5,2,3,7], 5),
            ([], 0),
            ([0, 1], 2)
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().findLHS(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
