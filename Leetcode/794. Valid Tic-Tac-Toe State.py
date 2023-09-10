'''
Given a Tic-Tac-Toe board as a string array board, return true if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.

The board is a 3 x 3 array that consists of characters ' ', 'X', and 'O'. The ' ' character represents an empty square.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares ' '.
The first player always places 'X' characters, while the second player always places 'O' characters.
'X' and 'O' characters are always placed into empty squares, never filled ones.
The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
 

Example 1:


Input: board = ["O  ","   ","   "]
Output: false
Explanation: The first player always plays "X".
Example 2:


Input: board = ["XOX"," X ","   "]
Output: false
Explanation: Players take turns making moves.
Example 3:


Input: board = ["XOX","O O","XOX"]
Output: true
 

Constraints:

board.length == 3
board[i].length == 3
board[i][j] is either 'X', 'O', or ' '.
'''
from typing import *

import unittest


class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        count_x = 0
        count_y = 0

        for s in board:
            count_x += s.count('X')
            count_y += s.count('O')
        
        def game_over(symbol):
            for s in board:
                if s[0] == symbol and s[1] == symbol and s[2] == symbol:
                    return True
            for i in range(len(board[0])):
                if board[0][i] == symbol and board[1][i] == symbol and board[2][i] == symbol:
                    return True
            
            if (board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol) or \
                (board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol):
                return True
            return False
        
        if count_x == count_y:
            if game_over('X'):
                return False
            return True
        elif count_x == count_y + 1:
            if game_over('O'):
                return False
            return True
        else:
            return False

        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((["XOX"," X ","   "],),False),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().validTicTacToe(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
