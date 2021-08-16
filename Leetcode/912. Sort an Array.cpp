#include <vector>
#include <stack>
#include <unordered_map>
#include <algorithm>
#include <iostream>
#include <tuple>
#include <assert.h>
using namespace std;

// Given an array of integers nums, sort the array in ascending order.

 

// Example 1:

// Input: nums = [5,2,3,1]
// Output: [1,2,3,5]
// Example 2:

// Input: nums = [5,1,1,2,0,0]
// Output: [0,0,1,1,2,5]
 

// Constraints:

// 1 <= nums.length <= 5 * 10^4
// -5 * 10^4 <= nums[i] <= 5 * 10^4

class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        sortByDivide(nums, 0, nums.size());
        return nums;
    }

    void sortByDivide(vector<int>& nums, int start, int end) {
        if (start >= end) {
            return;
        }
        int target = start;
        int iter = start + 1;
        int less = end - 1;
        while (iter <= less) {
            if (nums[iter] < nums[target]) {
                swap(nums[iter], nums[target]);
                target = iter++;
            } else {
                swap(nums[iter], nums[less--]);
            }
        }
        sortByDivide(nums, start, target);
        sortByDivide(nums, target + 1, end);
    }
};

int main() {
    Solution s;
    vector<tuple<vector<int>, vector<int>>> test_cases {
        {{}, {}},
        {{5,2,3,1}, {1,2,3,5}},
        {{5,1,1,2,0,0}, {0,0,1,1,2,5}},
    };

    for (auto& test_case: test_cases) {
        assert(s.sortArray(get<0>(test_case)) == get<1>(test_case));
    }
}