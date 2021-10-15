#include <vector>
#include <stack>
#include <iostream>
#include <tuple>
#include <assert.h>
#include <algorithm>
using namespace std;

// Let f(x) be the number of zeroes at the end of x!. Recall that x! = 1 * 2 * 3 * ... * x and by convention, 0! = 1.

// For example, f(3) = 0 because 3! = 6 has no zeroes at the end, while f(11) = 2 because 11! = 39916800 has two zeroes at the end.
// Given an integer k, return the number of non-negative integers x have the property that f(x) = k.

 

// Example 1:

// Input: k = 0
// Output: 5
// Explanation: 0!, 1!, 2!, 3!, and 4! end with k = 0 zeroes.
// Example 2:

// Input: k = 5
// Output: 0
// Explanation: There is no x such that x! ends in k = 5 zeroes.
// Example 3:

// Input: k = 3
// Output: 5
 

// Constraints:

// 0 <= k <= 10^9


class Solution {
public:
    int preimageSizeFZF(int k) {
        long start = 1;
        long end = 1;
        while (calculateZero(end) <= k) {
            end *= 2;
        }

        while (start < end) {
            long middle = (end - start) / 2 + start;
            if (calculateZero(middle) < k) {
                start = middle + 1;
            } else if (calculateZero(middle) > k) {
                end = middle - 1;
            } else {
                return 5;
            }
        }
        return 0;
    }

    int calculateZero(long n) {
        int sum = 0;
        while (n != 0) {
            n /= 5;
            sum += n;
        }
        return sum;
    }
};

int main() {
    Solution s;
    vector<tuple<int, int>> test_cases {
        {0, 5},
        {5, 0},
        {3, 5},
    };

    for (auto& test_case: test_cases) {
        assert(s.preimageSizeFZF(get<0>(test_case)) == get<1>(test_case));
    }
}