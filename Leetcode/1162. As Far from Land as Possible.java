import java.util.*;

// Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.

// The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

 

// Example 1:


// Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
// Output: 2
// Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.
// Example 2:


// Input: grid = [[1,0,0],[0,0,0],[0,0,0]]
// Output: 4
// Explanation: The cell (2, 2) is as far as possible from all the land with distance 4.
 

// Constraints:

// n == grid.length
// n == grid[i].length
// 1 <= n <= 100
// grid[i][j] is 0 or 1

class Solution1162 {
    public int maxDistance(int[][] grid) {
        Queue<Integer> q = new LinkedList<>();
        int row = grid.length;
        int col = grid[0].length;
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (grid[i][j] == 1) {
                    q.offer(i * row + j);
                }
            }
        }

        if (q.size() == row * col) {
            return -1;
        }

        Set<Integer> memory = new HashSet<>();
        int distance = -1;
        int[][] directions = {
            {-1, 0},
            {1, 0},
            {0, 1},
            {0, -1},
        };
        while (!q.isEmpty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                int num = q.poll();
                int x = num / row;
                int y = num % row;

                for (int[] direction: directions) {
                    int newX = x + direction[0];
                    int newY = y + direction[1];
                    int newNum = newX * row + newY;
                    if (memory.contains(newNum)) {
                        continue;
                    }

                    if (newX >= 0 && newX < row && newY >= 0 && newY < col && grid[newX][newY] == 0) {
                        q.offer(newNum);
                        memory.add(newNum);
                    }
                }
            }
            distance++;
        }
        return distance;
    }
}

class Driver1162 {
    public static void main(String[] args) {
        Solution1162 solution = new Solution1162();

        int[][] grid = {{1,0,0},{0,0,0},{0,0,0}};
        System.out.println(solution.maxDistance(grid));
    }
}