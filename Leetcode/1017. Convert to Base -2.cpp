#include <vector>
#include <deque>
#include <algorithm>
#include <iostream>
#include <tuple>
#include <assert.h>
using namespace std;


// Given an integer n, return a binary string representing its representation in base -2.

// Note that the returned string should not have leading zeros unless the string is "0".

 

// Example 1:

// Input: n = 2
// Output: "110"
// Explantion: (-2)2 + (-2)1 = 2
// Example 2:

// Input: n = 3
// Output: "111"
// Explantion: (-2)2 + (-2)1 + (-2)0 = 3
// Example 3:

// Input: n = 4
// Output: "100"
// Explantion: (-2)2 = 4
 

// Constraints:

// 0 <= n <= 10^9
 
class Solution {
public:
    string baseNeg2(int n) {
        if (n == 0) {
            return "0";
        }

        deque<char> res;
        while (n != 0) {
            int remain = abs(n % (-2));
            n = (n - remain) / (-2);
            res.push_front(remain + '0');
        }
        return {res.begin(), res.end()};
    }
};

int main() {
    Solution s;
    vector<tuple<int, string>> test_cases {
        {0, "0"},
        {1, "1"},
        {2, "110"},
        {3, "111"},
        {4, "100"},
    };

    for (auto& test_case: test_cases) {
        assert(s.baseNeg2(get<0>(test_case)) == get<1>(test_case));
    }
}