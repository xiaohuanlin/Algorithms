#include <vector>
#include <stack>
#include <deque>
#include <algorithm>
#include <iostream>
#include <tuple>
#include <assert.h>
using namespace std;


// A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. The width of such a ramp is j - i.

// Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.

 

// Example 1:

// Input: nums = [6,0,8,2,1,5]
// Output: 4
// Explanation: The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] = 0 and nums[5] = 5.
// Example 2:

// Input: nums = [9,8,1,0,1,9,4,0,4,1]
// Output: 7
// Explanation: The maximum width ramp is achieved at (i, j) = (2, 9): nums[2] = 1 and nums[9] = 1.
 

// Constraints:

// 2 <= nums.length <= 5 * 10^4
// 0 <= nums[i] <= 5 * 10^4

class Solution {
public:
    int maxWidthRamp(vector<int>& nums) {
        // use ut to reduce the searching time
        vector<int> right_max(nums.size(), 0);
        right_max[nums.size() - 1] = nums[nums.size() - 1];
        for (int i = nums.size() - 2; i >= 0; i--) {
            right_max[i] = max(right_max[i+1], nums[i]);
        }

        int left = 0, right = 0;
        int result = 0;
        while (right < nums.size()) {
            while (left < right && nums[left] > right_max[right]) {
                left++;
            }
            result = max(result, right - left);
            right++;
        }
        return result;
    }
};

int main() {
    Solution s;
    vector<tuple<vector<int>, int>> test_cases {
        {{2,1}, 0},
        {{6,0,8,2,1,5}, 4},
        {{9,8,1,0,1,9,4,0,4,1}, 7}
    };

    for (auto& test_case: test_cases) {
        assert(s.maxWidthRamp(get<0>(test_case)) == get<1>(test_case));
    }
}