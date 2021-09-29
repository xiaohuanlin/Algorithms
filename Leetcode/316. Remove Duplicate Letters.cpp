#include <algorithm>
#include <bitset>
#include <vector>
#include <math.h>
#include <deque>
#include <tuple>
#include <unordered_map>
#include <assert.h>
using namespace std;


// Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

 

// Example 1:

// Input: s = "bcabc"
// Output: "abc"
// Example 2:

// Input: s = "cbacdcbc"
// Output: "acdb"
 

// Constraints:

// 1 <= s.length <= 104
// s consists of lowercase English letters.
 

// Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/


class Solution {
public:
    string removeDuplicateLetters(string s) {
        deque<int> res;
        vector<int> counts(26, 0);
        for (auto& c: s) {
            counts[c - 'a']++;
        }
        bitset<26> includes(0);

        for (int i = 0; i < s.length(); i++) {
            counts[s[i] - 'a']--;
            // ignore the number that has been included
            if (includes[s[i] - 'a']) {
                continue;
            }
            // remove the smaller one and add bigger one. It is required that the smaller one should appear one more time.
            while (!res.empty() && s[res.back()] > s[i] && counts[s[res.back()] - 'a'] > 0) {
                includes[s[res.back()] - 'a'] = false;
                res.pop_back();
            }

            res.push_back(i);
            includes[s[i] - 'a'] = true;
        }
        
        string ans;
        while (!res.empty()) {
            ans += s[res.front()];
            res.pop_front();
        }
        return ans;
    }
};

int main() {
    Solution s;
    vector<tuple<string, string>> test_cases {
        {"a", "a"},
        {"bcabc", "abc"},
        {"cbacdcbc", "acdb"},
        {"leetcode", "letcod"}
    };

    for (auto& test_case: test_cases) {
        assert(s.removeDuplicateLetters(get<0>(test_case)) == get<1>(test_case));
    }
}