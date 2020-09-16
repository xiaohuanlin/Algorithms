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
#include <queue>
using namespace std;


// Given an array, strs, with strings consisting of only 0s and 1s. Also two integers m and n.

// Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s. Each 0 and 1 can be used at most once.

 

// Example 1:

// Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
// Output: 4
// Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are "10","0001","1","0".
// Example 2:

// Input: strs = ["10","0","1"], m = 1, n = 1
// Output: 2
// Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".
 

// Constraints:

// 1 <= strs.length <= 600
// 1 <= strs[i].length <= 100
// strs[i] consists only of digits '0' and '1'.
// 1 <= m, n <= 100


class Solution {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        vector<vector<vector<int>>> dp(strs.size() + 1, 
            vector<vector<int>>(m+1, 
                vector<int>(n+1, 0)
            )
        );

        vector<pair<int, int>> str_num;
        for (auto s: strs) {
            str_num.push_back({
                count(s.begin(), s.end(), '0'),
                count(s.begin(), s.end(), '1')
            });
        }

        for (int i = 1; i < dp.size(); ++i) {
            for (int j = 0; j < m+1; ++j) {
                for (int k = 0; k < n+1; ++k) {
                    int m_num = str_num[i-1].first;
                    int n_num = str_num[i-1].second;
                    if (j - m_num >= 0 && k - n_num >= 0 ) {
                        dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-m_num][k-n_num] + 1);
                    } else {
                        dp[i][j][k] = dp[i-1][j][k];
                    }
                }
            }
        }
        return dp[dp.size()-1][m][n];
    }
};


int main() {
    vector<string> array {"10", "1", "0"};
    Solution s;
    cout << s.findMaxForm(array, 1, 1) << endl;
}
