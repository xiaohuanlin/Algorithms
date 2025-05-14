#include <vector>
#include <stack>
#include <unordered_map>
#include <algorithm>
#include <iostream>
#include <tuple>
#include <assert.h>
using namespace std;


// You are given a binary array nums.

// A subarray of an array is good if it contains exactly one element with the value 1.

// Return an integer denoting the number of ways to split the array nums into good subarrays. As the number may be too large, return it modulo 109 + 7.

// A subarray is a contiguous non-empty sequence of elements within an array.

 

// Example 1:

// Input: nums = [0,1,0,0,1]
// Output: 3
// Explanation: There are 3 ways to split nums into good subarrays:
// - [0,1] [0,0,1]
// - [0,1,0] [0,1]
// - [0,1,0,0] [1]
// Example 2:

// Input: nums = [0,1,0]
// Output: 1
// Explanation: There is 1 way to split nums into good subarrays:
// - [0,1,0]
 

// Constraints:

// 1 <= nums.length <= 105
// 0 <= nums[i] <= 1


class Solution {
    public:
        int numberOfGoodSubarraySplits(vector<int>& nums) {
            long prev = 0;
            int cnt = 0;
            for (auto i = 1; i < nums.size() + 1; i++) {
                if (nums[i-1] == 0) {
                    cnt++;
                } else {
                    if (prev == 0) {
                        prev = 1;
                    } else {
                        prev = ((cnt + 1) * (prev % long(1e9 + 7))) % long(1e9 + 7);
                    }
                    cnt = 0;
                }
            }
            return prev;
        }
    };


int main() {
    Solution s;
    vector<tuple<vector<int>, int>> test_cases {
        {{0,1,0,0,1}, 3},
        {{0,1,0}, 1}
    };

    for (auto& test_case: test_cases) {
        assert(s.numberOfGoodSubarraySplits(get<0>(test_case)) == get<1>(test_case));
    }
}