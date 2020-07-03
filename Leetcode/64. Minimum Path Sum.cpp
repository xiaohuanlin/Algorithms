#include <stack>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;

// Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

// Note: You can only move either down or right at any point in time.

// Example:

// Input:
// [
//   [1,3,1],
//   [1,5,1],
//   [4,2,1]
// ]
// Output: 7
// Explanation: Because the path 1→3→1→1→1 minimizes the sum.

class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int max_row = grid.size();
        int max_col = grid[0].size();
        vector<vector<int>> res(max_row, vector<int>(max_col, 0));

        for (int i = 0; i < max_row; i++) {
            for (int j = 0; j < max_col; j++) {
                if (i == 0 && j == 0) {
                    res[i][j] = grid[i][j];
                    continue;
                }
                int up_value = i == 0 ? 0x7fffffff: res[i-1][j]; 
                int left_value = j == 0 ? 0x7fffffff: res[i][j-1]; 
                res[i][j] = grid[i][j] + (left_value < up_value ? left_value: up_value);
            }
        }
        return res[max_row-1][max_col-1];
    }

    int minPathSumNew(vector<vector<int>>& grid) {
        if (grid.empty()) {
            return -1;
        }
        int row = grid.size();

        if (grid[0].empty()) {
            return -1;
        }
        int col = grid[0].size();

        vector<int> res(col + 1, INT32_MAX);
        res[1] = 0;

        for (int i = 1; i <= row; i++) {
            for (int j = 1; j <= col; j++) {
                res[j] = min(res[j-1], res[j]) + grid[i-1][j-1];
            }
        }
        return res[col];
    }
};

int main() {
    Solution s;
    vector<vector<int>> array = {
        {1, 3, 1},
        {1, 5, 1},
        {4, 2, 1}
    };
    cout << s.minPathSumNew(array);
}