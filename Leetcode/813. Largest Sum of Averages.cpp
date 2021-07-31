#include <vector>
#include <iostream>
#include <tuple>
#include <assert.h>
using namespace std;

// You are given an integer array nums and an integer k. You can partition the array into at most k non-empty adjacent subarrays. The score of a partition is the sum of the averages of each subarray.

// Note that the partition must use every integer in nums, and that the score is not necessarily an integer.

// Return the maximum score you can achieve of all the possible partitions. Answers within 10-6 of the actual answer will be accepted.

 

// Example 1:

// Input: nums = [9,1,2,3,9], k = 3
// Output: 20.00000
// Explanation: 
// The best choice is to partition nums into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
// We could have also partitioned nums into [9, 1], [2], [3, 9], for example.
// That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.
// Example 2:

// Input: nums = [1,2,3,4,5,6,7], k = 4
// Output: 20.50000
 

// Constraints:

// 1 <= nums.length <= 100
// 1 <= nums[i] <= 10^4
// 1 <= k <= nums.length


class Solution {
public:
    double largestSumOfAverages(vector<int>& nums, int k) {
        vector<int> sums(nums.size(), 0);
        int sum = 0;
        for (int i = 0; i < nums.size(); ++i) {
            sum += nums[i];
            sums[i] = sum;
        }
        vector<vector<double>> dp(nums.size() + 1, vector<double>(k + 1, 0));
        for (int i = 1; i <= nums.size(); ++i) {
            for (int j = 1; j <= k; ++j) {
                if (j == 1) {
                    // only one part
                    dp[i][j] = double(sums[i - 1]) / i;
                } else if (j >= i) {
                    // one number one part
                    dp[i][j] = sums[i - 1];
                } else {
                    double max_v = 0;
                    for (int k = 1; i - k >= j - 1; ++k) {
                        max_v = max(max_v, dp[i - k][j - 1] + double(sums[i - 1] - sums[i - k - 1]) / k);
                    }
                    dp[i][j] = max_v;
                }
            }
        }
        return dp[nums.size()][k];
    }
};


int main() {
    Solution s;
    vector<tuple<tuple<vector<int>, int>, double>> test_cases {
        {{{9,1,2,3,9}, 3}, 20.0},
        {{{1,2,3,4,5,6,7}, 4}, 20.5},
    };

    for (auto& test_case: test_cases) {
        assert(s.largestSumOfAverages(get<0>(get<0>(test_case)), get<1>(get<0>(test_case))) == get<1>(test_case));
    }
}