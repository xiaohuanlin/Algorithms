#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;

// Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

// Example 1:

// Input:
// [
//  [ 1, 2, 3 ],
//  [ 4, 5, 6 ],
//  [ 7, 8, 9 ]
// ]
// Output: [1,2,3,6,9,8,7,4,5]
// Example 2:

// Input:
// [
//   [1, 2, 3, 4],
//   [5, 6, 7, 8],
//   [9,10,11,12]
// ]
// Output: [1,2,3,4,8,12,11,10,9,5,6,7]

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> res;
        if (matrix.empty()) {
            return res;
        } else if (matrix[0].empty()) {
            return res;
        }
        int row_size = matrix.size();
        int col_size = matrix[0].size();

        getNums(matrix, res, 0, 0, row_size, col_size);
        return res;
    }

    void getNums(vector<vector<int>> &matrix, vector<int> &res, int row, int col, int row_size, int col_size) {
        if (row_size <= 2) {
            for (int i = col; i < col + col_size; i++) {
                res.push_back(matrix[row][i]);
            }
            if (row_size == 2) {
                for (int i = col + col_size - 1; i >= col; i--) {
                    res.push_back(matrix[row + 1][i]);
                }
            }
            return;
        }

        if (col_size <= 2) {
            if (col_size == 2) {
                res.push_back(matrix[row][col]);
            }
            for (int i = row; i < row + row_size; i++) {
                res.push_back(matrix[i][col + col_size - 1]);
            }
            if (col_size == 2) {
                for (int i = row + row_size - 1; i > row; i--) {
                    res.push_back(matrix[i][col]);
                }
            }
            return;
        }

        for (int i = col; i < col + col_size; i++) {
            res.push_back(matrix[row][i]);
        }

        for (int i = row + 1; i < row + row_size - 1; i++) {
            res.push_back(matrix[i][col + col_size - 1]);
        }

        for (int i = col + col_size - 1; i >= col; i--) {
            res.push_back(matrix[row + row_size - 1][i]);
        }

        for (int i = row + row_size - 2; i > row; i--) {
            res.push_back(matrix[i][col]);
        }

        getNums(matrix, res, row + 1, col + 1, row_size - 2, col_size - 2);
    }
};

int main() {
    Solution s;
    vector<vector<int>> array = {
    };
    auto res = s.spiralOrder(array);
    for (auto e: res) {
        cout << e;
    }
    cout << endl;
}
