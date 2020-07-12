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


// Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

// Example 1:

// Input: [3,2,1,5,6,4] and k = 2
// Output: 5
// Example 2:

// Input: [3,2,3,1,2,4,5,5,6] and k = 4
// Output: 4
// Note: 
// You may assume k is always valid, 1 ≤ k ≤ array's length.


class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        int iter_start, start = 0;
        int iter_end, end = nums.size() - 1;
        while (start < end) {
            iter_start = start;
            iter_end = end;
            while (iter_start < iter_end) {
                if (nums[iter_start] <= nums[iter_end]) {
                    iter_start++;
                } else {
                    swap(nums[iter_start], nums[iter_end-1]);
                    swap(nums[iter_end-1], nums[iter_end]);
                    iter_end--;
                }
            } 
            if (iter_end < nums.size() - k) {
                start = iter_end + 1;
            } else if (iter_end > nums.size() - k) {
                end = iter_end - 1;
            } else {
                return nums[iter_end];
            }
        }
        return nums[start];
    }

};

int main() {
    Solution s;
    vector<int> array = {1,2,3,1};
    cout << s.findKthLargest(array, 3);
}
