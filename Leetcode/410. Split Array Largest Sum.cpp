#include <vector>
#include <math.h>
#include <deque>
#include <tuple>
#include <unordered_map>
#include <assert.h>
using namespace std;

// Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.

// Write an algorithm to minimize the largest sum among these m subarrays.

 

// Example 1:

// Input: nums = [7,2,5,10,8], m = 2
// Output: 18
// Explanation:
// There are four ways to split nums into two subarrays.
// The best way is to split it into [7,2,5] and [10,8],
// where the largest sum among the two subarrays is only 18.
// Example 2:

// Input: nums = [1,2,3,4,5], m = 2
// Output: 9
// Example 3:

// Input: nums = [1,4,4], m = 3
// Output: 4
 

// Constraints:

// 1 <= nums.length <= 1000
// 0 <= nums[i] <= 10^6
// 1 <= m <= min(50, nums.length)


class Solution {
public:
    int splitArray(vector<int>& nums, int m) {
        int start = INT32_MAX;
        int end = 0;
        for (auto& num: nums) {
            start = min(start, num);
            end += num;
        }
        while (start < end) {
            int middle = (end - start) / 2 + start;
            if (is_right(nums, middle, m)) {
                end = middle;
            } else {
                start = middle + 1;
            }
        }
        return start;
    }

    bool is_right(vector<int>& nums, int max_sum, int m) {
        int sum = 0;
        int res = 1;
        for (auto& num: nums) {
            if (max_sum < num) {
                return false;
            }

            if (sum + num <= max_sum) {
                sum += num;
            } else {
                res++;
                sum = num;
            }
        }
        return res <= m;
    }
};


int main() {
    Solution s;
    vector<tuple<tuple<vector<int>, int>, int>> test_cases {
        {{{7,2,5,10,8}, 2}, 18},
        {{{1,2,3,4,5}, 2}, 9},
        {{{1,4,4}, 3}, 4},
    };

    for (auto& test_case: test_cases) {
        assert(s.splitArray(get<0>(get<0>(test_case)), get<1>(get<0>(test_case))) == get<1>(test_case));
    }
}