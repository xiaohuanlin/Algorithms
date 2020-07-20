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

// One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as #.

//      _9_
//     /   \
//    3     2
//   / \   / \
//  4   1  #  6
// / \ / \   / \
// # # # #   # #
// For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.

// Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.

// Each comma separated value in the string must be either an integer or a character '#' representing null pointer.

// You may assume that the input format is always valid, for example it could never contain two consecutive commas such as "1,,3".

// Example 1:

// Input: "9,3,4,#,#,1,#,#,2,#,6,#,#"
// Output: true
// Example 2:

// Input: "1,#"
// Output: false
// Example 3:

// Input: "9,#,#,1"
// Output: false

class Solution {
public:
    bool isValidSerialization(string preorder) {

		stack<char> res;
		int count = 0;
		while (count < preorder.length()) {

			res.push(preorder[count]);
			while (is_valid(res)) {
			}

			while (count < preorder.length() && preorder[count] != ',') {
				count ++;
			};
			count ++;
		}

		if (res.empty() || res.top() != '#') {
			return false;
		}
		res.pop();
		return res.empty();
    }

	bool is_valid(stack<char> &res) {
		if (res.empty() || res.top() != '#') {
			return false;
		}
		res.pop();
		if (res.empty() || res.top() != '#') {
			res.push('#');
			return false;
		}
		res.pop();
		if (res.empty() || res.top() == '#') {
			res.push('#');
			res.push('#');
			return false;
		}
		res.pop();
		res.push('#');
		return true;
	}

};



int main() {
	Solution s;
	cout << s.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#");
}