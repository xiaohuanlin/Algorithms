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


// Given an integer array, your task is to find all the different possible increasing subsequences of the given array, and the length of an increasing subsequence should be at least 2.

 

// Example:

// Input: [4, 6, 7, 7]
// Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
 

// Constraints:

// The length of the given array will not exceed 15.
// The range of integer in the given array is [-100,100].
// The given array may contain duplicates, and two equal integers should also be considered as a special case of increasing sequence.


class Solution {
public:
    vector<vector<int>> findSubsequences(vector<int>& nums) {
        set<vector<int>> res;        
        for (int i = 0; i < nums.size(); ++i) {
            vector<vector<int>> tmp_res;
            for (auto iter = res.begin(); iter != res.end(); ++iter) {
                if (iter->back() <= nums[i]) {
                    vector<int> tmp(*iter);
                    tmp.push_back(nums[i]);
                    tmp_res.push_back(tmp);
                }
            }
            res.insert(tmp_res.begin(), tmp_res.end());
            res.insert(vector<int>(1, nums[i]));
        }

        vector<vector<int>> ans;
        for (auto iter = res.begin(); iter != res.end(); ++iter) {
            if (iter->size() > 1) {
                ans.push_back(*iter);
            }
        }
        return ans;
    }
};


int main() {
    Solution s;
    vector<int> array {4,6,7,7};
    auto res = s.findSubsequences(array);
    for (auto e: res) {
        for (auto l: e) {
            cout << l << ',';
        }
        cout << endl;
    }
}