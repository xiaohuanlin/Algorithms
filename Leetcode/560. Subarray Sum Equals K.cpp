#include <vector>
#include <unordered_map>
#include <iostream>
#include <tuple>
#include <assert.h>
using namespace std;

// Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

 

// Example 1:

// Input: nums = [1,1,1], k = 2
// Output: 2
// Example 2:

// Input: nums = [1,2,3], k = 3
// Output: 2
 

// Constraints:

// 1 <= nums.length <= 2 * 104
// -1000 <= nums[i] <= 1000
// -107 <= k <= 107

class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        vector<int> sums(nums.size(), 0);
        for (int i = 0; i < nums.size(); ++i) {
            if (i == 0) {
                sums[i] = nums[i];
            } else {
                sums[i] = sums[i - 1] + nums[i];
            }
        }

        unordered_map<int, int> sums_set;
        int res = 0;
        for (int i = sums.size() - 1; i >= 0; --i) {
            int find_v = sums[i] + k;
            if (sums_set.find(find_v) != sums_set.end()) {
                res += sums_set[find_v];
            }

            if (sums[i] == k) {
                res += 1;
            }

            sums_set[sums[i]] += 1;
        }
        return res;
    }
};

int main() {
    Solution s;
    vector<tuple<tuple<vector<int>, int>, int>> test_cases {
        {{{1, 1, 1}, 2}, 2},
        {{{1, 2, 3}, 3}, 2},
    };

    for (auto& test_case: test_cases) {
        assert(s.subarraySum(get<0>(get<0>(test_case)), get<1>(get<0>(test_case))) == get<1>(test_case));
    }
}