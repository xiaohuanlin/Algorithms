#include <vector>
#include <iostream>
#include <tuple>
#include <assert.h>
using namespace std;

// Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

 

// Example 1:


// Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
// Output: [1,2,4,7,5,3,6,8,9]
// Example 2:

// Input: mat = [[1,2],[3,4]]
// Output: [1,2,3,4]
 

// Constraints:

// m == mat.length
// n == mat[i].length
// 1 <= m, n <= 10^4
// 1 <= m * n <= 10^4
// -10^5 <= mat[i][j] <= 10^5

class Solution {
public:
    using Direction = pair<int, int>;

    vector<int> findDiagonalOrder(vector<vector<int>>& mat) {
        Direction direct = {-1, 1};
        int count = 0;
        int x = 0, y = 0;
        int x_max = mat.size() - 1;
        int y_max = mat[0].size() - 1;
        int size = mat.size() * mat[0].size();
        vector<int> res;
        while (count < size) {
            res.push_back(mat[x][y]);
            x += direct.first;
            y += direct.second;

            bool over_max_x = x > x_max;
            bool over_max_y = y > y_max;
            bool less_zero_x = x < 0;
            bool less_zero_y = y < 0;

            bool has_changed = false;

            if (less_zero_x) {
                if (!over_max_y) {
                    x = 0;
                }
                changeDirection(direct, has_changed);
            } else if (over_max_x) {
                x = x_max;
                y += 2;
                changeDirection(direct, has_changed);
            }

            if (less_zero_y) {
                if (!over_max_x) {
                    y = 0;
                }
                changeDirection(direct, has_changed);
            } else if (over_max_y) {
                y = y_max;
                x += 2;
                changeDirection(direct, has_changed);
            }
            count++;
        }
        return res;
    }

    void changeDirection(Direction &direct, bool &has_changed) {
        if (!has_changed) {
            direct.second *= -1;
            direct.first *= -1;
            has_changed = true;
        }
    }
};

int main() {
    Solution s;
    vector<tuple<vector<vector<int>>, vector<int>>> test_cases {
        {{{1}}, {1}},
        {{{1}, {2}}, {1, 2}},
        {{{1, 2}}, {1, 2}},
        {{{1,2,3},{4,5,6},{7,8,9}}, {1,2,4,7,5,3,6,8,9}},
        {{{1,2},{3,4}}, {1,2,3,4}}
    };

    for (auto& test_case: test_cases) {
        assert(s.findDiagonalOrder(get<0>(test_case)) == get<1>(test_case));
    }
}