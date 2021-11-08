#include <vector>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <iostream>
#include <tuple>
#include <assert.h>
using namespace std;

// Given two strings s and part, perform the following operation on s until all occurrences of the substring part are removed:

// Find the leftmost occurrence of the substring part and remove it from s.
// Return s after removing all occurrences of part.

// A substring is a contiguous sequence of characters in a string.

 

// Example 1:

// Input: s = "daabcbaabcbc", part = "abc"
// Output: "dab"
// Explanation: The following operations are done:
// - s = "daabcbaabcbc", remove "abc" starting at index 2, so s = "dabaabcbc".
// - s = "dabaabcbc", remove "abc" starting at index 4, so s = "dababc".
// - s = "dababc", remove "abc" starting at index 3, so s = "dab".
// Now s has no occurrences of "abc".
// Example 2:

// Input: s = "axxxxyyyyb", part = "xy"
// Output: "ab"
// Explanation: The following operations are done:
// - s = "axxxxyyyyb", remove "xy" starting at index 4 so s = "axxxyyyb".
// - s = "axxxyyyb", remove "xy" starting at index 3 so s = "axxyyb".
// - s = "axxyyb", remove "xy" starting at index 2 so s = "axyb".
// - s = "axyb", remove "xy" starting at index 1 so s = "ab".
// Now s has no occurrences of "xy".
 

// Constraints:

// 1 <= s.length <= 1000
// 1 <= part.length <= 1000
// s​​​​​​ and part consists of lowercase English letters.

class Solution {
public:
    string removeOccurrences(string s, string part) {
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '0') {
                continue;
            }

            int s_start = i;
            int part_start = 0;
            while (s_start < s.length() && part_start < part.length() && s[s_start] == part[part_start]) {
                while (s[++s_start] == '0');
                part_start++;
            }

            if (part_start == part.length()) {
                // remove it from string
                for (int j = i; j < s_start; j++) {
                    s[j] = '0';
                }
                // move forward part.length() - 1
                for (int count = 0; i >= 0 && count < static_cast<int>(part.length() - 1); count++) {
                    while (i >= 0 && s[i--] == '0');
                }
            }
        }

        string res;
        for (char c: s) {
            if (c != '0') {
                res.push_back(c);
            }
        }
        return res;
    }
};

int main() {
    Solution s;
    vector<tuple<tuple<string, string>, string>> test_cases {
        {{"daabcbaabcbc", "abc"}, "dab"},
        {{"axxxxyyyyb", "xy"}, "ab"}
    };

    for (auto& test_case: test_cases) {
        assert(s.removeOccurrences(get<0>(get<0>(test_case)), get<1>(get<0>(test_case))) == get<1>(test_case));
    }
}