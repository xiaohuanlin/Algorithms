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
        vector<int> path;
        set<int> exclude;
        core_permute(res, path, nums, exclude);
        return res;
    }

    void core_permute(vector<vector<int>> &res, vector<int> &path, vector<int> &nums, set<int> &exclude) {
        if (path.size() == nums.size()) {
            res.push_back(vector<int>(path));
            return;
        }

        for (int k = 0; k < nums.size(); k++) {
            if (exclude.find(nums[k]) != exclude.end()) {
                continue;
            }
            path.push_back(nums[k]);
            exclude.insert(nums[k]);
            core_permute(res, path, nums, exclude);
            path.pop_back();
            exclude.erase(exclude.find(nums[k]));
        }
    }
};

int main() {
    Solution s;
    vector<int> array = {};
    auto res = s.permute(array);
    for (auto e: res) {
        for (auto l: e) {
            cout << l << ',';
        }
        cout << endl;
    }
}
