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


// All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

// Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

// Example:

// Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

// Output: ["AAAAACCCCC", "CCCCCAAAAA"]


class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        unordered_set<string> once;
        unordered_set<string> twice;

        for (int i = 9; i < s.length(); i++) {
            string subs = s.substr(i - 9, 10);
            if (twice.find(subs) != twice.end()) {
                continue;
            }
            if (once.find(subs) != once.end()) {
                once.erase(subs);
                twice.insert(subs);
            } else {
                once.insert(subs);
            }
        }
        return vector<string>(twice.begin(), twice.end());
    }
};


int main() {
    Solution s;
    auto res = s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT");
    for (auto e: res) {

        cout << e << endl;
    }
}