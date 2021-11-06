#include <vector>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <iostream>
#include <tuple>
#include <assert.h>
using namespace std;

// A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

// Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.

 

// Example 1:


// Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
// Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
// Example 2:

// Input: mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]
// Output: [[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]
 

// Constraints:

// m == mat.length
// n == mat[i].length
// 1 <= m, n <= 100
// 1 <= mat[i][j] <= 100

class Solution {
public:
    vector<vector<int>> diagonalSort(vector<vector<int>>& mat) {
        int row = mat.size();
        int col = mat[0].size();
        
        unordered_set<int> starts;
        // first row
        for (int i = 0; i < col; i++) {
            starts.insert(i);
        }
        // first col
        for (int i = 0; i < row; i++) {
            starts.insert(i * col);
        }

        int end = row * col;
        for (int start: starts) {
            vector<int> array;
            int iter = start;
            while (iter < end) {
                array.push_back(mat[iter / col][iter % col]);
                iter = iter + col + 1;
                if (iter % col == 0) {
                    break;
                }
            }
            sort(array.begin(), array.end());

            iter = start;
            int index = 0;
            while (iter < end) {
                mat[iter / col][iter % col] = array[index++];
                iter = iter + col + 1;
                if (iter % col == 0) {
                    break;
                }
            }
        }
        return mat;
    }
};

int main() {
    Solution s;
    vector<tuple<vector<vector<int>>, vector<vector<int>>>> test_cases {
        // {{{3,3,1,1},{2,2,1,2},{1,1,1,2}}, {{1,1,1,1},{1,2,2,2},{1,2,3,3}}},
        {{{11,25,66,1,69,7},{23,55,17,45,15,52},{75,31,36,44,58,8},{22,27,33,25,68,4},{84,28,14,11,5,50}}, 
        {{5,17,4,1,52,7},{11,11,25,45,8,69},{14,23,25,44,58,15},{22,27,31,36,50,66},{84,28,75,33,55,68}}}
    };

    for (auto& test_case: test_cases) {
        assert(s.diagonalSort(get<0>(test_case)) == get<1>(test_case));
    }
}