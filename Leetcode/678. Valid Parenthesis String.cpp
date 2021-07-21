#include <vector>
#include <deque>
#include <tuple>
#include <unordered_map>
#include <assert.h>
using namespace std;

// Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

// The following rules define a valid string:

// Any left parenthesis '(' must have a corresponding right parenthesis ')'.
// Any right parenthesis ')' must have a corresponding left parenthesis '('.
// Left parenthesis '(' must go before the corresponding right parenthesis ')'.
// '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
 

// Example 1:

// Input: s = "()"
// Output: true
// Example 2:

// Input: s = "(*)"
// Output: true
// Example 3:

// Input: s = "(*))"
// Output: true
 

// Constraints:

// 1 <= s.length <= 100
// s[i] is '(', ')' or '*'.


class Solution {
public:
    bool checkValidString(string s) {
        int min_v = 0, max_v = 0;
        for (auto& c : s) {
            if (c == '(') {
                min_v++;
                max_v++;
            } else if (c == ')') {
                min_v--;
                max_v--;
            } else {
                min_v--;
                max_v++;
            }
            if (max_v < 0) {
                // for this condition, there is no path can make it become 0
                return false;
            }
            // we can't accept min_v less than 0. It is invalid.
            min_v = max(0, min_v);
        }
        return min_v == 0;
    }
};

int main() {
    Solution s;
    vector<tuple<string, bool>> test_cases {
        {"((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()", true},
        {"(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())", false},
        {"((*", false},
        {"(**(", false},
        {"()", true},
        {"(*)", true},
        {"*)", true},
        {"(*))", true},
        {")((*", false},
        {"()()", true},
        {"(())", true},
        {"*", true},
    };

    for (auto& test_case: test_cases) {
        assert(s.checkValidString(get<0>(test_case)) == get<1>(test_case));
    }
}