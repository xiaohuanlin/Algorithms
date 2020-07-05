#include <math.h>
#include <utility>
#include <stack>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;

// Given a string containing only digits, restore it by returning all possible valid IP address combinations.

// A valid IP address consists of exactly four integers (each integer is between 0 and 255) separated by single points.

// Example:

// Input: "25525511135"
// Output: ["255.255.11.135", "255.255.111.35"]


class Solution {
public:
    vector<string> restoreIpAddresses(string s) {
        stack<pair<int, vector<string>>> candidates;
        candidates.push(make_pair(0, vector<string>()));
        vector<string> res;

        while (!candidates.empty()) {
            auto item = candidates.top();
            candidates.pop();

            if (item.second.size() == 4 && item.first == s.length()) {
                string right_res;
                for (int i = 0; i < item.second.size(); i++) {
                    right_res += item.second[i];
                    if (i != item.second.size() - 1) {
                        right_res += '.';
                    }
                }
                res.push_back(right_res);
                continue;
            }

            if (item.first >= s.length() || item.second.size() >= 4) {
                continue;
            }

            item.second.push_back(s.substr(item.first, 1));
            candidates.push(make_pair(item.first+1, item.second));
            item.second.pop_back();

            if (item.first < s.length() - 1 && isValid(s[item.first], s[item.first+1])) {
                item.second.push_back(s.substr(item.first, 2));
                candidates.push(make_pair(item.first+2, item.second));
                item.second.pop_back();
            }

            if (item.first < s.length() - 2 && isValid(s[item.first], s[item.first+1], s[item.first+2])) {
                item.second.push_back(s.substr(item.first, 3));
                candidates.push(make_pair(item.first+3, item.second));
                item.second.pop_back();
            }
        }
        return res;
    }

    bool isValid(char a, char b) {
        return a != '0';
    }

    bool isValid(char a, char b, char c) {
        return (a == '1') || (a == '2' && (b - '0' < 5 || (b - '0' == 5 && c - '0' < 6)));
    }
};

int main() {
    Solution s;
    auto res = s.restoreIpAddresses("010010");
    for (auto e : res) {
        cout << e << ',';
    }
    cout << endl;
}