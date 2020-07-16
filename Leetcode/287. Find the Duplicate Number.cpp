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

// Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

// Example 1:

// Input: [1,3,4,2,2]
// Output: 2
// Example 2:

// Input: [3,1,3,4,2]
// Output: 3
// Note:

// You must not modify the array (assume the array is read only).
// You must use only constant, O(1) extra space.
// Your runtime complexity should be less than O(n2).
// There is only one duplicate number in the array, but it could be repeated more than once.


class Solution {
public:
    int findDuplicate(vector<int>& nums) {
		if (nums.empty()) {
			return -1;
		}
		int start = 1;
		int end = nums.size() - 1;
		while (start <= end) {
			int middle = start + (end - start) / 2;
			int large = 0;
			int less = 0;
			int equal = 0;
			for (int m: nums) {
				if (m > middle) {
					large++;
				} else if (m < middle){
					less++;
				} else {
					equal++;
				}
			}
			
			if (equal >= 2) {
				return middle;
			}

			if (large <= nums.size() - middle - 1) {
				end = middle - 1;
			} else {
				start = middle + 1;
			}
		}
		return nums[start];
    }
};

int main() {
	Solution s;
	vector<int> array = {3,1,1,6,1,2,4,9,8,7};
	cout << s.findDuplicate(array);
}