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


// Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

// Si % Sj = 0 or Sj % Si = 0.

// If there are multiple solutions, return any subset is fine.

// Example 1:

// Input: [1,2,3]
// Output: [1,2] (of course, [1,3] will also be ok)
// Example 2:

// Input: [1,2,4,8]
// Output: [1,2,4,8]


class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        vector<vector<int>> dps(nums.size(), vector<int>());
    }

};


int main() {
    Solution s;
    vector<int> array = {1,2,3,4,5,6,7,8,9};
    auto res = s.largestDivisibleSubset(array);
    for (auto e: res) {
        cout << e << ',';
    }
    cout << endl;
    // todo
}