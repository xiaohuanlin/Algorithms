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


// Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

// If the fractional part is repeating, enclose the repeating part in parentheses.

// Example 1:

// Input: numerator = 1, denominator = 2
// Output: "0.5"
// Example 2:

// Input: numerator = 2, denominator = 1
// Output: "2"
// Example 3:

// Input: numerator = 2, denominator = 3
// Output: "0.(6)"

 
class Solution {
public:

    string fractionToDecimal(int numerator, int denominator) {
        if (denominator == 0) {
            return "";
        }
        
        int64_t left_part = int64_t(numerator) / int64_t(denominator);
        int64_t remain = numerator - (denominator * left_part);

        unordered_map<string , int> maps;
        vector<char> res;
        while (remain) {
            int64_t current = remain * 10 / denominator;
            remain = (remain * 10) - denominator * current;
            res.push_back(abs(current) + '0');

            string search_key = to_string(current) + "-" + to_string(remain);
            if (maps.find(search_key) == maps.end()) {
                maps[search_key] = res.size() - 1;
            } else {
                res.pop_back();
                res.insert(res.begin() + maps[search_key], '(');
                res.push_back(')');
                break;
            }
        }

        string right_part;
        right_part.assign(res.begin(), res.end());

        if (res.empty()) {
            return to_string(left_part);
        } else {
            if (left_part == 0 && (numerator < 0) ^ (denominator < 0)) {
                return "-" + to_string(left_part) + "." + right_part;
            }
            return to_string(left_part) + "." + right_part;
        }
    }
};


int main() {
    Solution s;
    cout << s.fractionToDecimal(INT32_MIN, -1);
}