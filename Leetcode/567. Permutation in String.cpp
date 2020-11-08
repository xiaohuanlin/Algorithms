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


// Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

 

// Example 1:

// Input: s1 = "ab" s2 = "eidbaooo"
// Output: True
// Explanation: s2 contains one permutation of s1 ("ba").
// Example 2:

// Input:s1= "ab" s2 = "eidboaoo"
// Output: False
 

// Constraints:

// The input strings only contain lower case letters.
// The length of both given strings is in range [1, 10,000].


class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int s1_count[26] = {};
        int s2_count[26] = {};

        int size_s1 = s1.size();
        int size_s2 = s2.size();
        if (size_s1 > size_s2) {
            return false;
        }
        for (int i = 0; i < size_s1; i++) {
            s1_count[s1[i] - 'a']++;
            s2_count[s2[i] - 'a']++;
        }

        int delta = 0;
        do {
            if (equal(s1_count, s2_count)) {
                return true;
            }
            if (size_s1 + delta >= size_s2) {
                return false;
            }
            // remove oldest count
            s2_count[s2[0 + delta] - 'a']--;
            // increase newest count
            s2_count[s2[size_s1 + delta] - 'a']++;
            delta++;
        }
        while (size_s1 + delta <= size_s2);
        return false;
    }

    bool equal(int a[26], int b[26]) {
        int i = 0;
        while (i < 26) {
            if (a[i] != b[i]) {
                return false;
            }
            i++;
        }
        return true;
    }
};


int main() {
    Solution s;
    cout << boolalpha << s.checkInclusion("ab", "sdsdrba") << endl;
}
