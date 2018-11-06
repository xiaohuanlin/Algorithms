'''

Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False
Note:
The input array won't violate no-adjacent-flowers rule.
The input array size is in the range of [1, 20000].
n is a non-negative integer which won't exceed the input array size.

'''
import unittest


class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        space = 0

        flowerbed = [0] + flowerbed + [0, 1]
        for num in flowerbed:
            if num == 0:
                count += 1
            else:
                if count >= 2:
                    space += (count - 1)//2
                count = 0

        return n <= space


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,0,0,0,1], 1), True),
            (([1,0,0,0,1], 2), False),
            (([0], 1), True),
            (([0, 0, 0, 0], 3), False),
            (([1], 1), False),
            (([1,0,0,0,0,1], 2), False),
            (([0,0,1,0,1], 1), True),
            (([1, 0, 0, 0, 1, 0, 0], 2), True),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().canPlaceFlowers(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
