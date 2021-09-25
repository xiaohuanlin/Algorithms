#include <math.h>
#include <deque>
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
        // store the increasement array
        deque<int> candidates;
        vector<int> res;
        for (int i = 0; i < nums.size(); i++) {
            // remove useless element
            if (!candidates.empty() && i - k == candidates.front()) {
                candidates.pop_front();
            }

            while (!candidates.empty() && nums[candidates.back()] < nums[i]) {
                candidates.pop_back();
            }

            candidates.push_back(i);
            if (i >= k - 1) {
                res.push_back(nums[candidates.front()]);
            }
        }
        return res;
    }
};


int main() {
    Solution s;
    vector<tuple<tuple<vector<int>, int>, vector<int>>> test_cases {
        {{{1}, 1}, {1}},
        {{{1, -1}, 1}, {1, -1}},
        {{{9, 11}, 2}, {11}},
        {{{4, -2}, 2}, {4}},
        {{{1,3,-1,-3,5,3,6,7}, 3}, {3,3,5,5,6,7}},
        {{{-7,-8,7,5,7,1,6,0}, 4}, {7,7,7,7,7}},
    };

    for (auto& test_case: test_cases) {
        assert(s.maxSlidingWindow(get<0>(get<0>(test_case)), get<1>(get<0>(test_case))) == get<1>(test_case));
    }
}