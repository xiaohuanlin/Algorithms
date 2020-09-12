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

// Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

// Note:
// The array size can be very large. Solution that uses too much extra space will not pass the judge.

// Example:

// int[] nums = new int[] {1,2,3,3,3};
// Solution solution = new Solution(nums);

// // pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
// solution.pick(3);

// // pick(1) should return 0. Since in the array only nums[0] is equal to 1.
// solution.pick(1);


class Solution {
    vector<int>::iterator begin;
    vector<int>::iterator end;
public:
    Solution(vector<int>& nums): begin(nums.begin()), end(nums.end()) {
    }
    
    int pick(int target) {
        int res = -1;
        int count = 1;
        int dis = 0;
        for (auto iter = begin; iter < end; ++iter) {
            if (*iter == target) {
                if (rand() % count == 0) {
                    res = dis;
                }
                ++count;
            }

            ++dis;
        }
        return res;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums);
 * int param_1 = obj->pick(target);
 */


int main() {
    vector<int> array {1,2,3,1,2};
    Solution* obj = new Solution(array);
    cout << obj->pick(2);
    cout << obj->pick(2);
    cout << obj->pick(2);
    cout << obj->pick(2);

}