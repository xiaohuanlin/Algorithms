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


// Implement a basic calculator to evaluate a simple expression string.

// The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

// Example 1:

// Input: "3+2*2"
// Output: 7
// Example 2:

// Input: " 3/2 "
// Output: 1
// Example 3:

// Input: " 3+5 / 2 "
// Output: 5
// Note:

// You may assume that the given expression is always valid.
// Do not use the eval built-in library function.


class Solution {
public:
    int calculate(string s) {
        deque<int64_t> values;
        deque<char> opers;

        int64_t sum = -1;
        int index = 0;

        char oper;
        while (index < s.length()) {
            while (index < s.length() && s[index] == ' ') {
                index++;
            }

            while (index < s.length() && s[index] >= '0' && s[index] <= '9') {
                if (sum == -1) {
                    sum = 0;
                }
                sum = sum * 10 + s[index++] - '0';
            }
            if (sum >= 0) {
                if (!opers.empty() && opers.back() == '*') {
                    opers.pop_back();
                    int64_t left = values.back();
                    values.pop_back();
                    values.push_back(left * sum);
                } else if (!opers.empty() && opers.back() == '/') {
                    opers.pop_back();
                    int64_t left = values.back();
                    values.pop_back();
                    values.push_back(left / sum);
                } else {
                    values.push_back(sum);
                }
                sum = 0;
            }

            while (index < s.length() && s[index] == ' ') {
                index++;
            }

            if (index < s.length() && (s[index] == '+' || s[index] == '-' || s[index] == '*' || s[index] == '/')) {
                opers.push_back(s[index++]);
            }
        }

        while (!opers.empty()) {
            int64_t left = values.front();
            values.pop_front();

            int64_t right = values.front();
            values.pop_front();

            char oper = opers.front();
            opers.pop_front();

            if (oper == '+') {
                values.push_front(left+right);
            } else {
                values.push_front(left-right);
            }
        }

        return values[0];
    }
};

int main() {
    Solution s;
    cout <<  s.calculate("0 + 1 * 5 / 2");
}