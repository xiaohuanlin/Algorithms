import java.lang.reflect.Array;
import java.util.*;

// You are given an m x n integer matrix points (0-indexed). Starting with 0 points, you want to maximize the number of points you can get from the matrix.

// To gain points, you must pick one cell in each row. Picking the cell at coordinates (r, c) will add points[r][c] to your score.

// However, you will lose points if you pick a cell too far from the cell that you picked in the previous row. For every two adjacent rows r and r + 1 (where 0 <= r < m - 1), picking cells at coordinates (r, c1) and (r + 1, c2) will subtract abs(c1 - c2) from your score.

// Return the maximum number of points you can achieve.

// abs(x) is defined as:

// x for x >= 0.
// -x for x < 0.
 

// Example 1:


// Input: points = [[1,2,3],[1,5,1],[3,1,1]]
// Output: 9
// Explanation:
// The blue cells denote the optimal cells to pick, which have coordinates (0, 2), (1, 1), and (2, 0).
// You add 3 + 5 + 3 = 11 to your score.
// However, you must subtract abs(2 - 1) + abs(1 - 0) = 2 from your score.
// Your final score is 11 - 2 = 9.
// Example 2:


// Input: points = [[1,5],[2,3],[4,2]]
// Output: 11
// Explanation:
// The blue cells denote the optimal cells to pick, which have coordinates (0, 1), (1, 1), and (2, 0).
// You add 5 + 3 + 4 = 12 to your score.
// However, you must subtract abs(1 - 1) + abs(1 - 0) = 1 from your score.
// Your final score is 12 - 1 = 11.
 

// Constraints:

// m == points.length
// n == points[r].length
// 1 <= m, n <= 105
// 1 <= m * n <= 105
// 0 <= points[r][c] <= 105

class Solution1937 {
    public long maxPoints(int[][] points) {
        int row = points.length;
        int col = points[0].length;
        long[] currentDp = new long[col];
        long[] leftMax = new long[col + 1];
        long[] rightMax = new long[col + 1];

        for (int i = 0; i < col; i++) {
            currentDp[i] = points[0][i];
        }

        for (int i = 1; i < row; i++) {
            // calculate max value from left side
            leftMax[0] = -col;
            for (int j = 1; j < col + 1; j++) {
                leftMax[j] = Math.max(leftMax[j - 1], currentDp[j - 1] - (col - j));
            }

            // calculate max value from right side
            rightMax[col] = -col;
            for (int j = col - 1; j >= 0; j--) {
                rightMax[j] = Math.max(rightMax[j + 1], currentDp[j] - j);
            }

            for (int j = 0; j < col; j++) {
                currentDp[j] = Math.max(Math.max(leftMax[j] + (col - j - 1), rightMax[j + 1] + j), currentDp[j]) + points[i][j];
            }
        }

        long max = 0;
        for (int i = 0; i < col; i++) {
            max = Math.max(max, currentDp[i]);
        }
        return max;
    }
}

class Driver1937 {
    public static void main(String[] args) {
        int[][] points = {{0,3,0,4,2},{5,4,2,4,1},{5,0,0,5,1},{2,0,1,0,3}};
        System.out.println(new Solution1937().maxPoints(points));
    }
}