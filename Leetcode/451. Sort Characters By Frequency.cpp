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
#include <queue>
using namespace std;


// Given a string, sort it in decreasing order based on the frequency of characters.

// Example 1:

// Input:
// "tree"

// Output:
// "eert"

// Explanation:
// 'e' appears twice while 'r' and 't' both appear once.
// So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
// Example 2:

// Input:
// "cccaaa"

// Output:
// "cccaaa"

// Explanation:
// Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
// Note that "cacaca" is incorrect, as the same characters must be together.
// Example 3:

// Input:
// "Aabb"

// Output:
// "bbAa"

// Explanation:
// "bbaA" is also a valid answer, but "Aabb" is incorrect.
// Note that 'A' and 'a' are treated as two different characters.


class Solution {
    struct Node {
        char w;
        int count;
    };
public:
    string frequencySort(string s) {
        vector<pair<int, char>> res(256, {0, 0});
        for (auto e: s) {
            res[e].first++;
            res[e].second = e;
        }
        sort(res.begin(), res.end(), greater<pair<int, char>>());

        string ans(s.length(), '0');

        int count = 0;
        for (auto &e: res) {
            if (e.first == 0) {
                break;
            }
            for (int i = 0; i < e.first; ++i) {
                ans[count++] = e.second;
            }
        }
        return ans;
    }
};

int main() {
    Solution s;
    cout << s.frequencySort("tree");
}
