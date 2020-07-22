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
		int middle_size = (nums.size() - 1) / 2;
		if (middle_size <= 0) {
			return;
		}

		nth_element(nums.begin(), nums.begin() + middle_size, nums.end());
		int middle_value = nums[middle_size];

		// odd place larger number, even place small number
		int odd = 1;
		int even = (nums.size() - 1) % 2 == 0? nums.size() - 1: nums.size() - 2;
		int count = 0;
		while (count < nums.size()) {
			if (nums[count] > middle_size && (count > odd || count % 2 == 0)) {
				swap(nums[count], nums[odd]);
				odd += 2;
			} else if (nums[count] < middle_size && (count < even || count % 2 == 1)) {
				swap(nums[count], nums[even]);
				even -= 2;
			} else {
				count ++;
			}
		}
    }
};


int main() {
	Solution s;
	vector<int> array = {1,3,2,2,3,1};
	s.wiggleSort(array);
	for (auto e: array) {
		cout << e << ',';
	}
	cout << endl;
	// todo
}