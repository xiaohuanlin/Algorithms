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

// Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

// Example 1:

// Input: nums = [1, 5, 1, 1, 6, 4]
// Output: One possible answer is [1, 4, 1, 5, 1, 6].
// Example 2:

// Input: nums = [1, 3, 2, 2, 3, 1]
// Output: One possible answer is [2, 3, 1, 3, 1, 2].
// Note:
// You may assume all input has valid answer.

// Follow Up:
// Can you do it in O(n) time and/or in-place with O(1) extra space?

class Solution {
public:
    void wiggleSort(vector<int>& nums) {
		if (nums.size() <= 1) {
			return;
		}

		if (nums[0] > nums[1]) {
			swap(nums[0], nums[1]);
		}

		for (int i = 2; i < nums.size(); i++) {
			if (!((nums[i-2] < nums[i-1]) ^ (nums[i-1] < nums[i]))) {
				swap(nums[i-1], nums[i]);
			}
		}
    }
};


int main() {
	Solution s;
	vector<int> array = {1,5,1,1,6,4};
	s.wiggleSort(array);
	for (auto e: array) {
		cout << e << ',';
	}
	cout << endl;
	// todo
}