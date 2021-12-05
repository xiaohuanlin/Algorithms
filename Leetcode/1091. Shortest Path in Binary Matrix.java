import java.util.*;

// Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

// A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

// All the visited cells of the path are 0.
// All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
// The length of a clear path is the number of visited cells of this path.

 

// Example 1:


// Input: grid = [[0,1],[1,0]]
// Output: 2
// Example 2:


// Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
// Output: 4
// Example 3:

// Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
// Output: -1
 

// Constraints:

// n == grid.length
// n == grid[i].length
// 1 <= n <= 100
// grid[i][j] is 0 or 1

class Solution1091 {
    public int shortestPathBinaryMatrix(int[][] grid) {
        int row = grid.length;
        int col = grid[0].length;
        int[][] directions = new int[][] {
            {-1, -1}, {-1, 0}, {-1, 1},
            {0, -1}, {0, 1},
            {1, -1}, {1, 0}, {1, 1},
        };

        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[] {0, 0});
        int steps = 1;
        while (!q.isEmpty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                int[] pair = q.poll();
                int x = pair[0];
                int y = pair[1];
                if (grid[x][y] == 1) {
                    continue;
                }
                if (x == row - 1 && y == col - 1) {
                    return steps;
                }
                grid[x][y] = 1;
                for (int[] direction: directions) {
                    int xNew = x + direction[0];
                    int yNew = y + direction[1];
                    if (xNew >= 0 && xNew < row && yNew >= 0 && yNew < col) {
                        q.offer(new int[] {xNew, yNew});
                    }
                }
            }
            steps++;
        }
        return -1;
    }
}

class Driver1091 {
    public static void main(String[] args) {
        int[][] grid = {{0,0,0},{1,1,0},{1,1,0}};
        System.out.println((new Solution1091()).shortestPathBinaryMatrix(grid));
    }
}