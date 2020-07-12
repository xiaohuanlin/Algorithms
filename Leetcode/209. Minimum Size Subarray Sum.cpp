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


// Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

// Example: 

// Input: s = 7, nums = [2,3,1,2,4,3]
// Output: 2
// Explanation: the subarray [4,3] has the minimal length under the problem constraint.
// Follow up:
// If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 

class Solution {
public:
    int minSubArrayLen(int s, vector<int>& nums) {
        int min = nums.size();
        bool found = false;
        for (int i = 0; i < nums.size(); i++) {
            int sum = 0;
            int count = nums.size();
            int j = i;
            for (; j >= 0; j--) {
                if (sum >= s) {
                    count = i - j;
                    found = true;
                    break;
                }
                sum += nums[j];
            }
            if (sum >= s) {
                count = i - j;
                found = true;
            }

            if (count < min) {
                min = count;
            }
        }
        if (!found) {
            return 0;
        }
        return min;
    }
};


int main() {
    Solution s;
    vector<int> array = {2,3,1,2,4,3};
    cout << s.minSubArrayLen(8, array);
}