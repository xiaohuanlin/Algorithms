#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;

// Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

// Return the quotient after dividing dividend by divisor.

// The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

// Example 1:

// Input: dividend = 10, divisor = 3
// Output: 3
// Explanation: 10/3 = truncate(3.33333..) = 3.
// Example 2:

// Input: dividend = 7, divisor = -3
// Output: -2
// Explanation: 7/-3 = truncate(-2.33333..) = -2.
// Note:

// Both dividend and divisor will be 32-bit signed integers.
// The divisor will never be 0.
// Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.


class Solution {
public:
    int divide(int dividend, int divisor) {
        bool negative = (dividend < 0) ^ (divisor < 0);
        long long abs_dividend = dividend > 0? dividend: -(long long)dividend;
        long long abs_divisor = divisor > 0? divisor: -(long long)divisor;

        unsigned long long res = 0;

        while (abs_dividend >= abs_divisor) {
            long long start = 1;
            long long cur_value = 0;
            while ((start * abs_divisor) <= abs_dividend) {
                cur_value = start;
                start <<= 1;
            }
            res += cur_value;
            abs_dividend -= (cur_value * abs_divisor);
        }

        if (!negative && res > 0x7fffffff) {
            return 0x7fffffff;
        } else {
            if (negative) {
                return -res;
            } else {
                return res;
            }
        }
    }
};


int main() {
    Solution s;

    auto res = s.divide(2436, 11);
    cout << res;
}