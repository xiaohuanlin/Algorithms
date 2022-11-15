'''
In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket. Rick has n empty baskets, the ith basket is at position[i], Morty has m balls and needs to distribute the balls into the baskets such that the minimum magnetic force between any two balls is maximum.

Rick stated that magnetic force between two different balls at positions x and y is |x - y|.

Given the integer array position and the integer m. Return the required force.

 

Example 1:


Input: position = [1,2,3,4,7], m = 3
Output: 3
Explanation: Distributing the 3 balls into baskets 1, 4 and 7 will make the magnetic force between ball pairs [3, 3, 6]. The minimum magnetic force is 3. We cannot achieve a larger minimum magnetic force than 3.
Example 2:

Input: position = [5,4,3,2,1,1000000000], m = 2
Output: 999999999
Explanation: We can use baskets 1 and 1000000000.
 

Constraints:

n == position.length
2 <= n <= 105
1 <= position[i] <= 109
All integers in position are distinct.
2 <= m <= position.length
'''
from typing import *
import unittest

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def is_enough(n):
            count = 1
            prev = position[0]
            for i in range(len(position)):
                if position[i] - prev >= n:
                    count += 1
                    prev = position[i]
            return count >= m

        start = res = 1
        end = position[-1]
        while start <= end:
            middle = (start + end) // 2
            if is_enough(middle):
                start = middle + 1
                res = start - 1
            else:
                end = middle - 1
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([5,4,3,2,1,1000000000],2),999999999),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maxDistance(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
