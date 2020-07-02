#include <stack>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;

// Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

// Example:

// Input: 3
// Output:
// [
//  [ 1, 2, 3 ],
//  [ 8, 9, 4 ],
//  [ 7, 6, 5 ]
// ]

class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> res(n, vector<int>(n, 0));

        vector<vector<int>> directions = {
            {0, 1},
            {1, 0},
            {0, -1},
            {-1, 0}
        };

        vector<int> nums = {n, n};
        
        int x = 0, y = -1;
        int count = 0;
        int num = 1;
        while (nums[count%2] > 0) {
            int x_change = directions[count % 4][0];
            int y_change = directions[count % 4][1];
            for (int i = 0; i < nums[count%2]; i++) {
                x += x_change;
                y += y_change;
                res[x][y] = num++;
            }
            count ++;
            nums[count%2]--;
        }
        return res;
    }
};

int main() {
    Solution s;
    auto res = s.generateMatrix(5);
    for (auto e : res) {
        for (auto l : e) {
            cout << l << ',';
        }
        cout << endl;
    }
}
