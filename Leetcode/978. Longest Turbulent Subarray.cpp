#include <vector>
#include <algorithm>
#include <iostream>
#include <tuple>
#include <assert.h>
using namespace std;


// Given an integer array arr, return the length of a maximum size turbulent subarray of arr.

// A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

// More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:

// For i <= k < j:
// arr[k] > arr[k + 1] when k is odd, and
// arr[k] < arr[k + 1] when k is even.
// Or, for i <= k < j:
// arr[k] > arr[k + 1] when k is even, and
// arr[k] < arr[k + 1] when k is odd.
 

// Example 1:

// Input: arr = [9,4,2,10,7,8,8,1,9]
// Output: 5
// Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]
// Example 2:

// Input: arr = [4,8,12,16]
// Output: 2
// Example 3:

// Input: arr = [100]
// Output: 1
 

// Constraints:

// 1 <= arr.length <= 4 * 10^4
// 0 <= arr[i] <= 10^9


class Solution {
    enum class State {
        kNegtive,
        kNormal,
        kPositive
    };

public:
    int maxTurbulenceSize(vector<int>& arr) {
        int result = INT32_MIN;
        int count = 0;
        State state = State::kNormal;
        for (int i = 0; i < arr.size() - 1; i++) {
            int delta = arr[i+1] - arr[i];

            if (delta == 0) {
                result = max(result, count);
                count = 0;
                state = State::kNormal;
                continue;
            }

            if ((state == State::kPositive && delta > 0)
                || (state == State::kNegtive && delta < 0)) {
                result = max(result, count);
                count = 1;
            } else {
                count++;
            }
            
            if (delta == 0) {
                state = State::kNormal;
            } else if (delta > 0) {
                state = State::kPositive;
            } else {
                state = State::kNegtive;
            }
        }

        result = max(result, count);
        return result + 1;
    }
};

int main() {
    Solution s;
    vector<tuple<vector<int>, int>> test_cases {
        {{1, 1, 1}, 1},
        {{9,4,2,10,7,8,8,1,9}, 5},
        {{4,8,12,16}, 2},
        {{100}, 1},
    };

    for (auto& test_case: test_cases) {
        assert(s.maxTurbulenceSize(get<0>(test_case)) == get<1>(test_case));
    }
}