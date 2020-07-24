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

// Additive number is a string whose digits can form additive sequence.

// A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

// Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

// Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

 

// Example 1:

// Input: "112358"
// Output: true
// Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
//              1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
// Example 2:

// Input: "199100199"
// Output: true
// Explanation: The additive sequence is: 1, 99, 100, 199. 
//              1 + 99 = 100, 99 + 100 = 199
 

// Constraints:

// num consists only of digits '0'-'9'.
// 1 <= num.length <= 35
// Follow up:
// How would you handle overflow for very large input integers?

class Solution {
public:
	typedef pair<int, int> string_num;
    bool isAdditiveNumber(string num) {
		string_num first;
		string_num second;
		for (int j = 1; j <= num.length(); j++) {
			for (int i = j + 1; i <= num.length(); i++) {
				if (num[j] == '0' && i - j != 1) {
					continue;
				}
				first = make_pair(0, j);
				second = make_pair(j, i - j);
				for (int k = i + 1; k <= num.length(); k++) {
					if (backtrace(num, i, k - i, first, second)) {
						return true;
					}
				}
			}

		}
		return false;
    }


	bool backtrace(string &num, int start, int offset, string_num &first, string_num &second) {
		if (start == num.length()) {
			return true;
		}

		for (int i = offset; start + i <= num.length(); i++) {
			if (num[start] == '0' && i != 1) {
				continue;
			}
			string_num choice = make_pair(start, i);
			if (add_valid(num, first, second, choice)) {
				if (backtrace(num, start+i, i, second, choice)) {
					return true;
				}
			}
		}
		return false;
	}

	bool add_valid(string &num, string_num &a, string_num &b, string_num &c) {
		int first_ptr = a.first + a.second - 1, second_ptr = b.first + b.second - 1, third_ptr = c.first + c.second - 1;
		int carry = 0;
		while (first_ptr >= a.first || second_ptr >= b.first || third_ptr >= c.first) {
			int first_value = first_ptr >= a.first ? num[first_ptr] - '0': 0;
			int second_value = second_ptr >= b.first ? num[second_ptr] - '0': 0;
			int third_value = third_ptr >= c.first ? num[third_ptr] - '0': 0;
			int res = first_value + second_value + carry;
			carry = res / 10;
			if (res % 10 != num[third_ptr] - '0') {
				return false;
			}
			first_ptr --;
			second_ptr --;
			third_ptr --;
		}
		return true;
	}
};


int main() {
	Solution s;
	cout << s.isAdditiveNumber("1203");
}