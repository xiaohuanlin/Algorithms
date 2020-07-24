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

// Given a non-empty array of integers, return the k most frequent elements.

// Example 1:

// Input: nums = [1,1,1,2,2,3], k = 2
// Output: [1,2]
// Example 2:

// Input: nums = [1], k = 1
// Output: [1]
// Note:

// You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
// Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
// It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
// You can return the answer in any order.

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
		map<int, int> res;
		for (int i = 0; i < nums.size(); i ++) {
			if (res.find(nums[i]) == res.end()) {
				res[nums[i]] = 0;
			}
			res[nums[i]]++;
		}
		vector<pair<int, int>> sort_map;
		for (auto iter = res.begin(); iter != res.end(); iter++) {
			sort_map.push_back(make_pair(iter->first, iter->second));
		}
		sort(sort_map.begin(), sort_map.end(), [](pair<int, int> a, pair<int, int> b) {return a.second > b.second; });
		vector<int> result;
		for (int i = 0; i < sort_map.size(); i++) {
			result.push_back(sort_map[i].first);
			if (i >= k - 1) {
				break;
			}
		}
		return result;
    }
};


int main() {
	Solution s;

	vector<int> array = {1,1,2,3,3};
	auto res = s.topKFrequent(array, 2);
	for (auto e: res) {
		cout << e << ',';
	}
	cout << endl;
}