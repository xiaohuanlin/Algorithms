#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;

// Given a collection of numbers that might contain duplicates, return all possible unique permutations.

// Example:

// Input: [1,1,2]
// Output:
// [
//   [1,1,2],
//   [1,2,1],
//   [2,1,1]
// ]

class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        sort(nums.begin(), nums.end());
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
            if (k > start && nums[k] == nums[k-1]) {
                continue;
            }

            int tmp = nums[k];
            for (int j = k; j > start; j--) {
                nums[j] = nums[j-1];
            }
            nums[start] = tmp;
            core_permute(res, nums, start + 1);

            for (int j = start; j < k; j++) {
                nums[j] = nums[j+1];
            }
            nums[k] = tmp;
        }
    }
};

int main() {
    Solution s;
    vector<int> array = {0, 1, 0, 0, 9};
    auto res = s.permuteUnique(array);
    for (auto e: res) {
        for (auto l: e) {
            cout << l << ',';
        }
        cout << endl;
    }
}
