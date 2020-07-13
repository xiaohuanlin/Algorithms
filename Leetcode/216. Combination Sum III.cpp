#include <unordered_set>
#include <unordered_map>
#include <math.h>
#include <utility>
#include <stack>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;


// Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

// Note:

// All numbers will be positive integers.
// The solution set must not contain duplicate combinations.
// Example 1:

// Input: k = 3, n = 7
// Output: [[1,2,4]]
// Example 2:

// Input: k = 3, n = 9
// Output: [[1,2,6], [1,3,5], [2,3,4]]


class Solution {
public:
    vector<vector<int>> combinationSum3(int k, int n) {
        vector<vector<int>> res;
        vector<int> path;
        core_combi(res, path, 1, n, k);
        return res;
    }

    void core_combi(vector<vector<int>> &res, vector<int> &path, int start, int target, int limit) {
        if (target == 0 && limit == 0) {
            res.push_back(path);
            return;
        }

        if (target < 0 || start > 9 || limit < 0) {
            return;
        }

        for (int i = start; i <= 9; i++) {
            path.push_back(i);
            core_combi(res, path, i+1, target-i, limit-1);
            path.pop_back();
        }
        return;
    }
};

int main() {
    Solution s;
    auto res = s.combinationSum3(3, 7);

    for (auto e: res) {
        for (auto l: e) {
            cout << l << ',';
        }
        cout << endl;
    }
}
