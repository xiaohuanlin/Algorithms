#include <stack>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;

// A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

// The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

// How many possible unique paths are there?


// Above is a 7 x 3 grid. How many possible unique paths are there?

 
class Solution {
public:
    int uniquePaths(int m, int n) {
        int high = 1;
        int low = 1;
        int size = m > n ? n - 1:m - 1;

        return CombineNum(m + n - 2, size);
    }

    int CombineNum(int m, int n) {
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));

        for (int i = 0; i < m + 1; i++) {
            for (int j = 0; j < n + 1; j++) {
                if (j > i) {
                    continue;
                }
                if (i == j || j == 0) {
                    dp[i][j] = 1;
                } else {
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1];
                }
            }
        }
        return dp[m][n];
    }
};

int main() {
    Solution s;
    cout << s.uniquePaths(7, 3);
}
