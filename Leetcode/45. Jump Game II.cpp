#include <vector>
#include <iostream>
#include <tuple>
#include <assert.h>
using namespace std;

// Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

// Each element in the array represents your maximum jump length at that position.

// Your goal is to reach the last index in the minimum number of jumps.

// You can assume that you can always reach the last index.


class Solution {
public:
    int jump(vector<int>& nums) {
        int size = nums.size();

        // the array whose length less than 1 means we needn't do anything
        if (size < 2) {
            return 0;
        }

        int res[size];
        res[size - 1] = 0;

        for (int i = size - 2; i >= 0; --i) {
            int span = nums[i];

            // figure out the min steps we can reach out
            int min_steps = INT32_MAX;
            for (int j = 1; i + j < size && j <= span; ++j) {
                min_steps = min(min_steps, res[i + j]);
            }
            res[i] = min_steps == INT32_MAX ? INT32_MAX : min_steps + 1;
        }
        return res[0];
    }
};


int main() {
    Solution s;
    vector<tuple<vector<int>, int>> test_cases {
        {{2, 3, 1, 1, 4}, 2},
        {{2, 3, 0, 1, 4}, 2},
        {{1}, 0},
        {{1, 1}, 1},
        {{3, 1}, 1},
    };

    for (auto& test_case: test_cases) {
        assert(s.jump(get<0>(test_case)) == get<1>(test_case));
    }
}