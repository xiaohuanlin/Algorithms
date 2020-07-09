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


// Given an input string, reverse the string word by word.

 

// Example 1:

// Input: "the sky is blue"
// Output: "blue is sky the"
// Example 2:

// Input: "  hello world!  "
// Output: "world! hello"
// Explanation: Your reversed string should not contain leading or trailing spaces.
// Example 3:

// Input: "a good   example"
// Output: "example good a"
// Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

// Note:

// A word is defined as a sequence of non-space characters.
// Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
// You need to reduce multiple spaces between two words to a single space in the reversed string.
 

// Follow up:

// For C programmers, try to solve it in-place in O(1) extra space.

 
class Solution {
public:
    string reverseWords(string s) {
        clean_str(s);
        cout << s << endl;
        reverse(s, 0, s.length() - 1);

        int start = 0;
        int count = 0;

        while (count < s.length()) {
            while (count < s.length() && s[count] != ' ') {
                count ++;
            }

            reverse(s, start, count-1);

            while (count < s.length() && s[count] == ' ') {
                count ++;
            }
            start = count;
        }
        return s;
    }

    void clean_str(string &s) {
        int count = 0;
        int start = 0;

        while (count < s.length()) {
            while (count < s.length() && s[count] == ' ') {
                count ++;
            }

            while (count < s.length() && s[count] != ' ') {
                s[start++] = s[count++];
            }

            if (count < s.length()) {
                s[start++] = s[count++];
            }
        }

        if (start != 0 && s[start-1] == ' ') {
            s.resize(start-1);
        } else {
            s.resize(start);
        }
    }

    void reverse(string &s, int start, int end) {
        while (start < end) {
            swap(s[start++], s[end--]);
        }
    }
};

int main() {
    Solution s;
    cout << s.reverseWords("a good   example");
}