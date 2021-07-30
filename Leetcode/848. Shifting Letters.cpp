#include <vector>
#include <stack>
#include <iostream>
#include <tuple>
#include <assert.h>
#include <algorithm>
using namespace std;


// You are given a string s of lowercase English letters and an integer array shifts of the same length.

// Call the shift() of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a').

// For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.
// Now for each shifts[i] = x, we want to shift the first i + 1 letters of s, x times.

// Return the final string after all such shifts to s are applied.

 

// Example 1:

// Input: s = "abc", shifts = [3,5,9]
// Output: "rpl"
// Explanation: We start with "abc".
// After shifting the first 1 letters of s by 3, we have "dbc".
// After shifting the first 2 letters of s by 5, we have "igc".
// After shifting the first 3 letters of s by 9, we have "rpl", the answer.
// Example 2:

// Input: s = "aaa", shifts = [1,2,3]
// Output: "gfd"
 

// Constraints:

// 1 <= s.length <= 10^5
// s consists of lowercase English letters.
// shifts.length == s.length
// 0 <= shifts[i] <= 10^9

class Solution {
public:
    string shiftingLetters(string s, vector<int>& shifts) {
        int count = 0;
        for (int i = 0; i < shifts.size(); ++i) {
            count += (shifts[i] % 26);
        }

        int subtract_res = 0;
        for (int i = 0; i < shifts.size(); ++i) {
            if (i > 0) {
                subtract_res = (subtract_res + shifts[i - 1]) % 26;
            }
            int change = (s[i] - 'a' + count - subtract_res) % 26;
            if (change < 0) {
                change += 26;
            }
            s[i] = 'a' + change;
        }
        return s;
    }
};

int main() {
    Solution s;
    vector<tuple<tuple<string, vector<int>>, string>> test_cases {
        {{"bad", {10, 20, 30}}, "jyh"},
        {{"z", {52}}, "z"},
        {{"ab", {3, 5}}, "ig"},
        {{"abc", {3, 5, 9}}, "rpl"},
        {{"aaa", {1, 2, 3}}, "gfd"},
    };

    for (auto& test_case: test_cases) {
        assert(s.shiftingLetters(get<0>(get<0>(test_case)), get<1>(get<0>(test_case))) == get<1>(test_case));
    }
}