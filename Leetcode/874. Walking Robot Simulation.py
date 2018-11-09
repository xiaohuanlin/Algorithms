'''

A robot on an infinite grid starts at point (0, 0) and faces north.  The robot can receive one of three possible types of commands:

-2: turn left 90 degrees
-1: turn right 90 degrees
1 <= x <= 9: move forward x units
Some of the grid squares are obstacles.

The i-th obstacle is at grid point (obstacles[i][0], obstacles[i][1])

If the robot would try to move onto them, the robot stays on the previous grid square instead (but still continues following the rest of the route.)

Return the square of the maximum Euclidean distance that the robot will be from the origin.



Example 1:

Input: commands = [4,-1,3], obstacles = []
Output: 25
Explanation: robot will go to (3, 4)
Example 2:

Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
Output: 65
Explanation: robot will be stuck at (1, 4) before turning left and going to (1, 8)


Note:

0 <= commands.length <= 10000
0 <= obstacles.length <= 10000
-30000 <= obstacle[i][0] <= 30000
-30000 <= obstacle[i][1] <= 30000
The answer is guaranteed to be less than 2 ^ 31.

'''
import unittest


class Solution:
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        turn_left_dict = {
            (0, 1): (-1, 0),
            (-1, 0): (0, -1),
            (0, -1): (1, 0),
            (1, 0): (0, 1)
        }
        turn_right_dict = {value: key for key, value in turn_left_dict.items()}
        obstacles = set(map(tuple, obstacles))

        direct = (0, 1)
        x, y = (0, 0)
        max_distance = 0
        for command in commands:
            if command == -1:
                direct = turn_right_dict[direct]
            elif command == -2:
                direct = turn_left_dict[direct]
            else:
                x_off, y_off = direct[0], direct[1]
                while command > 0:
                    if (x + x_off, y + y_off) not in obstacles:
                        x, y = x + x_off, y + y_off
                    command -= 1
                max_distance = max(max_distance, x ** 2 + y ** 2)
        return max_distance


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([4, -1, 3], []), 25),
            (([4, -1, 4, -2, 4], [[2, 4]]), 65),
            (([-2, -1, -2, 3, 7],
              [[1, -3], [2, -3], [4, 0], [-2, 5], [-5, 2], [0, 0], [4, -4], [-2, -5], [-1, -2], [0, 2]]), 100),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().robotSim(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
