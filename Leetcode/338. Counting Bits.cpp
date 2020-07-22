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

// Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

// Example 1:

// Input: 2
// Output: [0,1,1]
// Example 2:

// Input: 5
// Output: [0,1,1,2,1,2]
// Follow up:

// It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
// Space complexity should be O(n).
// Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.

class Solution {
public:
    vector<int> countBits(int num) {
		vector<int> res(num + 1, 0);
		int count = 1;
		while (count < num+1) {
			int start = 0;
			while (start < count && start + count < num+1) {
				res[start + count] = res[start] + 1;
				start ++;
			}
			count *= 2;
		}
		return res;
    }
};

int main() {
	Solution s;
	auto array = s.countBits(10);
	for (auto e: array) {
		cout << e << ',';
	}
	cout << endl;
}