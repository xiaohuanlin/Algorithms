#include <vector>
#include <iostream>
#include <tuple>
#include <assert.h>
using namespace std;

// Given an array nums of integers, we need to find the maximum possible sum of elements of the array such that it is divisible by three.

 

// Example 1:

// Input: nums = [3,6,5,1,8]
// Output: 18
// Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).
// Example 2:

// Input: nums = [4]
// Output: 0
// Explanation: Since 4 is not divisible by 3, do not pick any number.
// Example 3:

// Input: nums = [1,2,3,4,4]
// Output: 12
// Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).
 

// Constraints:

// 1 <= nums.length <= 4 * 10^4
// 1 <= nums[i] <= 10^4

class Solution {
public:
    int maxSumDivThree(vector<int>& nums) {
        int min_remain_one[2] = {INT32_MAX, INT32_MAX};
        int min_remain_two[2] = {INT32_MAX, INT32_MAX};
        int res = 0;
        for (auto& num : nums) {
            int remain = num % 3;
            if (remain == 1) {
                minRemain(min_remain_one, num);
            } else if (remain == 2) {
                minRemain(min_remain_two, num);
            }
            res += num;
        }

        int res_remain = res % 3;
        if (res_remain == 1) {
            int min_one = res, min_two = res;
            if (min_remain_one[0] != INT32_MAX) {
                min_one = min_remain_one[0];
            }
            if (min_remain_two[0] != INT32_MAX && min_remain_two[1] != INT32_MAX) {
                min_two = min_remain_two[0] + min_remain_two[1];
            }
            return max(res - min_one, res - min_two);
        } else if (res_remain == 2) {
            int min_one = res, min_two = res;
            if (min_remain_two[0] != INT32_MAX) {
                min_two = min_remain_two[0];
            }
            if (min_remain_one[0] != INT32_MAX && min_remain_one[1] != INT32_MAX) {
                min_one = min_remain_one[0] + min_remain_one[1];
            }
            return max(res - min_one, res - min_two);
        } else {
            return res;
        }
    }

    /**
     * Maintain the min value
     */
    void minRemain(int min_remain[], int value) {
        if (value < min_remain[0]) {
            min_remain[1] = min_remain[0];
            min_remain[0] = value;
        } else if (value < min_remain[1]) {
            min_remain[1] = value;
        }
    }
};

int main() {
    Solution s;
    vector<tuple<vector<int>, int>> test_cases {
        {{4}, 0},
        {{1, 2, 3, 4, 4}, 12},
        {{3, 6, 5, 1, 8}, 18},
    };

    for (auto& test_case: test_cases) {
        assert(s.maxSumDivThree(get<0>(test_case)) == get<1>(test_case));
    }
}