// Write a program to solve a Sudoku puzzle by filling the empty cells.

// A sudoku solution must satisfy all of the following rules:

// Each of the digits 1-9 must occur exactly once in each row.
// Each of the digits 1-9 must occur exactly once in each column.
// Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
// The '.' character indicates empty cells.

 

// Example 1:


// Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
// Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
// Explanation: The input board is shown above and the only valid solution is shown below:


 

// Constraints:

// board.length == 9
// board[i].length == 9
// board[i][j] is a digit or '.'.
// It is guaranteed that the input board has only one solution.


class Solution37 {
    public void solveSudoku(char[][] board) {
        traceBack(board, 0);
    }

    public boolean traceBack(char[][] board, int pos) {
        if (pos == 81) {
            return true;
        }

        int x = pos / 9;
        int y = pos % 9;

        if (board[x][y] != '.') {
            return traceBack(board, pos+1);
        }

        for (int i = 1; i < 10; i++) {
            char candidate = (char)(i + '0');
            if (isValid(board, candidate, x, y)) {
                board[x][y] = candidate;
                if (traceBack(board, pos+1)) {
                    return true;
                }
                board[x][y] = '.';
            }
        }
        return false;
    }

    public boolean isValid(char[][] board, char candidate, int x, int y) {
        for (int i = 0; i < 9; i++) {
            if (board[i][y] == candidate) {
                return false;
            }
        }

        for (int j = 0; j < 9; j++) {
            if (board[x][j] == candidate) {
                return false;
            }
        }

        int row = x / 3;
        int col = y / 3;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (board[3 * row + i][3 * col + j] == candidate) {
                    return false;
                }
            }
        }
        return true;
    }
}

class Driver37 {
    public static void main(String[] args) {
        Solution37 solution = new Solution37();

        char[][] board = {{'5','3','.','.','7','.','.','.','.'},{'6','.','.','1','9','5','.','.','.'},{'.','9','8','.','.','.','.','6','.'},{'8','.','.','.','6','.','.','.','3'},{'4','.','.','8','.','3','.','.','1'},{'7','.','.','.','2','.','.','.','6'},{'.','6','.','.','.','.','2','8','.'},{'.','.','.','4','1','9','.','.','5'},{'.','.','.','.','8','.','.','7','9'}};
        solution.solveSudoku(board);
        for (char[] v: board) {
            System.out.println(v);
        }
    }
}