'''
You are given a 0-indexed 8 x 8 grid board, where board[r][c] represents the cell (r, c) on a game board. On the board, free cells are represented by '.', white cells are represented by 'W', and black cells are represented by 'B'.

Each move in this game consists of choosing a free cell and changing it to the color you are playing as (either white or black). However, a move is only legal if, after changing it, the cell becomes the endpoint of a good line (horizontal, vertical, or diagonal).

A good line is a line of three or more cells (including the endpoints) where the endpoints of the line are one color, and the remaining cells in the middle are the opposite color (no cells in the line are free). You can find examples for good lines in the figure below:


Given two integers rMove and cMove and a character color representing the color you are playing as (white or black), return true if changing cell (rMove, cMove) to color color is a legal move, or false if it is not legal.



Example 1:


Input: board = [[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],["W","B","B",".","W","W","W","B"],[".",".",".","B",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."]], rMove = 4, cMove = 3, color = "B"
Output: true
Explanation: '.', 'W', and 'B' are represented by the colors blue, white, and black respectively, and cell (rMove, cMove) is marked with an 'X'.
The two good lines with the chosen cell as an endpoint are annotated above with the red rectangles.
Example 2:


Input: board = [[".",".",".",".",".",".",".","."],[".","B",".",".","W",".",".","."],[".",".","W",".",".",".",".","."],[".",".",".","W","B",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".","B","W",".","."],[".",".",".",".",".",".","W","."],[".",".",".",".",".",".",".","B"]], rMove = 4, cMove = 4, color = "W"
Output: false
Explanation: While there are good lines with the chosen cell as a middle cell, there are no good lines with the chosen cell as an endpoint.


Constraints:

board.length == board[r].length == 8
0 <= rMove, cMove < 8
board[rMove][cMove] == '.'
color is either 'B' or 'W'.
'''

from typing import *

import unittest


class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        directions = (
            (-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, 1), (1, -1), (-1, -1), (1, 1)
        )
        row = len(board)
        col = len(board[0])
        board[rMove][cMove] = color

        for x_d, y_d in directions:
            start_x = rMove
            start_y = cMove
            count = 0
            length = 0
            while start_x >= 0 and start_x < row and start_y >= 0 and start_y < col:
                if board[start_x][start_y] == '.':
                    break
                count += (board[start_x][start_y] == color)
                length += 1
                start_x += x_d
                start_y += y_d
                if count == 2:
                    if length >= 3:
                        return True
                    break
        return False



class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            # (([[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],["W","B","B",".","W","W","W","B"],[".",".",".","B",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."]], 4, 3, "B"), True),
            (([[".",".","W",".","B","W","W","B"],
                ["B","W",".","W",".","W","B","B"],
                [".","W","B","W","W",".","W","W"],
                ["W","W",".","W",".",".","B","B"],
                ["B","W","B","B","W","W","B","."],
                ["W",".","W",".",".","B","W","W"],
                ["B",".","B","B",".",".","B","B"],
                [".","W",".","W",".","W",".","W"]], 5, 4, "W"), True),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().checkMove(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
