'''

Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3.
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4.
Example 2:
Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1.
Note: Length of the array will not exceed 10,000.

'''
import unittest


class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        count = 0
        max_c = 0
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                count += 1
            else:
                if count > max_c:
                    max_c = count
                count = 0
        else:
            if count > max_c:
                max_c = count

        return max_c + 1



class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ([1,3,5,4,7], 3),
            ([2,2,2,2,2], 1),
            ([], 0),
            ([2,3,4,1,2,3,4], 4)
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().findLengthOfLCIS(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
