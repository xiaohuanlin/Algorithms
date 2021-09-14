#include <vector>
#include <stack>
#include <unordered_map>
#include <algorithm>
#include <iostream>
#include <tuple>
#include <assert.h>
using namespace std;

// Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

// A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

// For example, "ace" is a subsequence of "abcde".
// A common subsequence of two strings is a subsequence that is common to both strings.

 

// Example 1:

// Input: text1 = "abcde", text2 = "ace" 
// Output: 3  
// Explanation: The longest common subsequence is "ace" and its length is 3.
// Example 2:

// Input: text1 = "abc", text2 = "abc"
// Output: 3
// Explanation: The longest common subsequence is "abc" and its length is 3.
// Example 3:

// Input: text1 = "abc", text2 = "def"
// Output: 0
// Explanation: There is no such common subsequence, so the result is 0.
 

// Constraints:

// 1 <= text1.length, text2.length <= 1000
// text1 and text2 consist of only lowercase English characters.


class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        vector<vector<int>> dp(text1.size() + 1, vector<int>(text2.size() + 1, 0));

        for (int i = text1.size() - 1; i >= 0; i--) {
            for (int j = text2.size() - 1; j >= 0; j--) {
                 if (text1[i] == text2[j]) {
                     dp[i][j] = 1 + dp[i+1][j+1];
                 } else {
                     dp[i][j] = max(dp[i+1][j], dp[i][j+1]);
                 }
            }
        }
        return dp[0][0];
    }
};

int main() {
    Solution s;
    vector<tuple<tuple<string, string>, int>> test_cases {
        {{"abcde", "ace"}, 3},
        {{"abc", "abc"}, 3},
        {{"abc", "def"}, 0},
    };

    for (auto& test_case: test_cases) {
        assert(s.longestCommonSubsequence(get<0>(get<0>(test_case)), get<1>(get<0>(test_case))) == get<1>(test_case));
    }
}