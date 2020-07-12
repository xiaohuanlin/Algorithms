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


// You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

// Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

// Example 1:

// Input: [2,3,2]
// Output: 3
// Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
//              because they are adjacent houses.
// Example 2:

// Input: [1,2,3,1]
// Output: 4
// Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
//              Total amount you can rob = 1 + 3 = 4.


class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() == 0) {
            return 0;
        } else if (nums.size() == 1) {
            return nums[0];
        } else if (nums.size() == 2) {
            return max(nums[1], nums[0]);
        }
        int left = rob_core(nums, 0, nums.size() - 1);
        int right = rob_core(nums, 1, nums.size());
        return max(left, right);
    }

    int rob_core(vector<int>& nums, int start, int end) {
        int low = nums[start];
        int high = max(nums[start], nums[start+1]);
        for (int i = 2; i < end - start; i++) {
            int tmp = max(high, low + nums[start + i]);
            low = high;
            high = tmp;
        }
        return high;
    }
};


int main() {
    Solution s;
    vector<int> array = {1,2,3,1};
    cout << s.rob(array);
}
