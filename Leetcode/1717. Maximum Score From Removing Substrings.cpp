#include <vector>
#include <queue>
#include <stack>
#include <unordered_map>
#include <algorithm>
#include <iostream>
#include <tuple>
#include <assert.h>
using namespace std;

// You are given a string s and two integers x and y. You can perform two types of operations any number of times.

// Remove substring "ab" and gain x points.
// For example, when removing "ab" from "cabxbae" it becomes "cxbae".
// Remove substring "ba" and gain y points.
// For example, when removing "ba" from "cabxbae" it becomes "cabxe".
// Return the maximum points you can gain after applying the above operations on s.

 

// Example 1:

// Input: s = "cdbcbbaaabab", x = 4, y = 5
// Output: 19
// Explanation:
// - Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
// - Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
// - Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
// - Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
// Total score = 5 + 4 + 5 + 5 = 19.
// Example 2:

// Input: s = "aabbaaxybbaabb", x = 5, y = 4
// Output: 20
 

// Constraints:

// 1 <= s.length <= 10^5
// 1 <= x, y <= 10^4
// s consists of lowercase English letters.

class Solution {
public:
    int maximumGain(string s, int x, int y) {
        stack<char> candidates;
        bool x_first = x > y;
        int sum = 0;

        for (int i = 0; i < s.length(); i++) {
            if (s[i] == 'b') {
                if (x_first && !candidates.empty() && candidates.top() == 'a') {
                    sum += x;
                    candidates.pop();
                } else {
                    candidates.push(s[i]);
                }
            } else if (s[i] == 'a') {
                if (!x_first && !candidates.empty() && candidates.top() == 'b') {
                    sum += y;
                    candidates.pop();
                } else {
                    candidates.push(s[i]);
                }
            }

            if ((s[i] != 'a' && s[i] != 'b') || i == s.length() - 1) {
                // clear stack
                stack<int> tmp; 

                while (!candidates.empty()) {
                    tmp.push(candidates.top());
                    candidates.pop();
                }

                while (!tmp.empty()) {
                    int element = tmp.top();
                    tmp.pop();

                    if (x_first) {
                        if (element == 'a' && !candidates.empty() && candidates.top() == 'b') {
                            sum += y;
                            candidates.pop();
                        } else {
                            candidates.push(element);
                        }
                    } else {
                        if (element == 'b' && !candidates.empty() && candidates.top() == 'a') {
                            sum += x;
                            candidates.pop();
                        } else {
                            candidates.push(element);
                        }
                    }
                }
                candidates = {};
            }
        }

        return sum;
    }
};


int main() {
    Solution s;
    vector<tuple<tuple<string, int, int>, int>> test_cases {
        {{"cdbcbbaaabab", 4, 5}, 19},
        {{"aabbaaxybbaabb", 5, 4}, 20},
    };

    for (auto& test_case: test_cases) {
        assert(s.maximumGain(get<0>(get<0>(test_case)), get<1>(get<0>(test_case)), get<2>(get<0>(test_case))) == get<1>(test_case));
    }
}