#include <utility>
#include <stack>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;

// Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

// (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

// You are given a target value to search. If found in the array return true, otherwise return false.

// Example 1:

// Input: nums = [2,5,6,0,0,1,2], target = 0
// Output: true
// Example 2:

// Input: nums = [2,5,6,0,0,1,2], target = 3
// Output: false
// Follow up:

// This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
// Would this affect the run-time complexity? How and why?

class Solution {
public:
    bool search(vector<int>& nums, int target) {
        return get_search(nums, target, 0, nums.size()-1);
    }
    
    bool get_search(vector<int>& nums, int target, int start, int end) {
        int middle = start + (end - start) / 2;
        if (start > end) {
            return false;
        }

        if (start == end) {
            return nums[start] == target;
        }

        if (nums[middle] == target) {
            return true;
        }

        if (target < nums[middle]) {
            if (target > nums[start]) {
                return get_search(nums, target, start+1, middle-1);
            } else if (target == nums[start]) {
                return true;
            } else {
                if (nums[middle] < nums[end]) {
                    return get_search(nums, target, start+1, middle-1);
                } else if (nums[middle] > nums[end]) {
                    return get_search(nums, target, middle+1, end);
                } else {
                    return get_search(nums, target, middle+1, end) || get_search(nums, target, start+1, middle-1);
                }
            }
        } else {
            if (target < nums[end]) {
                return get_search(nums, target, middle+1, end-1);
            } else if (target == nums[end]) {
                return true;
            } else {
                if (nums[middle] > nums[start]) {
                    return get_search(nums, target, middle+1, end-1);
                } else if (nums[middle] < nums[start]) {
                    return get_search(nums, target, start, middle-1);
                } else {
                    return get_search(nums, target, start, middle-1) || get_search(nums, target, middle+1, end-1);
                }
            }
        }
    }
};

int main() {
    Solution s;
    vector<int> array = {1,1,3,1};
    cout << s.search(array, 3);

}