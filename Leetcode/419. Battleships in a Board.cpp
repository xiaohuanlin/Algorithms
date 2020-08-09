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
#include <queue>
using namespace std;


// Given an 2D board, count how many battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. You may assume the following rules:
// You receive a valid board, made of only battleships or empty slots.
// Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
// At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.
// Example:
// X..X
// ...X
// ...X
// In the above board there are 2 battleships.
// Invalid Example:
// ...X
// XXXX
// ...X
// This is an invalid board that you will not receive - as battleships will always have a cell separating between them.
// Follow up:
// Could you do it in one-pass, using only O(1) extra memory and without modifying the value of the board?


class Solution {
public:
    int countBattleships(vector<vector<char>>& board) {
        if (board.empty()) {
            return 0;
        }

        int count = 0;

        vector<pair<vector<int>, vector<int>>> ban;
        for (int i = 0; i < board.size(); i++) {
            for (int j = 0; j < board[0].size(); j++) {
                bool ignore = false;
                for (auto &two_p: ban) {
                    if (i >= two_p.first[0] && i <= two_p.second[0] && 
                        j >= two_p.first[1] && j <= two_p.second[1]) {
                        ignore = true;
                        break;
                    }
                }

                if (!ignore && board[i][j] == 'X') {
                    // find right down
                    int row = i;
                    int col = j;
                    while (row < board.size() && board[row][col] == 'X') {
                        row++;
                    }
                    row--;
                    while (col < board[0].size() && board[row][col] == 'X') {
                        col++;
                    }
                    col--;
                    ban.push_back(make_pair(vector<int>{i, j}, vector<int>{row, col}));
                }
            }
        }
        return ban.size();
    }
};

int main() {
    Solution s;
    vector<vector<char>> array = {
        {'X','.','.','X'},
        {'X','.','.','X'},
        {'X','.','.','X'},
    };
    cout << s.countBattleships(array);
}
