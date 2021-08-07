#include <vector>
#include <unordered_map>
#include <iostream>
#include <tuple>
#include <assert.h>
using namespace std;

// A sequence x1, x2, ..., xn is Fibonacci-like if:

// n >= 3
// xi + xi+1 == xi+2 for all i + 2 <= n
// Given a strictly increasing array arr of positive integers forming a sequence, return the length of the longest Fibonacci-like subsequence of arr. If one does not exist, return 0.

// A subsequence is derived from another sequence arr by deleting any number of elements (including none) from arr, without changing the order of the remaining elements. For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].

 

// Example 1:

// Input: arr = [1,2,3,4,5,6,7,8]
// Output: 5
// Explanation: The longest subsequence that is fibonacci-like: [1,2,3,5,8].
// Example 2:

// Input: arr = [1,3,7,11,12,14,18]
// Output: 3
// Explanation: The longest subsequence that is fibonacci-like: [1,11,12], [3,11,14] or [7,11,18].
 

// Constraints:

// 3 <= arr.length <= 1000
// 1 <= arr[i] < arr[i + 1] <= 10^9


class Solution {
public:
    int lenLongestFibSubseq(vector<int>& arr) {
        vector<vector<int>> dp(arr.size(), vector<int>(arr.size(), 0));
        unordered_map<int, int> maps;
        // record the index of the array
        for (int i = 0; i < arr.size(); i++) {
            maps[arr[i]] = i;
        }

        int max_v = 0;
        for (int i = 2; i < arr.size(); i++) {
            for (int j = 1; j < i; j++) {
                // for the last two number of subsequence(arr[j], arr[i]), it can represent the whole sequence
                int remain = arr[i] - arr[j];
                if (remain < arr[j] && maps.find(remain) != maps.end()) {
                    dp[j][i] = max(dp[j][i], dp[maps[remain]][j] >= 3 ? dp[maps[remain]][j] + 1 : 3);
                    max_v = max(max_v, dp[j][i]);
                }
            }
        }
        return max_v;
    }
};


int main() {
    Solution s;
    vector<tuple<vector<int>, int>> test_cases {
        // {{1,2,3,4,5,6,7,8}, 5},
        {{1,3,7,11,12,14,18}, 3},
    };

    for (auto& test_case: test_cases) {
        assert(s.lenLongestFibSubseq(get<0>(test_case)) == get<1>(test_case));
    }
}