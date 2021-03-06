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


// Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

// Example 1:

// Input: 2
// Output: 1
// Explanation: 2 = 1 + 1, 1 × 1 = 1.
// Example 2:

// Input: 10
// Output: 36
// Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
// Note: You may assume that n is not less than 2 and not larger than 58.

class Solution {
public:
    int integerBreak(int n) {
        vector<int> dp(n+1, 1);
        for (int i = 3; i < n+1; i++) {
            for (int j = 1; j < i; j++) {
                dp[i] = max(dp[i], max(dp[j], j) * (i - j));
            }
        }
        return dp[n];
    }
}; 

int main() {
    Solution s;
    cout << s.integerBreak(10);
}