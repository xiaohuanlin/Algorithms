#include <vector>
#include <stack>
#include <unordered_map>
#include <algorithm>
#include <iostream>
#include <tuple>
#include <assert.h>
using namespace std;

// Given a balanced parentheses string s, return the score of the string.

// The score of a balanced parentheses string is based on the following rule:

// "()" has score 1.
// AB has score A + B, where A and B are balanced parentheses strings.
// (A) has score 2 * A, where A is a balanced parentheses string.
 

// Example 1:

// Input: s = "()"
// Output: 1
// Example 2:

// Input: s = "(())"
// Output: 2
// Example 3:

// Input: s = "()()"
// Output: 2
// Example 4:

// Input: s = "(()(()))"
// Output: 6
 

// Constraints:

// 2 <= s.length <= 50
// s consists of only '(' and ')'.
// s is a balanced parentheses string.


class Solution {
public:
    int scoreOfParentheses(string s) {
        stack<int> counts;
        unordered_map<int, int> values;

        int count = 0;
        for (int i = 0; i < s.length(); ++i) {
            if (s[i] == '(') {
                count++;
            } else {
                int value = values[count];
                if (value == 0) {
                    value = 1;
                } else {
                    value *= 2;
                }

                // clean current lenth sum
                values[count] = 0;

                count--;
                // add the right result to left 
                values[count] += value;
            }
        }
        return values[0];
    }
};


int main() {
    Solution s;
    vector<tuple<string, int>> test_cases {
        {{"()"}, 1},
        {{"(())"}, 2},
        {{"()()"}, 2},
        {{"(()(()))"}, 6},
        {{"(())()"}, 3},
    };

    for (auto& test_case: test_cases) {
        assert(s.scoreOfParentheses(get<0>(test_case)) == get<1>(test_case));
    }
}