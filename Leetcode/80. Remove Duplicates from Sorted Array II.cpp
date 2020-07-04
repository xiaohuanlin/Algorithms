#include <utility>
#include <stack>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;

// Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

// Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

// Example 1:

// Given nums = [1,1,1,2,2,3],

// Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

// It doesn't matter what you leave beyond the returned length.
// Example 2:

// Given nums = [0,0,1,1,1,1,2,3,3],

// Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.

// It doesn't matter what values are set beyond the returned length.
// Clarification:

// Confused why the returned value is an integer but your answer is an array?

// Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

// Internally you can think of this:

// // nums is passed in by reference. (i.e., without making a copy)
// int len = removeDuplicates(nums);

// // any modification to nums in your function would be known by the caller.
// // using the length returned by your function, it prints the first len elements.
// for (int i = 0; i < len; i++) {
//     print(nums[i]);
// }

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        return remove(nums, 0, nums.size());
    }

    int remove(vector<int>&nums, int start, int end) {
        if (end - start <= 2) {
            return end - start;
        }

        int middle = start + (end - start) / 2;
        int left_remain = remove(nums, start, middle);
        int right_remain = remove(nums, middle, end);

        int cut_index = middle;
        if (left_remain > 0 && right_remain > 0) {
            int left_last = nums[start+left_remain-1];
            int right_first = nums[middle];
            if (left_last == right_first) {
                if (left_remain > 1 && nums[start+left_remain-2] == left_last) {
                    if (right_remain > 1 && nums[middle+1] == left_last) {
                        cut_index = middle+2;
                        right_remain -= 2;
                    } else {
                        cut_index = middle+1;
                        right_remain--;
                    }
                } else if(right_remain > 1 && nums[middle+1] == left_last) {
                    cut_index = middle+1;
                    right_remain--;
                }
            }
        }

        // swap
        for (int i = 0; i < right_remain; i++) {
            swap(nums[start+left_remain+i], nums[cut_index+i]);
        }
        return left_remain + right_remain; 
    }


    int removeDuplicatesNew(vector<int>& nums) {
        if (nums.size() <= 2) {
            return nums.size();
        }
        int useless_index = -1;
        for (int i = 2; i < nums.size(); i++) {
            if (useless_index == -1 && nums[i] != nums[i-2]) {
                continue;
            }

            if (useless_index == -1) {
                useless_index = i;
            } else if (nums[i] != nums[useless_index-1] || (nums[i] == nums[useless_index-1] && nums[i] != nums[useless_index-2])) {
                swap(nums[useless_index++], nums[i]);
            }
        }
        return useless_index > 0? useless_index: nums.size();
    }
};

int main() {
    Solution s;
    vector<int> array = {1,1,1,2,2,2,3,3};
    cout << s.removeDuplicatesNew(array) << endl;

    for (auto e: array) {
        cout << e << ',';
    }
    cout << endl;
}