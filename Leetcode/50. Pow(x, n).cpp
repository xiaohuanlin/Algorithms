#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;

// Implement pow(x, n), which calculates x raised to the power n (xn).

// Example 1:

// Input: 2.00000, 10
// Output: 1024.00000
// Example 2:

// Input: 2.10000, 3
// Output: 9.26100
// Example 3:

// Input: 2.00000, -2
// Output: 0.25000
// Explanation: 2-2 = 1/22 = 1/4 = 0.25
// Note:

// -100.0 < x < 100.0
// n is a 32-bit signed integer, within the range [−231, 231 − 1]

class Solution {
public:
    double myPow(double x, int n) {
        bool power_negative = (n < 0);
        if (power_negative) {
            if (n == INT32_MIN) {
                return myPow(x, n + 1) * myPow(x, -1);
            }
            n = -n;
        }

        double sum = 1;
        double cur_pow = x;
        while (n > 0) {
            if ((n & 1) > 0) {
                sum *= cur_pow;
            }
            cur_pow *= cur_pow;
            n >>= 1;
        }

        if (power_negative) {
            sum = 1 / sum;
        }

        return sum;
    }
};

int main() {
    Solution s;
    cout << s.myPow(-2, 2);
}
