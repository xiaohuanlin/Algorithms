#include <stack>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;

// Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

// Integers in each row are sorted from left to right.
// The first integer of each row is greater than the last integer of the previous row.
// Example 1:

// Input:
// matrix = [
//   [1,   3,  5,  7],
//   [10, 11, 16, 20],
//   [23, 30, 34, 50]
// ]
// target = 3
// Output: true
// Example 2:

// Input:
// matrix = [
//   [1,   3,  5,  7],
//   [10, 11, 16, 20],
//   [23, 30, 34, 50]
// ]
// target = 13
// Output: false


class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int start = 0;
        int end = matrix.size() - 1;

        if (matrix.empty()) {
            return false;
        }

        if (matrix[0].empty()) {
            return false;
        }
        
        while (start < end) {
            int middle = start + (end - start) / 2;

            if (matrix[middle][0] == target) {
                return true;
            } else if (matrix[middle][0] > target) {
                end = middle - 1;
            } else {
                if (matrix[middle + 1][0] <= target) {
                    start = middle + 1;
                } else {
                    if (middle == start) {
                        break;
                    }
                    start = middle;
                }
            }
        }

        int row = start;
        start = 0;
        end = matrix[0].size() - 1;
        while (start < end) {
            int middle = start + (end - start) / 2;

            if (matrix[row][middle] == target) {
                return true;
            } else if (matrix[row][middle] > target) {
                end = middle - 1;
            } else {
                start = middle + 1;
            }
        }

        return matrix[row][start] == target;
    }

    bool searchMatrixNew(vector<vector<int>>& matrix, int target) {
        int m = matrix.size();
        if (m == 0) {
            return false;
        }
        int n = matrix[0].size();
        if (n == 0) {
            return false;
        }
        int start = 0;
        int end = m*n - 1;
        while (start <= end) {
            int middle = start + (end -start) / 2;
            int middle_value = matrix[middle / n][middle % n];
            if (middle_value == target) {
                return true;
            } else if (middle_value > target) {
                end = middle - 1;
            } else {
                start = middle + 1;
            }
        }
        return false;
    }
};

int main() {
    Solution s;
    vector<vector<int>> array = {
        {1, 3}
    };
    cout << s.searchMatrix(array, 3);
}