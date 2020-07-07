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


// Given a string s, partition s such that every substring of the partition is a palindrome.

// Return all possible palindrome partitioning of s.

// Example:

// Input: "aab"
// Output:
// [
//   ["aa","b"],
//   ["a","a","b"]
// ]


class Solution {
public:
    vector<vector<string>> partition(string s) {
        int size = s.length();
        vector<vector<vector<string>>> dp(size+1, vector<vector<string>>(size+1, 
            vector<string>()
        ));

        for (int col = 1; col < size + 1; col++) {
            for (int row = col - 1; row >= 0; row--) {
                if (row == col - 1) {
                    dp[row][col].push_back("");
                    continue;
                }
                unordered_set<string> res;
                for (int i = 1; i < col; i++) {
                    auto left = dp[row][i];
                    auto right = dp[i][col];

                    for (int left_i = 0; left_i < left.size(); left_i++) {
                        for (int right_i = 0; right_i < right.size(); right_i++) {
                            res.insert(left[left_i] + "0" + right[right_i]);
                        }
                    }
                }

                // judge if thw whole word is palindrome
                if (s[row] == s[col-1] && (row+1 == col-1 || !dp[row+1][col-1].empty())) {
                    res.insert(string(col-row-1, '1'));
                }

                for (auto iter = res.begin(); iter != res.end(); iter++) {
                    dp[row][col].push_back(*iter);
                }
            }
        }

        vector<vector<string>> real_result;
        vector<string> result;
        for (auto iter = dp[0][size].begin(); iter != dp[0][size].end(); iter++) {
            int start = 0;
            for (int i = 0; i < iter->size(); i++) {
                if ((*iter)[i] == '0') {
                    result.push_back(s.substr(start, i-start+1));
                    start = i+1;
                }
            }
            result.push_back(s.substr(start));
            real_result.push_back(result);
            result.clear();
        }
        return real_result;
    }


    vector<vector<string>> partitionNew(string s) {
        vector<vector<string>> res;
        if (s.empty()) {
            return res;
        }
        vector<string> path;
        backtrace(res, path, s, 0);
        return res;
    }

    void backtrace(vector<vector<string>> &res, vector<string> &path, string &s, 
                int start) {
        if (start == s.length()) {
            res.push_back(path);
            return;
        }

        for (int i = start; i < s.length(); i++) {
            if (isPalindorme(s, start, i)) {
                path.push_back(s.substr(start, i - start + 1));
                backtrace(res, path, s, i+1);
                path.pop_back();
            }
        }
    }

    bool isPalindorme(string &word, int start, int end) {
        while (start < end) {
            if (word[start++] != word[end--]) {
                return false;
            }
        }
        return true;
    }
};

int main() {
    Solution s;
    auto res = s.partitionNew("aab");
    for (auto e: res) {
        for (auto l: e) {
            cout << l << ',';
        }
        cout << endl;
    };
}