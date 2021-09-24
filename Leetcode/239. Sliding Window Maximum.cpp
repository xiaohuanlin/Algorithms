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
#include <assert.h>
using namespace std;


// You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

// Return the max sliding window.

 

// Example 1:

// Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
// Output: [3,3,5,5,6,7]
// Explanation: 
// Window position                Max
// ---------------               -----
// [1  3  -1] -3  5  3  6  7       3
//  1 [3  -1  -3] 5  3  6  7       3
//  1  3 [-1  -3  5] 3  6  7       5
//  1  3  -1 [-3  5  3] 6  7       5
//  1  3  -1  -3 [5  3  6] 7       6
//  1  3  -1  -3  5 [3  6  7]      7
// Example 2:

// Input: nums = [1], k = 1
// Output: [1]
// Example 3:

// Input: nums = [1,-1], k = 1
// Output: [1,-1]
// Example 4:

// Input: nums = [9,11], k = 2
// Output: [11]
// Example 5:

// Input: nums = [4,-2], k = 2
// Output: [4]
 

// Constraints:

// 1 <= nums.length <= 10^5
// -10^4 <= nums[i] <= 10^4
// 1 <= k <= nums.length


class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> next_max(nums.size(), 0);
        vector<int> prev_max(nums.size(), 0);
        stack<int> candidates_min, candidates_max;

        for (int i = nums.size() - 1; i >= 0; i--) {
            int j = nums.size() - 1 - i;
            while (!candidates_min.empty() && nums[candidates_min.top()] <= nums[i]) {
                candidates_min.pop();
            }
            while (!candidates_max.empty() && nums[candidates_max.top()] <= nums[j]) {
                candidates_max.pop();
            }

            next_max[i] = candidates_min.empty() ? nums.size(): candidates_min.top();
            prev_max[j] = candidates_max.empty() ? -1: candidates_max.top();
            candidates_min.push(i);
            candidates_max.push(j);
        }

        vector<int> res(nums.size() - k + 1, 0);
        for (int i = 0; i < nums.size(); i++) {
            int prev_index = prev_max[i];
            int next_index = next_max[i];
            // limit k step for prev and next index
            for (int j = max(prev_index + 1, i - k + 1); j + k <= next_index; j++) {
                res[j] = nums[i];
            }
        }

        return res;
    }
};


int main() {
    Solution s;
    vector<tuple<tuple<vector<int>, int>, vector<int>>> test_cases {
        // {{{1}, 1}, {1}},
        // {{{1, -1}, 1}, {1, -1}},
        // {{{9, 11}, 2}, {11}},
        // {{{4, -2}, 2}, {4}},
        // {{{1,3,-1,-3,5,3,6,7}, 3}, {3,3,5,5,6,7}},
        {{{-7,-8,7,5,7,1,6,0}, 4}, {7,7,7,7,7}},
    };

    for (auto& test_case: test_cases) {
        assert(s.maxSlidingWindow(get<0>(get<0>(test_case)), get<1>(get<0>(test_case))) == get<1>(test_case));
    }
}