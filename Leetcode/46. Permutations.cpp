#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;

// Given a collection of distinct integers, return all possible permutations.

// Example:

// Input: [1,2,3]
// Output:
// [
//   [1,2,3],
//   [1,3,2],
//   [2,1,3],
//   [2,3,1],
//   [3,1,2],
//   [3,2,1]
// ]

class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        core_permute(res, nums, 0);
        return res;
    }

    void core_permute(vector<vector<int>> &res, vector<int> &nums, int start) {
        if (start + 1 >= nums.size()) {
            res.push_back(vector<int>(nums));
            return;
        }

        for (int k = start; k < nums.size(); k++) {
            swap(nums[start], nums[k]);
            core_permute(res, nums, start + 1);
            swap(nums[start], nums[k]);
        }
    }
};

int main() {
    Solution s;
    vector<int> array = {1,2,3};
    auto res = s.permute(array);
    for (auto e: res) {
        for (auto l: e) {
            cout << l << ',';
        }
        cout << endl;
    }
}
