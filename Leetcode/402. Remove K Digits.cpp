#include <utility>
#include <stack>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;


// Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

// Note:
// The length of num is less than 10002 and will be ≥ k.
// The given num does not contain any leading zero.
// Example 1:

// Input: num = "1432219", k = 3
// Output: "1219"
// Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
// Example 2:

// Input: num = "10200", k = 1
// Output: "200"
// Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
// Example 3:

// Input: num = "10", k = 2
// Output: "0"
// Explanation: Remove all the digits from the number and it is left with nothing which is 0.


class Solution {
public:
    string removeKdigits(string num, int k) {
        if (num.length() == 0 || k < 0){
            return "";
        }

        vector<char> found;

        for (int i = 0; i < num.length(); i++) {
            while (k > 0 && found.size() > 0 && found.back() > num[i]) {
                found.pop_back();
                k--;
            }
            found.push_back(num[i]);
        }

        // if k still > 0, and we need delete elements
        int size = found.size();
        for (int i = 0; i < size && k > 0; i++) {
            found.pop_back();
            k--;
        }

        // remove leading zero
        bool init = false;
        string s;
        for (int j = 0; j < found.size(); j++) {
            if (!init && found[j] > '0') {
                init = true;
            }

            if (init) {
                s.push_back(found[j]);
            }
        }

        if (!init) {
            return "0";
        }
        return s;
    }
};


int main() {
    Solution s;
    cout << s.removeKdigits("12340", 4);
}