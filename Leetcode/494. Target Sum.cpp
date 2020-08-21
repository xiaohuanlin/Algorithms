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


// You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

// Find out how many ways to assign symbols to make sum of integers equal to target S.

// Example 1:

// Input: nums is [1, 1, 1, 1, 1], S is 3. 
// Output: 5
// Explanation: 

// -1+1+1+1+1 = 3
// +1-1+1+1+1 = 3
// +1+1-1+1+1 = 3
// +1+1+1-1+1 = 3
// +1+1+1+1-1 = 3

// There are 5 ways to assign symbols to make the sum of nums be target 3.
 

// Constraints:

// The length of the given array is positive and will not exceed 20.
// The sum of elements in the given array will not exceed 1000.
// Your output answer is guaranteed to be fitted in a 32-bit integer.


class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int S) {
        if (nums.empty()) {
            return 0;
        }
        
        int num = 3;
        int delta = num / 2;
        if (INT32_MAX - delta < S || S + delta >= num) {
            return 0;
        }

        vector<vector<int>> dp(num, vector<int>(nums.size(), 0));
        dp[nums[0] + delta][0] ++;
        dp[-nums[0] + delta][0] ++;

        for (int i = 1; i < nums.size(); ++i) {
            for (int j = 0; j < num; ++j) {
                if (j + nums[i] < num) {
                    dp[j][i] += dp[j+nums[i]][i-1];
                }
                if (j - nums[i] >= 0) {
                    dp[j][i] += dp[j-nums[i]][i-1];
                }
            }
        }
        return dp[S + delta][nums.size()-1];
    }
};

int main() {
    Solution s;
    vector<int> array {0,0,0,0,0,0,0,0,1};
    cout << s.findTargetSumWays(array, 1);

}
