'''

Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.

'''
import unittest


class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if nums == []:
        #     return 0
        # if nums[0] <= min(nums):
        #     return self.findUnsortedSubarray(nums[1:])
        # elif nums[-1] >= max(nums):
        #     return self.findUnsortedSubarray(nums[:-1])
        # return len(nums)
        # ---------------------------------------------
        # result = []
        # stack = []
        # # calculate the left and right continuous same number
        # for x, y in zip(nums, sorted(nums)):
        #     if x != y:
        #         result.append(stack[::])
        #         stack = []
        #     else:
        #         stack.append(x)
        # else:
        #     result.append(stack[::])
        # return len(nums) - (len(result[0]) + len(result[-1])) if len(result) > 1 else len(nums) - len(result[0])
        # -----------------------------------------------

        result = list(zip(nums, sorted(nums)))
        i, j = 0, len(result)-1
        i_count = j_count = 0
        while i <= j:
            if result[i][0] != result[i][1] and result[j][0] != result[j][1]:
                break

            if result[i][0] == result[i][1]:
                # print(i)
                i_count += 1
                i += 1
            elif result[j][0] == result[j][1]:
                # print(j)
                j_count += 1
                j -= 1

        return len(nums) - i_count - j_count



class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ([2, 6, 4, 8, 10, 9, 15], 5),
            ([1, 2, 3, 4], 0),
            ([1], 0),
            ([1, 2], 0),
            ([1,3,2,4,5], 2),
            ([1,2,3,3,3], 0),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().findUnsortedSubarray(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
