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


// Let's play the minesweeper game (Wikipedia, online game)!

// You are given a 2D char matrix representing the game board. 'M' represents an unrevealed mine, 'E' represents an unrevealed empty square, 'B' represents a revealed blank square that has no adjacent (above, below, left, right, and all 4 diagonals) mines, digit ('1' to '8') represents how many mines are adjacent to this revealed square, and finally 'X' represents a revealed mine.

// Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'), return the board after revealing this position according to the following rules:

// If a mine ('M') is revealed, then the game is over - change it to 'X'.
// If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B') and all of its adjacent unrevealed squares should be revealed recursively.
// If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
// Return the board when no more squares will be revealed.
 

// Example 1:

// Input: 

// [['E', 'E', 'E', 'E', 'E'],
//  ['E', 'E', 'M', 'E', 'E'],
//  ['E', 'E', 'E', 'E', 'E'],
//  ['E', 'E', 'E', 'E', 'E']]

// Click : [3,0]

// Output: 

// [['B', '1', 'E', '1', 'B'],
//  ['B', '1', 'M', '1', 'B'],
//  ['B', '1', '1', '1', 'B'],
//  ['B', 'B', 'B', 'B', 'B']]

// Explanation:

// Example 2:

// Input: 

// [['B', '1', 'E', '1', 'B'],
//  ['B', '1', 'M', '1', 'B'],
//  ['B', '1', '1', '1', 'B'],
//  ['B', 'B', 'B', 'B', 'B']]

// Click : [1,2]

// Output: 

// [['B', '1', 'E', '1', 'B'],
//  ['B', '1', 'X', '1', 'B'],
//  ['B', '1', '1', '1', 'B'],
//  ['B', 'B', 'B', 'B', 'B']]

// Explanation:

 

// Note:

// The range of the input matrix's height and width is [1,50].
// The click position will only be an unrevealed square ('M' or 'E'), which also means the input board contains at least one clickable square.
// The input board won't be a stage when game is over (some mines have been revealed).
// For simplicity, not mentioned rules should be ignored in this problem. For example, you don't need to reveal all the unrevealed mines when the game is over, consider any cases that you will win the game or flag any squares.

class Solution {
public:
    int calcu_mines(vector<vector<char>> &board, pair<int, int> &pos) {
        int sum = 0;
        int row = board.size();
        int col = board[0].size();
        if (pos.first - 1 >= 0) {
            if (pos.second - 1 >= 0) {
                sum += board[pos.first-1][pos.second-1] == 'M';
            }
            sum += board[pos.first-1][pos.second] == 'M';
            if (pos.second + 1 < col) {
                sum += board[pos.first-1][pos.second+1] == 'M';
            }
        }

        if (pos.second - 1 >= 0) {
            sum += board[pos.first][pos.second-1] == 'M';
        }
        if (pos.second + 1 < col) {
            sum += board[pos.first][pos.second+1] == 'M';
        }

        if (pos.first + 1 < row) {
            if (pos.second - 1 >= 0) {
                sum += board[pos.first+1][pos.second-1] == 'M';
            }
            sum += board[pos.first+1][pos.second] == 'M';
            if (pos.second + 1 < col) {
                sum += board[pos.first+1][pos.second+1] == 'M';
            }
        }
        return sum;
    }

    vector<vector<char>> updateBoard(vector<vector<char>>& board, vector<int>& click) {
        if (board.empty()) {
            return {};
        }
        int row = board.size();
        int col = board[0].size();
        vector<vector<char>> res(row, vector<char>(col, '\0'));

        if (board[click[0]][click[1]] == 'M') {
            res[click[0]][click[1]] = 'X';
        }
        stack<pair<int,int>> candidate;
        candidate.push(make_pair(click[0], click[1]));

        while (!candidate.empty()) {
            auto node = candidate.top();
            candidate.pop();

            if (node.first < row && node.first >= 0 
                && node.second < col && node.second >= 0
                && res[node.first][node.second] == '\0') {
                // calculate value
                int mine_num = calcu_mines(board, node);
                if (mine_num > 0) {
                    res[node.first][node.second] = mine_num + '0';
                } else {
                    res[node.first][node.second] = 'B';
                    // push node
                    candidate.push({node.first - 1, node.second - 1});
                    candidate.push({node.first - 1, node.second});
                    candidate.push({node.first - 1, node.second + 1});
                    candidate.push({node.first, node.second - 1});
                    candidate.push({node.first, node.second + 1});
                    candidate.push({node.first + 1, node.second - 1});
                    candidate.push({node.first + 1, node.second});
                    candidate.push({node.first + 1, node.second + 1});
                }
            }
        }

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (res[i][j] == '\0') {
                    res[i][j] = board[i][j];
                }
            }
        }
        return res;
    }
};

int main() {
    Solution s;
    vector<vector<char>> array = {
        {'E', 'E', 'E', 'E', 'E'},
        {'E', 'E', 'M', 'E', 'E'},
        {'E', 'E', 'E', 'E', 'E'},
        {'E', 'E', 'E', 'E', 'E'},
    };
    vector<int> click {3,0};
    auto res = s.updateBoard(array, click);
    for (auto e: res) {
        for (auto l: e) {
            cout << l << ',';
        }
        cout << endl;
    }
}