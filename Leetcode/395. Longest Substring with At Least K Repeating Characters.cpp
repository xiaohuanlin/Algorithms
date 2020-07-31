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
#include <queue>
using namespace std;


// Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

// Example 1:

// Input:
// s = "aaabb", k = 3

// Output:
// 3

// The longest substring is "aaa", as 'a' is repeated 3 times.
// Example 2:

// Input:
// s = "ababbc", k = 2

// Output:
// 5

// The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.


class Solution {
public:
    int longestSubstring(string s, int k) {
        // store all index of all possible word
        vector<vector<int>> index(26, vector<int>());
        for (int i = 0; i < s.length(); i++) {
            // todo
        }
    }

};

int main() {
    Solution s;
    cout << s.longestSubstring("ibbicccccizzzktttt", 3);
}
