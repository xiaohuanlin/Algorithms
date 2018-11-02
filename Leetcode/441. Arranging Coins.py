'''

You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.

'''
import unittest


class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        # stair = 0
        # while n > 0:
        #     stair += 1
        #     n -= stair
        #     if n < 0:
        #         stair -= 1
        #         break
        # return stair
        # ------------
        # i = 0
        # while True:
        #     sum_ = i*(i+1)/2
        #     if sum_ > n:
        #         return i - 1
        #     i += 1
        # -------------
        # use the root of the function to get answer
        return int(((8*n+1)**0.5 - 1)/2)



class TestSolution(unittest.TestCase):

    def test_arrangeCoins(self):
        examples = (
            (0, 0),
            (1, 1),
            (5, 2),
            (8, 3),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().arrangeCoins(first), second, msg="first: {}; second: {}".format(first, second))


unittest.main()