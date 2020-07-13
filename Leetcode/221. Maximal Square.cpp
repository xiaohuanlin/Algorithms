#include <unordered_set>
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


// Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

// Example:

// Input: 

// 1 0 1 0 0
// 1 0 1 1 1
// 1 1 1 1 1
// 1 0 0 1 0

// Output: 4


class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        int row = matrix.size();
        if (row == 0) {
            return 0;
        }
        int col = matrix[0].size();
        if (col == 0) {
            return 0;
        }
        vector<vector<int>> edge(row, vector<int>(col, 0));
        int size = 0;

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                // for edge of right-down point
                if (i == 0 || j == 0 || matrix[i][j] == '0') {
                    edge[i][j] = matrix[i][j] - '0';
                } else {
                    edge[i][j] = min(edge[i-1][j-1], min(edge[i-1][j], edge[i][j-1])) + 1;
                }

                size = max(size, edge[i][j]);
            }
        }

        return size * size;
    }
};


int main() {
    Solution s;
    vector<vector<char>> array = {
        {'0','0','0','1'},
        {'1','1','0','1'},
        {'1','1','1','1'},
        {'0','1','1','1'},
        {'0','1','1','1'},
    };
    cout << s.maximalSquare(array);

}
