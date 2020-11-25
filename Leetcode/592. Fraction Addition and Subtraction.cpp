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


// Given a string representing an expression of fraction addition and subtraction, you need to return the calculation result in string format. The final result should be irreducible fraction. If your final result is an integer, say 2, you need to change it to the format of fraction that has denominator 1. So in this case, 2 should be converted to 2/1.

// Example 1:
// Input:"-1/2+1/2"
// Output: "0/1"
// Example 2:
// Input:"-1/2+1/2+1/3"
// Output: "1/3"
// Example 3:
// Input:"1/3-1/2"
// Output: "-1/6"
// Example 4:
// Input:"5/3+1/3"
// Output: "2/1"
// Note:
// The input string only contains '0' to '9', '/', '+' and '-'. So does the output.
// Each fraction (input and output) has format ±numerator/denominator. If the first input fraction or the output is positive, then '+' will be omitted.
// The input only contains valid irreducible fractions, where the numerator and denominator of each fraction will always be in the range [1,10]. If the denominator is 1, it means this fraction is actually an integer in a fraction format defined above.
// The number of given fractions will be in the range [1,10].
// The numerator and denominator of the final result are guaranteed to be valid and in the range of 32-bit int.


class Solution {
    const long const_denominator = 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10;
public:
    string fractionAddition(string expression) {
        int count = 0;
        int size = expression.size();
        long numerator_result = 0;
        while (count < size) {
            if (count == 0) {
                numerator_result = parse_fraction_numerator(expression, count);
                continue;
            }

            if (expression[count] == '+') {
                numerator_result += parse_fraction_numerator(expression, ++count);
            } else {
                numerator_result -= parse_fraction_numerator(expression, ++count);
            }
        }
        return form_result(numerator_result);
    }

    long parse_fraction_numerator(string &s, int &count) {
        long numerator, denominator;

        int origin = count;
        while (s[count] != '/') {
            count++;
        }
        numerator = atol(s.substr(origin, count - origin).c_str());
        count++;
        origin = count;
        while (count < s.size() && s[count] >= '0' && s[count] <= '9') {
            count++;
        }
        denominator = atol(s.substr(origin, count - origin).c_str());
        return const_denominator / denominator * numerator;
    }

    string form_result(long numerator) {
        if (numerator == 0) {
            return "0/1";
        }
        bool positive = true;
        if (numerator < 0) {
            numerator = -numerator;
            positive = false;
        }

        long gcd = get_gcd(numerator);

        return (positive ? "": "-") + to_string(numerator / gcd) + "/" + to_string(const_denominator / gcd);
    }

    long get_gcd(long numerator) {
        long a = max(numerator, const_denominator);
        long b = min(numerator, const_denominator);

        while (a % b) {
            long remain = a % b;
            a = max(b, remain);
            b = min(b, remain);
        }
        return b;
    }
};

int main() {
    Solution s;
    cout << s.fractionAddition("-4/7") << endl;
}