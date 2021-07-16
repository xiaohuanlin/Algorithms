#include <vector>
#include <iostream>
#include <tuple>
#include <assert.h>
using namespace std;

// Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

// An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

// s = s1 + s2 + ... + sn
// t = t1 + t2 + ... + tm
// |n - m| <= 1
// The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
// Note: a + b is the concatenation of strings a and b.

 

// Example 1:


// Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
// Output: true
// Example 2:

// Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
// Output: false
// Example 3:

// Input: s1 = "", s2 = "", s3 = ""
// Output: true
 

// Constraints:

// 0 <= s1.length, s2.length <= 100
// 0 <= s3.length <= 200
// s1, s2, and s3 consist of lowercase English letters.
 

// Follow up: Could you solve it using only O(s2.length) additional memory space?


class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        int size1 = s1.length();
        int size2 = s2.length();
        int size3 = s3.length();

        if (size1 + size2 != size3) {
            return false;
        }

        if ((size1 == size3 && size2 == 0 && s1 == s3) ||
            (size2 == size3 && size1 == 0 && s2 == s3)) {
            return true;
        }

        // make the question become small: Is s3.substr(length) is interleaving when s1.substr(i) and
        // s2.substr(length-i)
        vector<vector<bool>> dp(size1 + 1, vector<bool>(size2 + 1, false));
        dp[0][0] = true;
        for (int length = 1; length < size3 + 1; ++length) {
            for (int i = 0; i < size1 + 1; ++i) {
                int left_x = i;
                int left_y = length - i - 1;
                int upper_x = i - 1;
                int upper_y = length - i;

                if ((isValidPosition(upper_x, upper_y, size1 + 1, size2 + 1) && dp[upper_x][upper_y] == true && s3[length - 1] == s1[upper_x]) ||
                    (isValidPosition(left_x, left_y, size1 + 1, size2 + 1) && dp[left_x][left_y] == true && s3[length - 1] == s2[left_y])) {
                    dp[i][length - i] = true;
                }
            }
        }
        return dp[size1][size2];
    }

    bool isValidPosition(int x, int y, int x_size, int y_size) {
        return x >= 0 && x < x_size && y >= 0 && y < y_size;
    }
};

int main() {
    Solution s;
    vector<tuple<string, string, string, bool>> test_cases {
        {"", "", "", true},
        {"", "", "a", false},
        {"a", "b", "", false},
        {"a", "a", "a", false},
        {"a", "ba", "aab", false},
        {"aab", "dbb", "aadbbb", true},
        {"aabcc", "dbbca", "aadbbcbcac", true},
        {"aabcc", "dbbca", "aadbbbaccc", false},
    };

    for (auto& test_case: test_cases) {
        assert(s.isInterleave(get<0>(test_case), get<1>(test_case), get<2>(test_case)) == get<3>(test_case));
    }
}