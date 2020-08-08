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


// Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.

// Note:
// Input contains only lowercase English letters.
// Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
// Input length is less than 50,000.
// Example 1:
// Input: "owoztneoer"

// Output: "012"
// Example 2:
// Input: "fviefuro"

// Output: "45"


class Solution {
public:
    string originalDigits(string s) {
        string answer;
        unordered_multiset<char> res;
        for (char &w: s) {
            res.insert(w);
        }

        vector<tuple<char, char, string>> choices {
            make_tuple('z', '0', "zero"),
            make_tuple('x', '6', "six"),
            make_tuple('s', '7', "seven"),
            make_tuple('v', '5', "five"),
            make_tuple('f', '4', "four"),
            make_tuple('r', '3', "three"),
            make_tuple('h', '8', "eight"),
            make_tuple('t', '2', "two"),
            make_tuple('o', '1', "one"),
            make_tuple('n', '9', "nine"),
        };

        for (auto &item: choices) {
            while (res.find(get<0>(item)) != res.end()) {
                answer.push_back(get<1>(item));
                for (char e: get<2>(item)) {
                    res.erase(res.find(e));
                }
            }
        }
        sort(answer.begin(), answer.end());
        return answer;
    }

};


int main() {
    Solution s;
    cout << s.originalDigits("ereht");
}
