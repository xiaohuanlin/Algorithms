#include <vector>
#include <stack>
#include <unordered_map>
#include <algorithm>
#include <iostream>
#include <tuple>
#include <assert.h>
using namespace std;

// You are given a binary string binary consisting of only 0's or 1's. You can apply each of the following operations any number of times:

// Operation 1: If the number contains the substring "00", you can replace it with "10".
// For example, "00010" -> "10010"
// Operation 2: If the number contains the substring "10", you can replace it with "01".
// For example, "00010" -> "00001"
// Return the maximum binary string you can obtain after any number of operations. Binary string x is greater than binary string y if x's decimal representation is greater than y's decimal representation.

 

// Example 1:

// Input: binary = "000110"
// Output: "111011"
// Explanation: A valid transformation sequence can be:
// "000110" -> "000101" 
// "000101" -> "100101" 
// "100101" -> "110101" 
// "110101" -> "110011" 
// "110011" -> "111011"
// Example 2:

// Input: binary = "01"
// Output: "01"
// Explanation: "01" cannot be transformed any further.
 

// Constraints:

// 1 <= binary.length <= 10^5
// binary consist of '0' and '1'.

class Solution {
public:
    string maximumBinaryString(string binary) {
        int zero_count = 0;
        int left_zero = -1;
        for (int i = 0; i < binary.length(); i++) {
            if (binary[i] == '0') {
                zero_count++;
                if (left_zero == -1) {
                    left_zero = i;
                }
            }
        }

        if (zero_count < 2) {
            return binary;
        }

        int zero_position = left_zero + zero_count - 1;

        string res;
        for (int i = 0; i < binary.length(); i++) {
            if (i == zero_position) {
                res.push_back('0');
            } else {
                res.push_back('1');
            }
        }
        return res;
    }
};


int main() {
    Solution s;
    vector<tuple<string, string>> test_cases {
        {"1", "1"},
        {"000110", "111011"},
        {"01", "01"},
    };

    for (auto& test_case: test_cases) {
        assert(s.maximumBinaryString(get<0>(test_case)) == get<1>(test_case));
    }
}