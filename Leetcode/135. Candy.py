'''
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

 

Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
 

Constraints:

n == ratings.length
1 <= n <= 2 * 104
0 <= ratings[i] <= 2 * 104
'''
import unittest

from typing import *


class Solution:
    def candy(self, ratings: List[int]) -> int:
        res = [1 for _ in range(len(ratings))]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                res[i] = res[i-1] + 1

        for i in range(len(ratings)-1)[::-1]:
            if ratings[i] > ratings[i+1]:
                res[i] = max(res[i], res[i+1] + 1)
        return sum(res)


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1, 2, 3, 4, 5],), 15),
            (([1, 0, 2],), 5),
            (([1, 2, 2],), 4)
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().candy(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

