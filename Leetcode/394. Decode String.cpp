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


// Given an encoded string, return its decoded string.

// The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

// You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

// Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

 

// Example 1:

// Input: s = "3[a]2[bc]"
// Output: "aaabcbc"
// Example 2:

// Input: s = "3[a2[c]]"
// Output: "accaccacc"
// Example 3:

// Input: s = "2[abc]3[cd]ef"
// Output: "abcabccdcdcdef"
// Example 4:

// Input: s = "abc3[cd]xyz"
// Output: "abccdcdcdxyz"


class Solution {
public:
    string decodeString(string s) {
        stack<int> pos;        
        stack<int> num_pos;        

        int count = 0;
        while (count < s.length()) {
            if (s[count] == '[') {
                pos.push(count);
            }

            if (isdigit(s[count])) {
                int delta = 0;
                while (isdigit(s[count])) {
                    ++count;
                    ++delta;
                }
                num_pos.push(delta);
                continue;
            }

            if (s[count] == ']') {
                string inner = s.substr(pos.top() + 1, count - pos.top() - 1);
                int repeat_num = stoi(s.substr(pos.top() - num_pos.top(), num_pos.top()));

                string res;
                for (int i = 0; i < repeat_num; ++i) {
                    res += inner;
                }

                int remain_length = s.length() - count - 1;
                // substitute
                s = s.substr(0, pos.top() - num_pos.top()) + res + s.substr(count+1, remain_length);
                pos.pop();
                num_pos.pop();
                count = s.length() - remain_length - 1;
            }
            ++count;
        }
        return s;
    }
};


int main() {
    Solution s;
    cout << s.decodeString("3[a2[c]]b");
}
