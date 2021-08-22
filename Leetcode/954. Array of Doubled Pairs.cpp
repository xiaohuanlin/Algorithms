#include <vector>
#include <unordered_map>
#include <set>
#include <algorithm>
#include <iostream>
#include <tuple>
#include <assert.h>
using namespace std;


// Given an integer array of even length arr, return true if it is possible to reorder arr such that arr[2 * i + 1] = 2 * arr[2 * i] for every 0 <= i < len(arr) / 2, or false otherwise.

 

// Example 1:

// Input: arr = [3,1,3,6]
// Output: false
// Example 2:

// Input: arr = [2,1,2,6]
// Output: false
// Example 3:

// Input: arr = [4,-2,2,-4]
// Output: true
// Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].
// Example 4:

// Input: arr = [1,2,4,16,8,4]
// Output: false
 

// Constraints:

// 2 <= arr.length <= 3 * 10^4
// arr.length is even.
// -105 <= arr[i] <= 10^5


class Solution {
public:
    bool canReorderDoubled(vector<int>& arr) {
        sort(arr.begin(), arr.end(), [] (int a, int b) {
            return abs(a) < abs(b);
        });

        unordered_map<int, int> counts;
        for (auto& num: arr) {
            counts[num]++;
        }

        for (auto& num: arr) {
            if (counts[num] == 0) {
                continue;
            }

            counts[num]--;
            counts[2 * num]--;
            if (counts[2 * num] < 0) {
                return false;
            }
        }
        return true;
    }
};


int main() {
    Solution s;
    vector<tuple<vector<int>, bool>> test_cases {
        {{3,1,3,6}, false},
        {{0,1,3,0}, false},
        {{0,1,2,0}, true},
        {{2,1,2,6}, false},
        {{4,-2,2,-4}, true},
        {{1,2,4,16,8,4}, false},
    };

    for (auto& test_case: test_cases) {
        assert(s.canReorderDoubled(get<0>(test_case)) == get<1>(test_case));
    }
}