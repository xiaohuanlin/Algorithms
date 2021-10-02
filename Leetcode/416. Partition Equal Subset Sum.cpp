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


// Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

// Note:

// Each of the array element will not exceed 100.
// The array size will not exceed 200.
 

// Example 1:

// Input: [1, 5, 11, 5]

// Output: true

// Explanation: The array can be partitioned as [1, 5, 5] and [11].
 

// Example 2:

// Input: [1, 2, 3, 5]

// Output: false

// Explanation: The array cannot be partitioned into equal sum subsets.


class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sum = 0;
        for (auto &ele: nums) {
            sum += ele;
        }
        if (sum % 2 != 0) {
            return false;
        }

        int target = sum / 2;
        vector<vector<bool>> dp(nums.size() + 1, vector<bool>(target + 1, false));

        for (int i = 0; i < dp.size(); i++) {
            dp[i][0] = true;
        }

        // i means previous number
        // j means target value
        for (int i = 1; i < dp.size(); i++) {
            for (int j = 1; j < dp[0].size(); j++) {
                dp[i][j] = (j >= nums[i - 1] ? dp[i - 1][j - nums[i - 1]]: false) ||
                            (dp[i - 1][j]);
            }
        }
        return dp[dp.size() - 1][target];
    }
};

int main() {
    Solution s;
    vector<int> array = {1,5,11,5};
    cout << s.canPartition(array);
}
