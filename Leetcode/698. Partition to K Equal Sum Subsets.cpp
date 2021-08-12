#include <vector>
#include <stack>
#include <algorithm>
#include <iostream>
#include <tuple>
#include <assert.h>
using namespace std;


// Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

 

// Example 1:

// Input: nums = [4,3,2,3,5,2,1], k = 4
// Output: true
// Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
// Example 2:

// Input: nums = [1,2,3,4], k = 3
// Output: false
 

// Constraints:

// 1 <= k <= nums.length <= 16
// 1 <= nums[i] <= 10^4
// The frequency of each element is in the range [1, 4].


class Solution {
public:
    bool canPartitionKSubsets(vector<int>& nums, int k) {
        int sum = 0;
        for (auto& num : nums) {
            sum += num;
        }

        if (sum % k) {
            return false;
        }
        vector<bool> visited(nums.size(), false);
        
        return traceback(nums, 0, visited, 0, sum / k, k);
    }

    bool traceback(vector<int>& nums, int start, vector<bool>& visited, int sum, int sum_target, int group_target) {
        if (sum > sum_target) {
            return false;
        }

        // find all groups
        if (group_target == 0) {
            return true;
        }

        if (sum == sum_target) {
            // finish searching one group
            return traceback(nums, 0, visited, 0, sum_target, group_target - 1);
        }

        for (int i = start; i < nums.size(); i++) {
            if (!visited[i]) {
                visited[i] = true;
                if (traceback(nums, i + 1, visited, sum + nums[i], sum_target, group_target)) {
                    return true;
                }
                // restore
                visited[i] = false;
            }
        }
        return false;
    }
};

int main() {
    Solution s;
    vector<tuple<tuple<vector<int>, int>, bool>> test_cases {
        {{{4,3,2,3,5,2,1}, 4}, true},
        {{{1,2,3,4}, 3}, false},
    };

    for (auto& test_case: test_cases) {
        assert(s.canPartitionKSubsets(get<0>(get<0>(test_case)),get<1>(get<0>(test_case))) == get<1>(test_case));
    }
}