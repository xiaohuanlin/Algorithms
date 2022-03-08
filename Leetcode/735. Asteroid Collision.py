'''
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
 

Constraints:

2 <= asteroids.length <= 104
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0
'''
import unittest
from typing import *


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):
            cur = asteroids[i]
            append = True
            while stack and stack[-1] > 0 and cur < 0:
                top = stack.pop()
                if abs(top) > abs(cur):
                    cur = top
                elif abs(top) == abs(cur):
                    append = False
                    break

            if not append:
                continue
            stack.append(cur)
        return stack


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([5,10,-5],), [5,10]),
            (([8,-8],), []),
            (([10,2,-5],), [10])
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().asteroidCollision(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
