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


// Given an unsorted array of integers, find the length of longest increasing subsequence.

// Example:

// Input: [10,9,2,5,3,7,101,18]
// Output: 4 
// Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
// Note:

// There may be more than one LIS combination, it is only necessary for you to return the length.
// Your algorithm should run in O(n2) complexity.
// Follow up: Could you improve it to O(n log n) time complexity?


class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int size = nums.size();
        if (size == 0){
            return 0;
        }
        vector<int> dp(size, 1);

        for (int i = 0; i < size; i++) {
            for (int k = i - 1; k >= 0; k--) {
                if (nums[k] < nums[i]) {
                    dp[i] = max(dp[i],dp[k] + 1);
                }
            }
        }
    
        int max_value = 0;
        for (int j = 0; j < size; j++) {
            if (dp[j] > max_value) {
                max_value = dp[j];
            }
        }
        return max_value;
    }
};


int main() {
    Solution s;
    vector<int> array = {1,3,6,7,9,4,10,5,6};
    cout << s.lengthOfLIS(array);
}
