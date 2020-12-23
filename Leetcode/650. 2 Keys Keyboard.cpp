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

// Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step:

// Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
// Paste: You can paste the characters which are copied last time.
 

// Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted. Output the minimum number of steps to get n 'A'.

// Example 1:

// Input: 3
// Output: 3
// Explanation:
// Intitally, we have one character 'A'.
// In step 1, we use Copy All operation.
// In step 2, we use Paste operation to get 'AA'.
// In step 3, we use Paste operation to get 'AAA'.
 

// Note:

// The n will be in the range [1, 1000].

class Solution {
public:
    int minSteps(int n) {
        vector<vector<pair<int, int>>> dp(n + 1, vector<pair<int,int>>());
        dp[1] = {};
        for (int i = 1; i < dp.size(); ++i) {
            auto paths = dp[i];
            int min_v = INT32_MAX;
            for (int j = 0; j < paths.size(); ++j) {
                int last_paste_v = paths[j].first;
                int min_times = paths[j].second;
                if (i + last_paste_v < dp.size()) {
                    dp[i + last_paste_v].push_back({last_paste_v, min_times + 1});
                }
                if (min_times < min_v) {
                    min_v = min_times;
                }
            }

            if (min_v == INT32_MAX) {
                min_v = 0;
            }
            if (i + i < dp.size()) {
                dp[i + i].push_back({i, min_v + 2});
            }
            if (dp.size() - 1 == i) {
                return min_v;
            }
        }
        return 0;
    }
};

int main() {
    Solution s;
    cout << s.minSteps(1) << endl;
}