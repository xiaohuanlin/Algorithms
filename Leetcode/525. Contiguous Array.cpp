#include <unordered_map>
#include <unordered_set>
#include <math.h>
#include <utility>
#include <stack>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;


// Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

// Example 1:
// Input: [0,1]
// Output: 2
// Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
// Example 2:
// Input: [0,1,0]
// Output: 2
// Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
// Note: The length of the given binary array will not exceed 50,000.


class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        unordered_map<int,int> res;
        res[0] = -1;
        int sum = 0;
        int max_v = 0;
        int size = nums.size();
        for (int i = 0; i < size; i++) {
            int v = nums[i] == 1? 1: -1;
            sum += v;
            if (res.find(sum) == res.end()) {
                res[sum] = i;
            } else {
                max_v = max(max_v, i - res[sum]);
            }
        }
        return max_v;
    }
};

int main() {
    vector<int> array {0, 0, 0, 1, 1, 0, 1 ,0};
    Solution s;
    cout << s.findMaxLength(array) << endl;
}