#include <unordered_map>
#include <unordered_set>
#include <math.h>
#include <utility>
#include <stack>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;


// Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

// The distance between two adjacent cells is 1.

 

// Example 1:

// Input:
// [[0,0,0],
//  [0,1,0],
//  [0,0,0]]

// Output:
// [[0,0,0],
//  [0,1,0],
//  [0,0,0]]
// Example 2:

// Input:
// [[0,0,0],
//  [0,1,0],
//  [1,1,1]]

// Output:
// [[0,0,0],
//  [0,1,0],
//  [1,2,1]]
 

// Note:

// The number of elements of the given matrix will not exceed 10,000.
// There are at least one 0 in the given matrix.
// The cells are adjacent in only four directions: up, down, left and right.


class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& matrix) {
        if (matrix.empty()) {
            return matrix;
        }

        vector<pair<int,int>> candidates, next;        
        int row = matrix.size();
        int col = matrix[0].size();
        vector<vector<int>> res(row, vector<int>(col, -1));

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (matrix[i][j] == 0) {
                    candidates.push_back(make_pair(i, j));
                }
            }
        }

        int dis = 0;
        while (!candidates.empty()) {
            while (!candidates.empty()) {
                auto node = candidates.back();
                candidates.pop_back();

                if (node.first >= 0 && node.first < row && node.second >= 0 
                    && node.second < col && res[node.first][node.second] == -1) {
                        res[node.first][node.second] = dis;
                        next.push_back(make_pair(node.first-1, node.second));
                        next.push_back(make_pair(node.first, node.second-1));
                        next.push_back(make_pair(node.first, node.second+1));
                        next.push_back(make_pair(node.first+1, node.second));
                    }
            }
            candidates = next;
            next.clear();
            dis++;
        }
        return res;
    }
};


int main() {
    Solution s;
    vector<vector<int>> array {
        {0,0,0},
        {0,1,0},
        {1,1,1}
    };
    auto res = s.updateMatrix(array);
    for (auto e: res) {
        for (auto l: e) {
            cout << l << ',';
        }
        cout << endl;
    }
}