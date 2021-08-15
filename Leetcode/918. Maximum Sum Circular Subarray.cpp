#include <vector>
#include <stack>
#include <algorithm>
#include <iostream>
#include <tuple>
#include <assert.h>
using namespace std;


// Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

// A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

// A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

 

// Example 1:

// Input: nums = [1,-2,3,-2]
// Output: 3
// Explanation: Subarray [3] has maximum sum 3
// Example 2:

// Input: nums = [5,-3,5]
// Output: 10
// Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10
// Example 3:

// Input: nums = [3,-1,2,-1]
// Output: 4
// Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4
// Example 4:

// Input: nums = [3,-2,2,-3]
// Output: 3
// Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3
// Example 5:

// Input: nums = [-2,-3,-1]
// Output: -1
// Explanation: Subarray [-1] has maximum sum -1
 

// Constraints:

// n == nums.length
// 1 <= n <= 3 * 10^4
// -3 * 104 <= nums[i] <= 3 * 10^4

class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        // we only need to find the max value and the min value for remain array
        int dp_max = 0;
        int dp_min = 0;

        // find maximum sum subarray
        int max_sum_v = INT32_MIN;
        // find minimum sum subarray
        int min_sum_v = INT32_MAX;
        int sum = 0;
        for (int i = 0; i < nums.size(); ++i) {
            dp_max = max(dp_max + nums[i], nums[i]);
            max_sum_v = max(dp_max, max_sum_v);
            dp_min = min(dp_min + nums[i], nums[i]);
            min_sum_v = min(dp_min, min_sum_v);
            sum += nums[i];
        }

        // for the case of no element be select when minimum sum equal min_sum_v
        if (sum == min_sum_v) {
            return max_sum_v;
        }
        return max(max_sum_v, sum - min_sum_v);
    }
};

int main() {
    Solution s;
    vector<tuple<vector<int>, int>> test_cases {
        {{1, -2, 3, -2}, 3},
        {{5, -3, 5}, 10},
        {{3, -1, 2, -1}, 4},
        {{3, -2, 2, -3}, 3},
        {{-2, -3, -1}, -1},
    };

    for (auto& test_case: test_cases) {
        assert(s.maxSubarraySumCircular(get<0>(test_case)) == get<1>(test_case));
    }
}