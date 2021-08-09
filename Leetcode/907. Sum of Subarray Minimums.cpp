#include <vector>
#include <stack>
#include <unordered_map>
#include <algorithm>
#include <iostream>
#include <tuple>
#include <assert.h>
using namespace std;

// Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 10^9 + 7.

 

// Example 1:

// Input: arr = [3,1,2,4]
// Output: 17
// Explanation: 
// Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
// Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
// Sum is 17.
// Example 2:

// Input: arr = [11,81,94,43,3]
// Output: 444
 

// Constraints:

// 1 <= arr.length <= 3 * 10^4
// 1 <= arr[i] <= 3 * 10^4


class Solution {
public:
    int sumSubarrayMins(vector<int>& arr) {
        stack<int> candidates;

        vector<int> pln(arr.size(), -1);
        vector<int> nln(arr.size(), arr.size());
        // find previous less number
        for (int i = 0; i < arr.size(); i++) {
            while (!candidates.empty() && arr[candidates.top()] > arr[i]) {
                candidates.pop();
            }

            if (!candidates.empty()) {
                pln[i] = candidates.top();
            }

            candidates.push(i);
        }

        while (!candidates.empty()) {
            candidates.pop();
        }

        // find next less number
        for (int i = arr.size() - 1; i >= 0; i--) {
            // it is important to add equal. it fix the same element bug
            while (!candidates.empty() && arr[candidates.top()] >= arr[i]) {
                candidates.pop();
            }

            if (!candidates.empty()) {
                nln[i] = candidates.top();
            }

            candidates.push(i);
        }

        int64_t sum = 0;
        for (int i = 0; i < arr.size(); i++) {
            int64_t tmp = (static_cast<int64_t>(i - pln[i]) * (nln[i] - i) * arr[i]) % 1000000007;
            sum = (sum + tmp) % 1000000007;
        }
        return sum;
    }
};


int main() {
    Solution s;
    vector<tuple<vector<int>, int>> test_cases {
        {{1,1,1,1}, 10},
        {{3,1,2,4}, 17},
        {{11,81,94,43,3}, 444},
    };

    for (auto& test_case: test_cases) {
        assert(s.sumSubarrayMins(get<0>(test_case)) == get<1>(test_case));
    }
}