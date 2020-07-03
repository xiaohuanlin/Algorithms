#include <stack>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;

// Given a set of distinct integers, nums, return all possible subsets (the power set).

// Note: The solution set must not contain duplicate subsets.

// Example:

// Input: nums = [1,2,3]
// Output:
// [
//   [3],
//   [1],
//   [2],
//   [1,2,3],
//   [1,3],
//   [2,3],
//   [1,2],
//   []
// ]

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> path;

        getSubsets(res, path, nums, 0, nums.size());
        return res;
    }

    void getSubsets(vector<vector<int>> &res, vector<int> &path, vector<int> &candidate, int count, int target) {
        if (count == target) {
            res.push_back(path);
            return;
        }

        count++;
        getSubsets(res, path, candidate, count, target);
        count--;

        path.push_back(candidate[count++]);
        getSubsets(res, path, candidate, count, target);
        path.pop_back();
        count--;
    }
};

int main() {
    Solution s;
    vector<int> array = {1,2,3};
    auto res = s.subsets(array);

    for (auto e: res) {
        for (auto l : e) {
            cout << l << ',';
        }
        cout << endl;
    }
    cout << endl;
}