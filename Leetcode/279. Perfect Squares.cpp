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


// Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

// Example 1:

// Input: n = 12
// Output: 3 
// Explanation: 12 = 4 + 4 + 4.
// Example 2:

// Input: n = 13
// Output: 2
// Explanation: 13 = 4 + 9.

class Solution {
public:
    int numSquares(int n) {
        vector<int> res(n+1, 0);
        for (int i = 1; i < n + 1; i++) {
            int min_value = INT32_MAX;
            for (int j = 1; j * j <= i; j++) {
                min_value = min(min_value, res[i - j*j] + 1);
            }
            res[i] = min_value;
        }
        return res.back();
    }
};


int main() {
    Solution s;
    cout << s.numSquares(13);
}
