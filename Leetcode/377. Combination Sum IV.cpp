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
#include <queue>
using namespace std;

// Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

// Example:

// nums = [1, 2, 3]
// target = 4

// The possible combination ways are:
// (1, 1, 1, 1)
// (1, 1, 2)
// (1, 2, 1)
// (1, 3)
// (2, 1, 1)
// (2, 2)
// (3, 1)

// Note that different sequences are counted as different combinations.

// Therefore the output is 7.
 

// Follow up:
// What if negative numbers are allowed in the given array?
// How does it change the problem?
// What limitation we need to add to the question to allow negative numbers?

// Credits:
// Special thanks to @pbrother for adding this problem and creating all test cases.


class Solution {
    unordered_map<int, int> cache;
public:
    int combinationSum4(vector<int>& nums, int target) {
        if (cache.find(target) != cache.end()) {
            return cache[target];
        }

        if (target == 0) {
            return 1;
        } else if (target < 0) {
            return 0;
        }

        int sum = 0;

        for (auto &num: nums) {
            sum += combinationSum4(nums, target - num);
        }

        cache[target] = sum;
        return sum;
    }
};


int main() {
    Solution s;
    vector<int> array = {1,2,3};
    cout << s.combinationSum4(array, 4);
}
