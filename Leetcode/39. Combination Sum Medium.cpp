#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;

// Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

// The same repeated number may be chosen from candidates unlimited number of times.

// Note:

// All numbers (including target) will be positive integers.
// The solution set must not contain duplicate combinations.
// Example 1:

// Input: candidates = [2,3,6,7], target = 7,
// A solution set is:
// [
//   [7],
//   [2,2,3]
// ]
// Example 2:

// Input: candidates = [2,3,5], target = 8,
// A solution set is:
// [
//   [2,2,2,2],
//   [2,3,3],
//   [3,5]
// ]

class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<vector<int>>> dp(target + 1, 
            vector<vector<int>>()
        );

        dp[0] = vector<vector<int>>(1, 
            vector<int>()
        );

        int count = 1;
        while (count <= target) {
            set<vector<int>> new_item;
            for (int i = 0; i < candidates.size(); i ++) {
                int before_number = count - candidates[i];
                if (before_number < 0) {
                    continue;
                }
                
                for (int k = 0; k < dp[before_number].size(); k++) {
                    vector<int> item(dp[before_number][k]);
                    item.push_back(candidates[i]);
                    sort(item.begin(), item.end());
                    new_item.insert(item);
                }
            }
            dp[count] = vector<vector<int>>(new_item.begin(), new_item.end());
            count ++;
        }
        return dp[target];
    }
};


int main() {
    Solution s;
    vector<int> array = {2, 3, 5};
    auto res = s.combinationSum(array, 8);
    for (auto e: res) {
        for (auto l:e) {
            cout << l << ',';
        }
        cout << endl;
    }
}