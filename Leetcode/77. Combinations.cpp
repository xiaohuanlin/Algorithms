#include <stack>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;

// Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

// Example:

// Input: n = 4, k = 2
// Output:
// [
//   [2,4],
//   [3,4],
//   [2,3],
//   [1,2],
//   [1,3],
//   [1,4],
// ]

class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> res;
        vector<int> path;
        vector<int> candidates;

        getCombine(path, res, 1, n, k);
        return res;
    }

    void getCombine(vector<int> &path, vector<vector<int>> &res, int start, int n, int k) {
        if (path.size() == k) {
            res.push_back(path);
            return;
        }

        for (int iter = start; iter <= n; iter++) {
            path.push_back(iter);
            getCombine(path, res, iter+1, n, k);
            path.pop_back();
        }
    }
};

int main() {
    Solution s;
    auto res = s.combine(3, 2);

    for (auto e: res) {
        for (auto l : e) {
            cout << l << ',';
        }
        cout << endl;
    }
    cout << endl;
}