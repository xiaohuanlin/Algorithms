#include <vector>
#include <stack>
#include <unordered_map>
#include <algorithm>
#include <iostream>
#include <tuple>
#include <assert.h>
using namespace std;

// A parentheses string is valid if and only if:

// It is the empty string,
// It can be written as AB (A concatenated with B), where A and B are valid strings, or
// It can be written as (A), where A is a valid string.
// You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

// For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
// Return the minimum number of moves required to make s valid.

 

// Example 1:

// Input: s = "())"
// Output: 1
// Example 2:

// Input: s = "((("
// Output: 3
// Example 3:

// Input: s = "()"
// Output: 0
// Example 4:

// Input: s = "()))(("
// Output: 4
 

// Constraints:

// 1 <= s.length <= 1000
// s[i] is either '(' or ')'.


class Solution {
public:
    int minAddToMakeValid(string s) {
        int sum = 0;
        int move = 0;
        for (auto& c : s) {
            if (c == '(') {
                sum++;
            } else {
                if (sum == 0) {
                    // we need add '(' signal to make it balance
                    move++;
                } else {
                    sum--;
                }
            }
        }
        return move + sum;
    }
};


int main() {
    Solution s;
    vector<tuple<string, int>> test_cases {
        {"())", 1},
        {")(", 2},
        {"(((", 3},
        {"()", 0},
        {"()))((", 4},
    };

    for (auto& test_case: test_cases) {
        assert(s.minAddToMakeValid(get<0>(test_case)) == get<1>(test_case));
    }
}