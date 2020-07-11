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


// Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

// Example 1:

// Input: grid = [
//   ["1","1","1","1","0"],
//   ["1","1","0","1","0"],
//   ["1","1","0","0","0"],
//   ["0","0","0","0","0"]
// ]
// Output: 1
// Example 2:

// Input: grid = [
//   ["1","1","0","0","0"],
//   ["1","1","0","0","0"],
//   ["0","0","1","0","0"],
//   ["0","0","0","1","1"]
// ]
// Output: 3


class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        stack<pair<int,int>> candidates;
        int count = 0;
        for (int i = 0; i < grid.size(); i++) {
            if (grid[i].empty()) {
                continue;
            }
            for (int j = 0; j < grid[i].size(); j++) {
                if (grid[i][j] == '1') {
                    // find all 1
                    candidates.push(make_pair(i, j));
                    while (!candidates.empty()) {
                        auto item = candidates.top();
                        candidates.pop();

                        int row = item.first, col = item.second;
                        if (row < 0 || row > grid.size() - 1 || col < 0 || col > grid[i].size() - 1) {
                            continue;
                        }
                        if (grid[row][col] == '1') {
                            grid[row][col] = '#';
                            candidates.push(make_pair(row-1, col));
                            candidates.push(make_pair(row+1, col));
                            candidates.push(make_pair(row, col-1));
                            candidates.push(make_pair(row, col+1));
                        }
                    }
                    count++;
                }
            }
        }
        return count;
    }
};


int main() {
    Solution s;
    vector<vector<char>> array = {
        {'1'}
    };
    cout << s.numIslands(array);
}