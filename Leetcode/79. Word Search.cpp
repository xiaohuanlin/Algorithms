#include <utility>
#include <stack>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;

// Given a 2D board and a word, find if the word exists in the grid.

// The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

// Example:

// board =
// [
//   ['A','B','C','E'],
//   ['S','F','C','S'],
//   ['A','D','E','E']
// ]

// Given word = "ABCCED", return true.
// Given word = "SEE", return true.
// Given word = "ABCB", return false.


class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        if (board.empty()) {
            return word.length() == 0;
        }

        if (board[0].empty()) {
            return word.length() == 0; 
        }

        for (int i = 0; i < board.size(); i++) {
            for (int j = 0; j < board[0].size(); j++) {
                if (board[i][j] == word[0]) {
                    board[i][j] = '*';
                    if (getExist(board, word, i, j, 1)) {
                        return true;
                    };
                    board[i][j] = word[0];
                }
            }
        }
        return false;
    }

    bool getExist(vector<vector<char>> &board, string &word, int x, int y, int target) {
        if (target == word.length()) {
            return true;
        }

        if (x < 0 || y < 0 || x > board.size() - 1 || y > board[0].size() - 1) {
            return false;
        }

        bool right_res = false, down_res = false, up_res = false, left_res = false;
        if (y < board[0].size() - 1 && board[x][y+1] == word[target] && board[x][y+1] != '*') {
            board[x][y+1] = '*';
            right_res = getExist(board, word, x, y+1, target+1);
            board[x][y+1] = word[target];
        }
        
        if (right_res) {
            return true;
        }
        
        if (x < board.size() - 1 && board[x+1][y] == word[target] && board[x+1][y] != '*') {
            board[x+1][y] = '*';
            down_res = getExist(board, word, x+1, y, target+1);
            board[x+1][y] = word[target];
        }
        if (down_res) {
            return true;
        }

        if (y > 0 && board[x][y-1] == word[target] && board[x][y-1] != '*') {
            board[x][y-1] = '*';
            left_res = getExist(board, word, x, y-1, target+1);
            board[x][y-1] = word[target];
        }
        if (left_res) {
            return true;
        }
        
        if (x > 0 && board[x-1][y] == word[target] && board[x-1][y] != '*') {
            board[x-1][y] = '*';
            up_res = getExist(board, word, x-1, y, target+1);
            board[x-1][y] = word[target];
        }
        if (up_res) {
            return true;
        }
        return false;
    }
};

int main() {
    Solution s;
    vector<vector<char>> array = {
        {'A', 'B', 'C', 'E'},
        {'S', 'F', 'C', 'S'},
        {'A', 'D', 'E', 'E'},
    };
    cout << s.exist(array, "SEE");
}