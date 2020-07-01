#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;

// You are given an n x n 2D matrix representing an image.

// Rotate the image by 90 degrees (clockwise).

// Note:

// You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

// Example 1:

// Given input matrix = 
// [
//   [1,2,3],
//   [4,5,6],
//   [7,8,9]
// ],

// rotate the input matrix in-place such that it becomes:
// [
//   [7,4,1],
//   [8,5,2],
//   [9,6,3]
// ]
// Example 2:

// Given input matrix =
// [
//   [ 5, 1, 9,11],
//   [ 2, 4, 8,10],
//   [13, 3, 6, 7],
//   [15,14,12,16]
// ], 

// rotate the input matrix in-place such that it becomes:
// [
//   [15,13, 2, 5],
//   [14, 3, 4, 1],
//   [12, 6, 8, 9],
//   [16, 7,10,11]
// ]

class Solution {
public:
    void transfer(vector<vector<int>> &matrix, int row, int col, int size, int x, int y) {
        for (int i = row; i < row+size; i++) {
            for (int j = col; j < col+size; j++) {
                matrix[i+x][j+y] = matrix[i][j];
            }
        }
    }

    void rotate(vector<vector<int>>& matrix) {
        core_rotate(matrix, 0, 0, matrix.size());
    }

    void core_rotate(vector<vector<int>>& matrix, int row, int col, int size) {
        if (size <= 1) {
            return;
        }

        vector<int> tmp(matrix[row].begin(), matrix[row].begin() + size - 1);
        transfer(matrix, row + 1, col, size - 1, -1, 0);
        
        for (int i = size - 1; i >= 0; i--) {
            matrix[row + size - 1][col + size - 1 - i] = matrix[row + i][col + size - 1];
        }

        for (int k = 0; k < size - 1; k++ ) {
            matrix[row + k][col + size - 1] = tmp[k];
        }
        core_rotate(matrix, row, col, size - 1);
    }
};

int main() {
    Solution s;
    vector<vector<int>> array= {
        {2,29,20,26,16,28},
        {12,27,9,25,13,21},
        {32,33,32,2,28,14},
        {13,14,32,27,22,26},
        {33,1,20,7,21,7},
        {4,24,1,6,32,34}
    };
    s.rotate(array);
    for (auto e: array) {
        for (auto l: e) {
            cout << l << ',';
        }
        cout << endl;
    }
}
