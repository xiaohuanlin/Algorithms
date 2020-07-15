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


// Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

// Integers in each row are sorted in ascending from left to right.
// Integers in each column are sorted in ascending from top to bottom.
// Example:

// Consider the following matrix:

// [
//   [1,   4,  7, 11, 15],
//   [2,   5,  8, 12, 19],
//   [3,   6,  9, 16, 22],
//   [10, 13, 14, 17, 24],
//   [18, 21, 23, 26, 30]
// ]
// Given target = 5, return true.

// Given target = 20, return false.


class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int row_size = matrix.size();
        if (row_size == 0) {
            return false;
        }
        int col_size = matrix[0].size();
        if (col_size == 0) {
            return false;
        }

        int row = row_size - 1;
        int col = 0;
        while (row >= 0 && col < col_size) {
            if (target > matrix[row][col]) {
                col++;
            } else if (target < matrix[row][col]) {
                row--;
            } else {
                return true;
            }
        }
        return false;
    }
};

int main() {
    Solution s;
    vector<vector<int>> array = {
        {1,1},
    };
    cout << s.searchMatrix(array, 4);

}