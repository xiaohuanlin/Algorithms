#include <vector>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <iostream>
#include <tuple>
#include <assert.h>
using namespace std;

// A split of an integer array is good if:

// The array is split into three non-empty contiguous subarrays - named left, mid, right respectively from left to right.
// The sum of the elements in left is less than or equal to the sum of the elements in mid, and the sum of the elements in mid is less than or equal to the sum of the elements in right.
// Given nums, an array of non-negative integers, return the number of good ways to split nums. As the number may be too large, return it modulo 109 + 7.

 

// Example 1:

// Input: nums = [1,1,1]
// Output: 1
// Explanation: The only good way to split nums is [1] [1] [1].
// Example 2:

// Input: nums = [1,2,2,2,5,0]
// Output: 3
// Explanation: There are three good ways of splitting nums:
// [1] [2] [2,2,5,0]
// [1] [2,2] [2,5,0]
// [1,2] [2,2] [5,0]
// Example 3:

// Input: nums = [3,2,1]
// Output: 0
// Explanation: There is no good way to split nums.
 

// Constraints:

// 3 <= nums.length <= 105
// 0 <= nums[i] <= 104


class Solution {
public:
    int waysToSplit(vector<int>& nums) {
        vector<int> cache_sum(nums.size(), nums[0]);
        for (int i = 1; i < nums.size(); i++) {
            cache_sum[i] = cache_sum[i - 1] + nums[i];
        }

        int count = 0;

        for (int first = 0; first < nums.size(); first++) {
            auto second_lower_pos = lower_bound(cache_sum.begin(), cache_sum.end(), cache_sum[first] * 2);
            auto second_upper_pos = upper_bound(cache_sum.begin(), cache_sum.end(), (cache_sum[cache_sum.size() - 1] + cache_sum[first]) / 2);

            int distance_second_lower = distance(cache_sum.begin(), second_lower_pos);
            int distance_second_upper = distance(cache_sum.begin(), second_upper_pos);
            count += max((min(distance_second_upper, int(cache_sum.size() - 1)) - max(first + 1, distance_second_lower)), 0);
            count %= static_cast<int>(1e9 + 7);
        }
        return count;
    }
};

int main() {
    Solution s;
    vector<tuple<vector<int>, int>> test_cases {
        {{0,0,0,0}, 3},
        {{0,3,3}, 1},
        {{1,1,1}, 1},
        {{1,2,2,2,5,0}, 3},
        {{3,2,1}, 0},
    };

    for (auto& test_case: test_cases) {
        assert(s.waysToSplit(get<0>(test_case)) == get<1>(test_case));
    }
}