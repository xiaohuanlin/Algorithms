#include <vector>
#include <stack>
#include <iostream>
#include <tuple>
#include <assert.h>
#include <algorithm>
using namespace std;

// You are given two strings order and s. All the words of order are unique and were sorted in some custom order previously.

// Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.

// Return any permutation of s that satisfies this property.

 

// Example 1:

// Input: order = "cba", s = "abcd"
// Output: "cbad"
// Explanation: 
// "a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a". 
// Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.
// Example 2:

// Input: order = "cbafg", s = "abcd"
// Output: "cbad"
 

// Constraints:

// 1 <= order.length <= 26
// 1 <= s.length <= 200
// order and s consist of lowercase English letters.
// All the characters of order are unique.


class Solution {
public:
    string customSortString(string order, string s) {
        vector<int> count(26, 0);
        for (auto& c : s) {
            ++count[c - 'a'];
        }

        // set the order string first
        string res;
        res.reserve(s.length());
        for (auto& c : order) {
            for (int i = 0; i < count[c - 'a']; ++i) {
                res.push_back(c);
            }
            count[c - 'a'] = 0;
        }

        // set others
        for (int j = 0; j < count.size(); ++j) {
            for (int i = 0; i < count[j]; ++i) {
                res.push_back(j + 'a');
            }
        }
        return res;
    }
};


int main() {
    Solution s;
    vector<tuple<tuple<string, string>, string>> test_cases {
        {{"cba", "abcd"}, "cbad"},
        {{"cbafg", "abcd"}, "cbad"},
        {{"a", "bcd"}, "bcd"},
    };

    for (auto& test_case: test_cases) {
        assert(s.customSortString(get<0>(get<0>(test_case)), get<1>(get<0>(test_case))) == get<1>(test_case));
    }
}