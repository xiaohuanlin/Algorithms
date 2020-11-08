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


// Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

// Note:

// Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

// Example 1:

// Input: [2,2,3,2]
// Output: 3
// Example 2:

// Input: [0,1,0,1,0,1,99]
// Output: 99


class Solution {
public:
    int singleNumber(vector<int>& nums) {
        // the number appear more than once will have special pattern for certain bit, so find it and 
        // figure out what is the special number
        int shift = 0;
        unsigned int res = 0;
        while (shift < 32) {
            unsigned int count = 0;
            for (int i = 0; i < nums.size(); i++) {
                count += ((nums[i] >> shift) & 1);
            }
            if (count % 3) {
                res = res + (1 << shift);
            }
            shift++;
        }
        return res;
    }
};


int main() {
}