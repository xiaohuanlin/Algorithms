#include <vector>
#include <array>
#include <tuple>
#include <assert.h>
#include <algorithm>
using namespace std;

// Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

// Return any possible rearrangement of s or return "" if not possible.

 

// Example 1:

// Input: s = "aab"
// Output: "aba"
// Example 2:

// Input: s = "aaab"
// Output: ""
 

// Constraints:

// 1 <= s.length <= 500
// s consists of lowercase English letters.

class Solution {
public:
    string reorganizeString(string s) {
        using Item = pair<char, int>;
        array<int, 26> counts_map {};
        int max_count = 0;
        for (auto& c : s) {
            max_count = max(max_count, ++counts_map[c - 'a']);
        }

        // the max char exceed the half of whole chars
        if ((s.length() + 1) / 2 < max_count) {
            return "";
        }

        vector<Item> counts;
        for (int i = 0; i < 26; i++) {
            if (counts_map[i] > 0) {
                counts.push_back({'a' + i, counts_map[i]});
            }
        }


        auto cmp = [] (Item& a, Item& b) {
            return a.second < b.second;
        };

        make_heap(counts.begin(), counts.end(), cmp);

        string res {};

        for (int i = 0; i < s.length(); i+=2) {
            if (counts.empty()) {
                break;
            }

            Item item1, item2 {};
            item1 = counts.front();
            pop_heap(counts.begin(), counts.end(), cmp);
            counts.pop_back();
            res.push_back(item1.first);
            item1.second--;

            if (!counts.empty()) {
                item2 = counts.front();
                pop_heap(counts.begin(), counts.end(), cmp);
                counts.pop_back();
                res.push_back(item2.first);
                item2.second--;
            }

            if (item1.second > 0) {
                counts.push_back(item1);
                push_heap(counts.begin(), counts.end(), cmp);
            }

            if (item2.second > 0) {
                counts.push_back(item2);
                push_heap(counts.begin(), counts.end(), cmp);
            }
        }
        return res;
    }
};

int main() {
    Solution s;
    vector<tuple<string, string>> test_cases {
        {"eqmeyggvp", ""},
        {"aab", "aba"},
        {"aaab", ""},
    };

    for (auto& test_case: test_cases) {
        assert(s.reorganizeString(get<0>(test_case)) == get<1>(test_case));
    }
}