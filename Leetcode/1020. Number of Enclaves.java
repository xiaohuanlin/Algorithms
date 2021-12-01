import java.util.*;

// You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

// A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

// Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

 

// Example 1:


// Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
// Output: 3
// Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.
// Example 2:


// Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
// Output: 0
// Explanation: All 1s are either on the boundary or can reach the boundary.
 

// Constraints:

// m == grid.length
// n == grid[i].length
// 1 <= m, n <= 500
// grid[i][j] is either 0 or 1.


class Solution1020 {
    public int numEnclaves(int[][] grid) {
        int row = grid.length;
        int col = grid[0].length;
        Stack<int[]> s = new Stack<>();
        for (int i: new int[] {0, row - 1}) {
            for (int j = 0; j < col; j++) {
                if (grid[i][j] == 1) {
                    s.push(new int[] {i, j});
                }
            }
        }
        for (int j: new int[] {0, col - 1}) {
            for (int i = 0; i < row; i++) {
                if (grid[i][j] == 1) {
                    s.push(new int[] {i, j});
                }
            }
        }

        while (!s.isEmpty()) {
            int[] pair = s.pop();
            if (grid[pair[0]][pair[1]] != 1) {
                continue;
            }
            grid[pair[0]][pair[1]] = -1;
            for (int[] direction: new int[][] {
                {1, 0},
                {0, 1},
                {-1, 0},
                {0, -1},
            }) {
                int x = pair[0] + direction[0];
                int y = pair[1] + direction[1];
                if (x > 0 && x < row && y > 0 && y < col && grid[x][y] == 1) {
                    s.push(new int[] {x, y});
                }
            }
        }
        
        int res = 0;
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (grid[i][j] == 1) {
                    res++;
                }
            }
        }
        return res;
    }
}

class Driver1020 {
    public static void main(String[] args) {
        int[][] grid = {{0,0,0,0},{1,0,1,0},{0,1,1,0},{0,0,0,0}};
        System.out.println((new Solution1020()).numEnclaves(grid));
    }
}