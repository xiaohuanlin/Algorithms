#include <math.h>
#include <utility>
#include <stack>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;

// Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

// Note: The solution set must not contain duplicate subsets.

// Example:

// Input: [1,2,2]
// Output:
// [
//   [2],
//   [1],
//   [1,2,2],
//   [2,2],
//   [1,2],
//   []
// ]

class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> path;
        if (nums.empty()) {
            return res;
        }
        sort(nums.begin(), nums.end());
        backtrace(res, path, nums, 0, nums[0], true);
        return res;
    }
    
    void backtrace(vector<vector<int>> &res, vector<int> &path, vector<int> &nums, int current,
                    int previous, bool exist) {
        if (current == nums.size()) {
            res.push_back(path);
            return;
        }

        // use this element
        if (!(previous == nums[current] && !exist)) {
            path.push_back(nums[current]);
            backtrace(res, path, nums, current+1, nums[current], true);
            path.pop_back();
        }

        backtrace(res, path, nums, current+1, nums[current], false);
    }
};

int main() {
    Solution s;
    vector<int> array = {3, 2, 2};
    auto res = s.subsetsWithDup(array);
    for (auto e: res) {
        for (auto l: e) {
            cout << l << ',';
        }
        cout << endl;
    }
}