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

// Given a string, your task is to count how many palindromic substrings in this string.

// The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

// Example 1:

// Input: "abc"
// Output: 3
// Explanation: Three palindromic strings: "a", "b", "c".
 

// Example 2:

// Input: "aaa"
// Output: 6
// Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

// Note:

// The input string length won't exceed 1000.

class Solution {
public:
    int countSubstrings(string s) {
        // store the index of same alphabet
        vector<int> vector_array[26] = {};
        vector<vector<bool>> validated_value(s.length(), vector<bool>(s.length(), false));
        for (int i = 0; i < s.length(); ++i) {
            vector_array[s[i] - 'a'].push_back(i);
        }

        int res = 0;
        for (int k = 0; k < s.length(); ++k) {
            vector<int> same_v = vector_array[s[k] - 'a'];
            for (int j = 0; j < same_v.size(); ++j) {
                if (same_v[j] > k) {
                    continue;
                }

                if (same_v[j] + 1 <= k - 1 && !validated_value[same_v[j] + 1][k - 1]) {
                    continue;
                }

                res++;
                validated_value[same_v[j]][k] = true;
            }
        }
        return res;
    }
};

int main() {
    Solution s;
    cout << s.countSubstrings("bcd") << endl;
}