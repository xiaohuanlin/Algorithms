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


// Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

// Example 1:

// Input: [5,7]
// Output: 4
// Example 2:

// Input: [0,1]
// Output: 0


class Solution {
public:
    int rangeBitwiseAnd(int m, int n) {
        if (m == 0 && n == INT32_MAX) {
            return 0;
        }

        int stand = 1;
        int size = n - m + 1;
        int res = 0, count = 0;

        while (n && m) {
            if (size <= stand) {
                res += ((m & 1) & (n & 1)) << count;
            }

            count++;
            n >>= 1;
            m >>= 1;
            stand <<= 1;
        }
        return res;
    }
};

int main() {
    Solution s;
    cout << s.rangeBitwiseAnd(0, 2147483647);
}