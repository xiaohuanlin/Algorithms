#include <vector>
#include <iostream>
#include <tuple>
#include <assert.h>
using namespace std;

// Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

// Follow-up: Could you solve the problem in linear time and in O(1) space?

 

// Example 1:

// Input: nums = [3,2,3]
// Output: [3]
// Example 2:

// Input: nums = [1]
// Output: [1]
// Example 3:

// Input: nums = [1,2]
// Output: [1,2]
 

// Constraints:

// 1 <= nums.length <= 5 * 10^4
// -10^9 <= nums[i] <= 10^9


class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        // I have to know about what is Boyer-Moore Majority Vote algorithm
        if (nums.empty()) {
            return {};
        }

        int count1 = 0, count2 = 0, major1 = INT32_MAX, major2 = INT32_MAX;
        for (auto& num : nums) {
            if (count1 == 0 && major2 != num) {
                major1 = num;
                count1++;
            } else if (count2 == 0 && major1 != num) {
                major2 = num;
                count2++;
            } else if (major1 == num) {
                count1++;
            } else if (major2 == num) {
                count2++;
            } else {
                count1--;
                count2--;
            }
        }

        count1 = 0;
        count2 = 0;
        for (auto& num : nums) {
            if (num == major1) {
                count1++;
            } else if (num == major2) {
                count2++;
            }
        }
        vector<int> res;
        if (count1 > nums.size() / 3) {
            res.push_back(major1);
        }
        if (count2 > nums.size() / 3) {
            res.push_back(major2);
        }
        return res;
    }
};


int main() {
    Solution s;
    vector<tuple<vector<int>, vector<int>>> test_cases {
        {{}, {}},
        {{3, 2, 3}, {3}},
        {{1}, {1}},
        {{1, 2}, {1, 2}},
        {{1, 1, 1, 2, 3, 7, 8, 1, 6, 9}, {1}},
        {{2, 1, 1, 3, 1, 4, 5, 6}, {1}},
    };

    for (auto& test_case: test_cases) {
        assert(s.majorityElement(get<0>(test_case)) == get<1>(test_case));
    }
}