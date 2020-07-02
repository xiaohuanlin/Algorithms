#include <stack>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;

// A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

// The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

// Now consider if some obstacles are added to the grids. How many unique paths would there be?



// An obstacle and empty space is marked as 1 and 0 respectively in the grid.

// Note: m and n will be at most 100.

// Example 1:

// Input:
// [
//   [0,0,0],
//   [0,1,0],
//   [0,0,0]
// ]
// Output: 2
// Explanation:
// There is one obstacle in the middle of the 3x3 grid above.
// There are two ways to reach the bottom-right corner:
// 1. Right -> Right -> Down -> Down
// 2. Down -> Down -> Right -> Right
 
class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) { 
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();
        vector<vector<int>> dp(m, vector<int>(n, 0));

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (obstacleGrid[i][j] == 1) {
                    continue;
                }
                int left_value = j == 0 ? 0: dp[i][j-1];
                int up_value = i == 0 ? 0: dp[i-1][j];
                if (i == 0 && j == 0) {
                    dp[i][j] = 1;
                } else {
                    dp[i][j] = left_value + up_value;
                }
            }
        }
        return dp[m-1][n-1];
    }
};

int main() {
    Solution s;
    vector<vector<int>> array = {
        {0, 1, 0},
        {0, 1, 0},
        {0, 0, 0}
    };
    cout << s.uniquePathsWithObstacles(array);
}
