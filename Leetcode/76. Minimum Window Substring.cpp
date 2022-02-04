#include <vector>
#include <queue>
#include <unordered_map>
#include <iostream>
#include <tuple>
#include <assert.h>
#include <algorithm>
using namespace std;

// Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

// The testcases will be generated such that the answer is unique.

// A substring is a contiguous sequence of characters within the string.

 

// Example 1:

// Input: s = "ADOBECODEBANC", t = "ABC"
// Output: "BANC"
// Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
// Example 2:

// Input: s = "a", t = "a"
// Output: "a"
// Explanation: The entire string s is the minimum window.
// Example 3:

// Input: s = "a", t = "aa"
// Output: ""
// Explanation: Both 'a's from t must be included in the window.
// Since the largest window of s only has one 'a', return empty string.
 

// Constraints:

// m == s.length
// n == t.length
// 1 <= m, n <= 105
// s and t consist of uppercase and lowercase English letters.
 

// Follow up: Could you find an algorithm that runs in O(m + n) time?

class Solution {
public:
    string minWindow(string s, string t) {
        unordered_map<char, int> maps;
        for (char c: t) {
            maps[c]++;
        }

        int left = 0;
        int right = 0;

        int min = INT32_MAX;
        pair<int, int> min_pair = {0, 0};

        while (right < s.length()) {
            if (maps.count(s[right])) {
                maps[s[right]]--;
            }
            right++;

            while (left <= right && validate(maps)) {
                if (right - left < min) {
                    min_pair = {left, right - left};
                    min = right - left;
                }

                if (maps.count(s[left])) {
                    maps[s[left]]++;
                }
                left++;
            }
        }
        return s.substr(min_pair.first, min_pair.second);
    }

    bool validate(unordered_map<char,int>& maps) {
        for (auto pair: maps) {
            if (pair.second > 0) {
                return false;
            }
        }
        return true;
    }
};

int main() {
    Solution s;
    vector<
        tuple<
            tuple<string, string>, 
            string
        >
    > test_cases {
        {
            {"ADOBECODEBANC", "ABC"},
            "BANC"
        },
        {
            {"a", "a"},
            "a"
        },
        {
            {"a", "aa"},
            ""
        },
        {
            {"abc", "b"},
            "b"
        },
    };

    for (auto& test_case: test_cases) {
        assert(s.minWindow(
                    get<0>(get<0>(test_case)),
                    get<1>(get<0>(test_case))
                ) == get<1>(test_case)
        );
    }
}