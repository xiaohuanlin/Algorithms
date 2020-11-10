#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
#include <unordered_map>
using namespace std;


// Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

// Follow up: Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

 

// Example 1:

// Input: nums = [1,2,1,3,2,5]
// Output: [3,5]
// Explanation:  [5, 3] is also a valid answer.
// Example 2:

// Input: nums = [-1,0]
// Output: [-1,0]
// Example 3:

// Input: nums = [0,1]
// Output: [1,0]
 

// Constraints:

// 1 <= nums.length <= 30000
//  Each integer in nums will appear twice, only two integers will appear once.


class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        if (nums.size() < 2) {
            return {};
        }
        int xor_res = nums[0];
        for (int i = 1; i < nums.size(); i++) {
            xor_res ^= nums[i];
        }

        // find the position of 1, which means we can divide those two number into
        // different groups.
        int count = 0;
        while (xor_res) {
            if ((xor_res >> count) & 1) {
                break;
            }
            count++;
        }

        int xor_res_for_1 = xor_res;
        int xor_res_for_2 = xor_res;
        for (int i = 0; i < nums.size(); i++) {
            if ((nums[i] >> count) & 1) {
                xor_res_for_1 ^= nums[i];
            } else {
                xor_res_for_2 ^= nums[i];
            }
        }
        return {xor_res_for_1, xor_res_for_2};
    }
};


int main() {
}