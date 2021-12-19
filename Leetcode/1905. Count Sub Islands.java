import java.util.*;

// You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.

// An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.

// Return the number of islands in grid2 that are considered sub-islands.

 

// Example 1:


// Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
// Output: 3
// Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
// The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.
// Example 2:


// Input: grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
// Output: 2 
// Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
// The 1s colored red in grid2 are those considered to be part of a sub-island. There are two sub-islands.
 

// Constraints:

// m == grid1.length == grid2.length
// n == grid1[i].length == grid2[i].length
// 1 <= m, n <= 500
// grid1[i][j] and grid2[i][j] are either 0 or 1.

class Solution1905 {
    public int countSubIslands(int[][] grid1, int[][] grid2) {
        int row = grid2.length;
        int col = grid2[0].length;

        int res = 0;
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (grid2[i][j] == 1 && visit(i, j, row, col, grid1, grid2)) {
                    res++;
                }
            }
        }
        return res;
    }

    public boolean visit(int i, int j, int row, int col, int[][] grid1, int[][] grid2) {
        grid2[i][j] = 0;
        boolean res = grid1[i][j] == 1;
        for (int[] direction: new int[][] {{-1, 0}, {1, 0}, {0, 1}, {0, -1}}) {
            int x = i + direction[0];
            int y = j + direction[1];
            if (x >= 0 && x < row && y >= 0 && y < col && grid2[x][y] == 1) {
                res &= visit(x, y, row, col, grid1, grid2);
            }
        }
        return res;
    }
}

class Driver1905 {
    public static void main(String[] args) {
        int[][] grid1 = {{1,1,1,0,0},{0,1,1,1,1},{0,0,0,0,0},{1,0,0,0,0},{1,1,0,1,1}};
        int[][] grid2 = {{1,1,1,0,0},{0,0,1,1,1},{0,1,0,0,0},{1,0,1,1,0},{0,1,0,1,0}};
        System.out.println((new Solution1905()).countSubIslands(grid1, grid2));
    }
}