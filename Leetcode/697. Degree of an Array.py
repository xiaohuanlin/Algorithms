'''

Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation:
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.

'''
import unittest


class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        fre_dict = defaultdict(list)
        result = []

        for i, num in enumerate(nums):
            fre_dict[num].append(i)
        max_fre = max(len(value) for value in fre_dict.values())
        for key, value in fre_dict.items():
            if len(value) == max_fre:
                # print(value)
                if len(value) > 1:
                    result.append(value[-1] - value[0] + 1)
                else:
                    result.append(value[0] + 1)
        return min(result)


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ([1, 2, 2, 3, 1], 2),
            ([1,2,2,3,1,4,2], 6)
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().findShortestSubArray(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
