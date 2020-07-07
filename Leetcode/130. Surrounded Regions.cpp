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


// Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

// A region is captured by flipping all 'O's into 'X's in that surrounded region.

// Example:

// X X X X
// X O O X
// X X O X
// X O X X
// After running your function, the board should be:

// X X X X
// X X X X
// X X X X
// X O X X
// Explanation:

// Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.



class Solution {
public:
    void solve(vector<vector<char>>& board) {
        if (board.empty()) {
            return;
        }
        int row = board.size();
        if (board[0].empty()) {
            return;
        }
        int col = board[0].size();

        set<pair<int, int>> points;
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (board[i][j] == 'O') {
                    points.insert(make_pair(i, j));
                }
            }
        }

        stack<pair<int, int>> candidates;

        while (!points.empty()) {
            bool to_board = false;
            set<pair<int, int>> tmp;

            candidates.push(*points.begin());
            tmp.insert(*points.begin());
            points.erase(points.begin());

            while (!candidates.empty()) {
                auto item = candidates.top();
                candidates.pop();

                int ori_row = item.first;
                int ori_col = item.second;
                if (ori_row <= 0 || ori_col <= 0 || ori_row >= row - 1 || ori_col >= col - 1) {
                    to_board = true;
                }

                if (ori_row > 0) {
                    pair<int, int> unit(ori_row - 1, ori_col);
                    if (board[ori_row-1][ori_col] == 'O') {
                        if (points.find(unit) != points.end()) {
                            points.erase(points.find(unit));
                            candidates.push(unit);
                            tmp.insert(unit);
                        }
                    }
                }

                if (ori_col > 0) {
                    pair<int, int> unit(ori_row, ori_col - 1);
                    if (board[ori_row][ori_col-1] == 'O') {
                        if (points.find(unit) != points.end()) {
                            points.erase(points.find(unit));
                            candidates.push(unit);
                            tmp.insert(unit);
                        }
                    }
                }
                if (ori_row < row - 1) {
                    pair<int, int> unit(ori_row + 1, ori_col);
                    if (board[ori_row+1][ori_col] == 'O') {
                        if (points.find(unit) != points.end()) {
                            points.erase(points.find(unit));
                            candidates.push(unit);
                            tmp.insert(unit);
                        }
                    }
                }
                if (ori_col < col - 1) {
                    pair<int, int> unit(ori_row, ori_col + 1);
                    if (board[ori_row][ori_col+1] == 'O') {
                        if (points.find(unit) != points.end()) {
                            points.erase(points.find(unit));
                            candidates.push(unit);
                            tmp.insert(unit);
                        }
                    }
                }
            }
            if (!to_board) {
                for (auto iter = tmp.begin(); iter != tmp.end(); iter++) {
                    board[iter->first][iter->second] = 'X';
                }
            }
        }
    }
};

int main() {
    Solution s;
    vector<vector<char>> array = {
        {'X', 'X', 'X', 'X'},
        {'X', 'O', 'O', 'X'},
        {'X', 'O', 'X', 'X'},
        {'X', 'X', 'O', 'X'},
    };
    s.solve(array);
    for (auto e: array) {
        for (auto l: e) {
            cout << l << ',';
        }
        cout << endl;
    };
}