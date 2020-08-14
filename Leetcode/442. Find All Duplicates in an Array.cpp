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


// Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

// Find all the elements that appear twice in this array.

// Could you do it without extra space and in O(n) runtime?

// Example:
// Input:
// [4,3,2,7,8,2,3,1]

// Output:
// [2,3]

class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        vector<int> res;
        if (nums.empty()) {
            return res;
        }

        int start = 0;
        while (start < nums.size()) {
            if (start == nums[start] - 1 || nums[start] == 0) {
                start++;
                continue;
            }

            if (nums[start] == nums[nums[start] - 1]) {
                res.push_back(nums[start]);
                nums[start] = 0;
                start++;
                continue;
            }
            swap(nums[start], nums[nums[start] - 1]);
        }
        return res;
    }
};

int main() {
    Solution s;
    vector<int> array {4,3,2,7,8,2,3,1};
    auto res = s.findDuplicates(array);
    for (auto e: res) {
        cout << e << ',';
    }
    cout << endl;
}