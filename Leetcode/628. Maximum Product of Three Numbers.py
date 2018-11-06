'''

Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:
Input: [1,2,3]
Output: 6
Example 2:
Input: [1,2,3,4]
Output: 24
Note:
The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.

'''
import unittest


class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # nums = sorted(nums, reverse=True)
        # return max(nums[0] * nums[1] * nums[2], nums[0] * nums[-1] * nums[-2])
        # ---------------------------------------------------
        from heapq import nlargest, nsmallest
        a, b = nlargest(3, nums), nsmallest(2, nums)
        return max(a[0]*a[1]*a[2], a[0]*b[0]*b[1])






class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ([1,2,3], 6),
            ([1,2,3,4], 24),
            ([1,-2,3,4], 12),
            ([5, 2, 3, 4], 60),
            ([1,0,100], 0),
            ([-1,-2,-3,-4], -6),
            ([-1000,-1000,1000], 1000000000),
            ([-4,-3,-2,-1,60], 720),
            ([722,634,-504,-379,163,-613,-842,-578,750,951,-158,30,-238,-392,-487,-797,-157,-374,999,-5,-521,-879,-858,382,626,803,-347,903,-205,57,-342,186,-736,17,83,726,-960,343,-984,937,-758,-122,577,-595,-544,-559,903,-183,192,825,368,-674,57,-959,884,29,-681,-339,582,969,-95,-455,-275,205,-548,79,258,35,233,203,20,-936,878,-868,-458,-882,867,-664,-892,-687,322,844,-745,447,-909,-586,69,-88,88,445,-553,-666,130,-640,-918,-7,-420,-368,250,-786], 943695360),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maximumProduct(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
