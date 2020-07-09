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


// Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

// (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

// Find the minimum element.

// You may assume no duplicate exists in the array.

// Example 1:

// Input: [3,4,5,1,2] 
// Output: 1
// Example 2:

// Input: [4,5,6,7,0,1,2]
// Output: 0

 
class Solution {
public:
    int findMin(vector<int>& nums) {
        if (nums.size() == 0) {
            return 0;
        }
        return find_min(nums, 0, nums.size()-1);
    }

    int find_min(vector<int> &nums, int start, int end) {
        if (start == end) {
            return nums[start];
        }

        if (end - start == 1) {
            return nums[start] < nums[end] ? nums[start]: nums[end];
        }

        int middle_left = start + (end - start) / 2;
        int middle_right = middle_left + 1;
        if (nums[middle_left] > nums[middle_right]) {
            return nums[middle_right];
        } else {
            if (nums[start] < nums[middle_left]) {
                if (nums[start] > nums[end]) {
                    return find_min(nums, middle_right, end);
                } else {
                    return find_min(nums, start, middle_left);
                }
            } else {
                return find_min(nums, start, middle_left);
            }
        }
    }
};

int main() {
    Solution s;
    vector<int> array = {1,2,3,4,5};
    cout << s.findMin(array);
}