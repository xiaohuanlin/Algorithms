#include <vector>
#include <stack>
#include <iostream>
#include <tuple>
#include <assert.h>
#include <algorithm>
using namespace std;


// You are given an integer array nums of length n which represents a permutation of all the integers in the range [0, n - 1].

// The number of global inversions is the number of the different pairs (i, j) where:

// 0 <= i < j < n
// nums[i] > nums[j]
// The number of local inversions is the number of indices i where:

// 0 <= i < n - 1
// nums[i] > nums[i + 1]
// Return true if the number of global inversions is equal to the number of local inversions.
// Example 1:

// Input: nums = [1,0,2]
// Output: true
// Explanation: There is 1 global inversion and 1 local inversion.
// Example 2:

// Input: nums = [1,2,0]
// Output: false
// Explanation: There are 2 global inversions and 1 local inversion.
 

// Constraints:

// n == nums.length
// 1 <= n <= 10^5
// 0 <= nums[i] < n
// All the integers of nums are unique.
// nums is a permutation of all the numbers in the range [0, n - 1].


class Solution {
public:
    bool isIdealPermutation(vector<int>& nums) {
        // we only need to find if there is any i, which makes nums[i] larger than all numbers after i+2
        // so we iter the number from end to begin, try to minimize the total run time
        int min_v = INT32_MAX;
        for (int i = nums.size() - 1; i > 1; --i) {
            min_v = min(min_v, nums[i]);
            if (nums[i - 2] > min_v) {
                return false;
            }
        }
        return true;
    }
};


int main() {
    Solution s;
    vector<tuple<vector<int>, bool>> test_cases {
        {{0}, true},
        {{1,0,2}, true},
        {{1,2,0}, false},
    };

    for (auto& test_case: test_cases) {
        assert(s.isIdealPermutation(get<0>(test_case)) == get<1>(test_case));
    }
}