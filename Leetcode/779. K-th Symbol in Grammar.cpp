#include <vector>
#include <stack>
#include <iostream>
#include <tuple>
#include <assert.h>
#include <algorithm>
using namespace std;


// We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

// For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
// Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.

 

// Example 1:

// Input: n = 1, k = 1
// Output: 0
// Explanation: row 1: 0
// Example 2:

// Input: n = 2, k = 1
// Output: 0
// Explanation:
// row 1: 0
// row 2: 01
// Example 3:

// Input: n = 2, k = 2
// Output: 1
// Explanation:
// row 1: 0
// row 2: 01
// Example 4:

// Input: n = 3, k = 1
// Output: 0
// Explanation:
// row 1: 0
// row 2: 01
// row 3: 0110
 

// Constraints:

// 1 <= n <= 30
// 1 <= k <= 2^n - 1

class Solution {
public:
    int kthGrammar(int n, int k) {
        // when we draw the picture of this tree, we can simply get the basic function
        // f(n+1, 2k) = 1 and f(n+1, 2k-1) = 0 when f(n, k) = 0
        // f(n+1, 2k) = 0 and f(n+1, 2k-1) = 1 when f(n, k) = 0
        // it also means that
        // f(n, k) = 1 - f(n-1, k/2) if k % 2 == 0
        // f(n, k) = f(n-1, k/2 + 1) if k % 2 == 1
        int res = 0;
        while (n > 1) {
            if (k % 2 == 0) {
                res = 1 - res;
            }
            k = (k + 1) / 2;
            n--;
        }
        return res;
    }
};

int main() {
    Solution s;
    vector<tuple<tuple<int, int>, int>> test_cases {
        {{1, 1}, 0},
        {{2, 1}, 0},
        {{2, 2}, 1},
        {{3, 1}, 0},
        {{3, 3}, 1},
        {{4, 5}, 1},
        {{4, 7}, 0},
    };

    for (auto& test_case: test_cases) {
        assert(s.kthGrammar(get<0>(get<0>(test_case)), get<1>(get<0>(test_case))) == get<1>(test_case));
    }
}