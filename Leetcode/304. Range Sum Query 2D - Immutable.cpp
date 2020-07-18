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

// Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

// Range Sum Query 2D
// The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

// Example:
// Given matrix = [
//   [3, 0, 1, 4, 2],
//   [5, 6, 3, 2, 1],
//   [1, 2, 0, 1, 5],
//   [4, 1, 0, 1, 7],
//   [1, 0, 3, 0, 5]
// ]

// sumRegion(2, 1, 4, 3) -> 8
// sumRegion(1, 1, 2, 2) -> 11
// sumRegion(1, 2, 2, 4) -> 12
// Note:
// You may assume that the matrix does not change.
// There are many calls to sumRegion function.
// You may assume that row1 ≤ row2 and col1 ≤ col2.

class NumMatrix {
	bool empty;
	vector<vector<int>> dps;
public:
    NumMatrix(vector<vector<int>>& matrix) {
		int row = matrix.size();
		if (row == 0) {
			empty = true;
		} else {
			int col = matrix[0].size();
			if (col == 0) {
				empty = true;
			} else {
				dps.resize(row+1);
				for (int i = 0; i < row+1; i++) {
					dps[i].resize(col+1);
					for (int j = 0; j < col+1; j++) {
						if (i == 0 || j == 0) {
							dps[i][j] = 0;
						} else {
							dps[i][j] = dps[i][j-1] + dps[i-1][j] + matrix[i-1][j-1] - dps[i-1][j-1];
						}
					}
				}
			}
		}
    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {
		return dps[row2+1][col2+1] + dps[row1][col1] - dps[row2+1][col1] - dps[row1][col2+1];
    }
};

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix* obj = new NumMatrix(matrix);
 * int param_1 = obj->sumRegion(row1,col1,row2,col2);
 */


int main() {
	vector<vector<int>> array = {
		{1,2,3},
		{1,2,3},
		{1,2,3},
	};

	NumMatrix* obj = new NumMatrix(array);
 	cout << obj->sumRegion(1,1,1,1);
}