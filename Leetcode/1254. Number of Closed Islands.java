import java.util.*;

// Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

// Return the number of closed islands.

 

// Example 1:



// Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
// Output: 2
// Explanation: 
// Islands in gray are closed because they are completely surrounded by water (group of 1s).
// Example 2:



// Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
// Output: 1
// Example 3:

// Input: grid = [[1,1,1,1,1,1,1],
//                [1,0,0,0,0,0,1],
//                [1,0,1,1,1,0,1],
//                [1,0,1,0,1,0,1],
//                [1,0,1,1,1,0,1],
//                [1,0,0,0,0,0,1],
//                [1,1,1,1,1,1,1]]
// Output: 2
 

// Constraints:

// 1 <= grid.length, grid[0].length <= 100
// 0 <= grid[i][j] <=1


class Solution1254 {
    public int closedIsland(int[][] grid) {
        int row = grid.length;
        int col = grid[0].length;
        Stack<int[]> s = new Stack<>();

        for (int i: new int[] {0, row - 1}) {
            for (int j = 0; j < col; j++) {
                if (grid[i][j] == 0) {
                    s.push(new int[] {i, j});
                }
            }
        }

        for (int i = 0; i < row; i++) {
            for (int j: new int[] {0, col - 1}) {
                if (grid[i][j] == 0) {
                    s.push(new int[] {i, j});
                }
            }
        }

        // change 0 to 1
        while (!s.empty()) {
            int[] node = s.pop();
            int x = node[0];
            int y = node[1];
            
            if (grid[x][y] == 0) {
                grid[x][y] = 1;
                for (int[] delta: new int[][] {{0, 1}, {1, 0}, {-1, 0}, {0, -1}}) {
                    int nextX = x + delta[0];
                    int nextY = y + delta[1];
                    if (nextX >= 0 && nextX < row && nextY >= 0 && nextY < col) {
                        s.push(new int[] {nextX, nextY});
                    }
                }
            }
        }

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (grid[i][j] == 0) {
                    s.push(new int[] {i, j});
                }
            }
        }
        // find res
        int res = 0;
        while (!s.empty()) {
            Stack<int[]> tmp = new Stack<>();
            int[] ele = s.pop();
            if (grid[ele[0]][ele[1]] == 1) {
                continue;
            }

            tmp.push(ele);
            while (!tmp.empty()) {
                int[] node = tmp.pop();
                int x = node[0];
                int y = node[1];

                if (grid[x][y] == 0) {
                    grid[x][y] = 1;
                    for (int[] delta: new int[][] {{0, 1}, {1, 0}, {-1, 0}, {0, -1}}) {
                        int nextX = x + delta[0];
                        int nextY = y + delta[1];
                        if (nextX >= 0 && nextX < row && nextY >= 0 && nextY < col) {
                            tmp.push(new int[] {nextX, nextY});
                        }
                    }
                }
            }

            res++;
        }
        return res;
    }
}

class Driver1254 {
    public static void main(String[] args) {
        int[][] arr = {{1,1,1,1,1,1,1,0},{1,0,0,0,0,1,1,0},{1,0,1,0,1,1,1,0},{1,0,0,0,0,1,0,1},{1,1,1,1,1,1,1,0}};
        System.out.println((new Solution1254()).closedIsland(arr));
    }
}