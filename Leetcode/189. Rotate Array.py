'''
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
'''

import unittest

class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length

        if k == 0:
            return None
    
        a, b = 0, k
        k_list = nums[a:b]
        
        max_time = length//k + 1
        i = 0
        while i <= max_time:

            if a >= b:
                # print((a,b), nums, k_list)
                nums[a:], k_list[:length-a] = k_list[:length-a], nums[a:]
                # print((a,b), nums, k_list)

                nums[:b], k_list[length-a:] = k_list[length-a:], nums[:b]
                # print((a,b), nums, k_list)
            else:
                nums[a:b], k_list= k_list, nums[a:b]
            a,b = (a+k)%length, (b+k)%length
            i += 1
        # return nums

class TestSolution(unittest.TestCase):

    def test_rotate(self):
        examples = (
            (([1,2,3,4,5,6,7], 3), [5,6,7,1,2,3,4]),
            (([1], 1), [1]),
            (([1,2], 5), [2,1]),
        )
        for first,second in examples:
            self.assert_function(first, second)
        
    def assert_function(self, first, second):
        self.assertEqual(Solution().rotate(*first), second)

unittest.main()