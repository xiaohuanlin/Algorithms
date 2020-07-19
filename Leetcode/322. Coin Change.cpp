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

// You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

// Example 1:

// Input: coins = [1, 2, 5], amount = 11
// Output: 3 
// Explanation: 11 = 5 + 5 + 1
// Example 2:

// Input: coins = [2], amount = 3
// Output: -1
// Note:
// You may assume that you have an infinite number of each kind of coin.


class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
		if (amount == 0) {
			return 0;
		}
		vector<int> dp(amount+1, 0);
		for (int i = 0; i < amount+1; i++) {
			int min_value = INT32_MAX;
			for (int j = 0; j < coins.size(); j++) {
				if (i == coins[j]) {
					dp[i] = 1;
				} else if (i >= coins[j] && dp[i - coins[j]] > 0 && dp[i - coins[j]] < min_value) {
					min_value = dp[i - coins[j]];
				}
			}
			if (min_value == INT32_MAX || dp[i] != 0) {
				continue;
			}
			dp[i] = min_value + 1;
		}
		return dp[amount] == 0 ? -1: dp[amount];
	}
};


int main() {
	Solution s;
	vector<int> array = {1,2};
	cout << s.coinChange(array, 2);
}