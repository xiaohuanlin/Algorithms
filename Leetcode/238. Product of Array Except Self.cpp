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


// Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

// Example:

// Input:  [1,2,3,4]
// Output: [24,12,8,6]
// Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

// Note: Please solve it without division and in O(n).

// Follow up:
// Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)


class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> result(nums.size(), 1);

        int from_begin = 1;
        int from_end = 1;
        for (int i = 1; i < nums.size(); i++) {
            from_begin *= nums[i-1];
            result[i] *= from_begin;
        }
        for (int i = nums.size() - 2; i >= 0; i--) {
            from_end *= nums[i+1];
            result[i] *= from_end;
        }
        return result;
    }
};

int main() {
    Solution s;
    vector<int> array = {
        1,2,3,4,5
    };
    auto res = s.productExceptSelf(array);
    for (auto e: res) {
        cout << e << ',';
    }
    cout << endl;
}