#include <unordered_map>
#include <unordered_set>
#include <math.h>
#include <utility>
#include <stack>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;


// Given two strings representing two complex numbers.

// You need to return a string representing their multiplication. Note i2 = -1 according to the definition.

// Example 1:
// Input: "1+1i", "1+1i"
// Output: "0+2i"
// Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
// Example 2:
// Input: "1+-1i", "1+-1i"
// Output: "0+-2i"
// Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
// Note:

// The input strings will not have extra blank.
// The input strings will be given in the form of a+bi, where the integer a and b will both belong to the range of [-100, 100]. And the output should be also in this form.

class Solution {
public:
    string complexNumberMultiply(string a, string b) {
        int arg_a_0, arg_a_1, arg_b_0, arg_b_1;
        sscanf(a.c_str(), "%d+%di", &arg_a_0, &arg_a_1);
        sscanf(b.c_str(), "%d+%di", &arg_b_0, &arg_b_1);

        char answer[32];
        sprintf(answer, "%d+%di", arg_a_0 * arg_b_0 - arg_a_1 * arg_b_1,
                        arg_a_1 * arg_b_0 + arg_a_0 * arg_b_1);
        return string(answer);
    }
};

int main() {
    Solution s;
    cout << s.complexNumberMultiply("1+1i", "1+1i") << endl;
}