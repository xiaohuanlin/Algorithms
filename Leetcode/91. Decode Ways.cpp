#include <math.h>
#include <utility>
#include <stack>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;

// A message containing letters from A-Z is being encoded to numbers using the following mapping:

// 'A' -> 1
// 'B' -> 2
// ...
// 'Z' -> 26
// Given a non-empty string containing only digits, determine the total number of ways to decode it.

// Example 1:

// Input: "12"
// Output: 2
// Explanation: It could be decoded as "AB" (1 2) or "L" (12).
// Example 2:

// Input: "226"
// Output: 3
// Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

class Solution {
public:
    int numDecodings(string s) {
        if (s.empty()) {
            return 0;
        }
        stack<int> dfs;
        set<string> valid_item = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                                "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
                                "21", "22", "23", "24", "25", "26"};
        dfs.push(0);

        int count = 0;
        while (!dfs.empty()) {
            auto item = dfs.top();
            dfs.pop();
            
            if (item >= s.length()) {
                if (item == s.length()) {
                    count++;
                }
                continue;
            }

            if (valid_item.find(s.substr(item, 1)) != valid_item.end()) {
                dfs.push(item+1);
            }

            if (valid_item.find(s.substr(item, 2)) != valid_item.end()) {
                dfs.push(item+2);
            }
        }
        return count;
    }


    int numDecodingsNew(string s) {
        if (s.empty()) {
            return 0;
        }
        vector<int> dp(s.length() + 1, 1);

        for (int i = 1; i < dp.size(); i++) {
            int last_last_res = 0;
            int last_res = 0;
            if (i -2 >= 0 && isValid(s[i-2], s[i-1])) {
                last_last_res = dp[i-2];
            }
            if (isValid(s[i-1])) {
                last_res = dp[i-1];
            }
            dp[i] = last_res + last_last_res;
        }
        return dp[dp.size() - 1];
    }

    bool isValid(char a) {
        return a != '0';
    }

    bool isValid(char a, char b) {
        return a == '1' || (a == '2' && b - '0' <= 6);
    }
};

int main() {
    Solution s;
    cout << s.numDecodingsNew("222");
}