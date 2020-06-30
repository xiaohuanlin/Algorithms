#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;

// Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

// Each number in candidates may only be used once in the combination.

// Note:

// All numbers (including target) will be positive integers.
// The solution set must not contain duplicate combinations.
// Example 1:

// Input: candidates = [10,1,2,7,6,1,5], target = 8,
// A solution set is:
// [
//   [1, 7],
//   [1, 2, 5],
//   [2, 6],
//   [1, 1, 6]
// ]
// Example 2:

// Input: candidates = [2,5,2,1,2], target = 5,
// A solution set is:
// [
//   [1,2,2],
//   [5]
// ]

class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<set<vector<int>>> dp(target + 1, 
            set<vector<int>>()
        );

        dp[0] = set<vector<int>>();
        dp[0].insert(vector<int>());

        // we can't solve solutions before and get result, and it is most important that
        // iter candidate first and iter sum from target to 0 to make sure we can not use
        // same number twice.
        for (int i = 0; i < candidates.size(); i ++) {
            int count = target;
            while (count >= 1) {
                int before_number = count - candidates[i];
                if (before_number < 0) {
                    count --;
                    continue;
                }
                
                for (auto j = dp[before_number].begin(); j != dp[before_number].end(); j++) {
                    vector<int> item(*j);
                    item.push_back(candidates[i]);
                    dp[count].insert(item);
                }
                count --;
            }
        }
        vector<vector<int>> res(dp[target].begin(), dp[target].end());
        return res;
    }
};


int main() {
    Solution s;
    vector<int> array = {};
    auto res = s.combinationSum2(array, 5);
    for (auto e: res) {
        for (auto l:e) {
            cout << l << ',';
        }
        cout << endl;
    }
}