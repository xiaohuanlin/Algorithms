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


// Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to a multiple of k, that is, sums up to n*k where n is also an integer.

 

// Example 1:

// Input: [23, 2, 4, 6, 7],  k=6
// Output: True
// Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
// Example 2:

// Input: [23, 2, 6, 4, 7],  k=6
// Output: True
// Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
 

// Constraints:

// The length of the array won't exceed 10,000.
// You may assume the sum of all the numbers is in the range of a signed 32-bit integer.


class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        unordered_map<int, vector<int>> res;       
        res[0].push_back(-1);
        int sum = 0;
        int size = nums.size();
        for (int i = 0; i < size; i++) {
            sum += nums[i];
            if (k != 0) {
                sum %= k;
            }

            // find previous index
            if (!res[sum].empty()) {
                int prev = res[sum].front();
                if (i - prev > 1) {
                    return true;
                }
            }
            res[sum].push_back(i);
        }

        return false;
    }
};

int main() {
    vector<int> array {23,2,6};
    Solution s;
    cout << boolalpha << s.checkSubarraySum(array, 6) << endl;
}