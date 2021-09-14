#include <vector>
#include <stack>
#include <unordered_map>
#include <algorithm>
#include <iostream>
#include <tuple>
#include <assert.h>
using namespace std;

// You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.

// Return the minimum number of moves to make every value in nums unique.

 

// Example 1:

// Input: nums = [1,2,2]
// Output: 1
// Explanation: After 1 move, the array could be [1, 2, 3].
// Example 2:

// Input: nums = [3,2,1,2,1,7]
// Output: 6
// Explanation: After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
// It can be shown with 5 or less moves that it is impossible for the array to have all unique values.
 

// Constraints:

// 1 <= nums.length <= 10^^5
// 0 <= nums[i] <= 10^5


class Solution {
public:
    int minIncrementForUnique(vector<int>& nums) {
        sort(nums.begin(), nums.end());

        int start = -1;
        int count = 0;
        
        for (auto& num: nums) {
            if (start < num) {
                start = num;
            } else {
                start++;
                count += (start - num);
            }
        }
        return count;
    }
};


int main() {
    Solution s;
    vector<tuple<vector<int>, int>> test_cases {
        {{1,2,2}, 1},
        {{3,2,1,2,1,7}, 6},
    };

    for (auto& test_case: test_cases) {
        assert(s.minIncrementForUnique(get<0>(test_case)) == get<1>(test_case));
    }
}