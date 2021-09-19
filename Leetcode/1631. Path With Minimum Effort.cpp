#include <vector>
#include <queue>
#include <unordered_map>
#include <iostream>
#include <tuple>
#include <assert.h>
#include <algorithm>
using namespace std;


// You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

// A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

// Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

 

// Example 1:



// Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
// Output: 2
// Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
// This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.
// Example 2:



// Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
// Output: 1
// Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].
// Example 3:


// Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
// Output: 0
// Explanation: This route does not require any effort.
 

// Constraints:

// rows == heights.length
// columns == heights[i].length
// 1 <= rows, columns <= 100
// 1 <= heights[i][j] <= 10^6


class Solution {
    struct Node {
        int row_;
        int col_;
        int effort_;
        Node(int row, int col, int effort): row_(row), col_(col), effort_(effort) {};
    };

public:
    int minimumEffortPath(vector<vector<int>>& heights) {
        int row = heights.size();
        int col = heights[0].size();
        vector<vector<int>> efforts(row, vector<int>(col, INT32_MAX));
        efforts[0][0] = 0;
        auto func = [] (const Node& a, const Node& b) {
            return a.effort_ > b.effort_;
        };
        priority_queue<Node, vector<Node>, decltype(func)> candidates(func);
        candidates.push({0, 0, 0});

        while (!candidates.empty()) {
            auto node = candidates.top();
            candidates.pop();

            if (node.row_ == row - 1 && node.col_ == col - 1) {
                return node.effort_;
            }

            if (efforts[node.row_][node.col_] < node.effort_) {
                continue;
            }

            for (auto& item: vector<vector<int>>{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}) {
                int next_row = node.row_ + item[0];
                int next_col = node.col_ + item[1];

                if (next_row >= 0 && next_row < row && next_col >= 0 && next_col < col) {
                    // we trace the max effort of this path
                    int next_effort = max(efforts[node.row_][node.col_], abs(heights[next_row][next_col] - heights[node.row_][node.col_]));

                    if (next_effort < efforts[next_row][next_col]) {
                        candidates.push({next_row, next_col, next_effort});
                        efforts[next_row][next_col] = next_effort;
                    }
                }
            }
        }
        return -1;
    }
};

int main() {
    Solution s;
    vector<tuple<vector<vector<int>>, int>> test_cases {
        {{{1,2,2},{3,8,2},{5,3,5}}, 2},
        {{{1,2,3},{3,8,4},{5,3,5}}, 1},
        {{{1,2,1,1,1},{1,2,1,2,1},{1,2,1,2,1},{1,2,1,2,1},{1,1,1,2,1}}, 0}
    };

    for (auto& test_case: test_cases) {
        assert(s.minimumEffortPath(get<0>(test_case)) == get<1>(test_case));
    }
}