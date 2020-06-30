#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;

// Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

// (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

// You are given a target value to search. If found in the array return its index, otherwise return -1.

// You may assume no duplicate exists in the array.

// Your algorithm's runtime complexity must be in the order of O(log n).

// Example 1:

// Input: nums = [4,5,6,7,0,1,2], target = 0
// Output: 4
// Example 2:

// Input: nums = [4,5,6,7,0,1,2], target = 3
// Output: -1

class Solution {
public:
    int search(vector<int>& nums, int target) {
        if (nums.size() == 0) {
            return -1;
        }
        return coresearch(nums, target, 0, nums.size() - 1);
    }

    int coresearch(vector<int> &nums, int target, int start, int end) {
        if (start > end) {
            return -1;
        }

        if (nums[start] < nums[end]) {
            return bisearch(nums, target, start, end);
        }

        if (target < nums[start] && target > nums[end]) {
            return -1;
        }

        int middle = start + (end-start) / 2;
        if (nums[middle] > target) {
            if (nums[middle] < nums[end]) {
                return coresearch(nums, target, start, middle - 1);
            } else if (target < nums[end]) {
                return coresearch(nums, target, middle + 1, end - 1);
            } else if (target > nums[start]) {
                return bisearch(nums, target, start + 1, middle -1);
            } else if (target == nums[start]) {
                return start;
            } else {
                return end;
            }

        } else if (nums[middle] < target) {
            if (nums[middle] > nums[start]) {
                return coresearch(nums, target, middle + 1, end);
            } else if (target > nums[start]) {
                return coresearch(nums, target, start + 1, middle - 1);
            } else if (target < nums[end]) {
                return bisearch(nums, target, middle + 1, end - 1);
            } else if (target == nums[start]) {
                return start;
            } else {
                return end;
            }
        } else {
            return middle;
        }
    }

    int bisearch(vector<int> &nums, int target, int start, int end) {
        if (start > end) {
            return -1;
        }

        while (start < end) {
            int middle = start + (end - start) / 2;
            if (target == nums[middle]) {
                start = middle;
                break;
            } else if (target > nums[middle]) {
                start = middle + 1;
            } else {
                end = middle - 1;
            }
        }
        
        if (nums[start] != target) {
            return -1;
        } else {
            return start;
        }
    }
};


int main() {
    Solution s;
    vector<int> array = {4, 5, 6, 0, 1, 2};
    cout << s.search(array, 0);
}