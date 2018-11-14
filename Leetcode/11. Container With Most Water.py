'''

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.





The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.



Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49

'''
import unittest


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # max_area = 0
        # for i in range(len(height)):
        #     for j in range(i+1, len(height)):
        #         area = (j - i) * min(height[i], height[j])
        #         max_area = max(area, max_area)
        # return max_area
        # ------------------------------------------------------
        # assume that we add two lines at beginning and ending, there are 3 possible solutions:
        # 1. the level higher than before
        #     (a) this means we just choose two lines as container
        # 2. the level lower than before
        #     (a) either choose old lines
        #     (b) or choose the higher line of two lines if this higher than min line of old lines
        # Another solution
        # 1. The widest container (using first and last line) is a good candidate, because of its width. Its water level is the height of the smaller one of first and last line.
        # 2. All other containers are less wide and thus would need a higher water level in order to hold more water.
        # 3. The smaller one of first and last line doesn't support a higher water level and can thus be safely removed from further consideration.

        i = 0
        j = len(height) - 1
        water = 0
        while i < j:
            water = max(water, (j - i) * min(height[j], height[i]))
            # the less line should not count into candidate
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return water



class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ([1,8,6,2,5,4,8,3,7], 49),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maxArea(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
