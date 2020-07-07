#include <unordered_map>
#include <math.h>
#include <utility>
#include <stack>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;


// Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

// For example, given the following triangle

// [
//      [2],
//     [3,4],
//    [6,5,7],
//   [4,1,8,3]
// ]
// The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

// Note:

// Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.


class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int min = INT32_MAX;
        backtrace(min, 0, triangle, 0, 0, triangle.size());
        return min;
    }

    void backtrace(int &min, int sum, vector<vector<int>> triangle,
                     int row, int col, int target) {
        if (row == target) {
            if (sum < min) {
                min = sum;
            }
            return;
        }

        sum += triangle[row][col];
        backtrace(min, sum, triangle, row+1, col, target);
        backtrace(min, sum, triangle, row+1, col+1, target);
    }

    int minimumTotalNew(vector<vector<int>>& triangle) {
        int size = triangle.size();
        if (size == 0) {
            return 0;
        }

        vector<vector<int>> dp(size+1, vector<int>(size+1, INT32_MAX));
        dp[1][1] = triangle[0][0];

        for (int row = 2; row < size + 1; row ++) {
            for (int col = 1; col < row + 1; col++) {
                int min_dis = dp[row-1][col] > dp[row-1][col-1] ? dp[row-1][col-1]: dp[row-1][col];
                dp[row][col] = min_dis + triangle[row-1][col-1];
            }
        }

        int min = dp[size][1];
        for (int i = 1; i < size + 1; i++) {
            if (min > dp[size][i]) {
                min = dp[size][i];
            }
        }
        return min;
    }
};

int main() {
    Solution s;
    vector<vector<int>> array = {
        {2},
        {3, 4},
        {6, 5, 7},
        {4, 1, 8, 3}
    };
    cout << s.minimumTotalNew(array);
}