#include <stack>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;

// You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.

// Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c. Chain of pairs can be formed in this fashion.

// Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. You can select pairs in any order.

// Example 1:
// Input: [[1,2], [2,3], [3,4]]
// Output: 2
// Explanation: The longest chain is [1,2] -> [3,4]
// Note:
// The number of given pairs will be in the range [1, 1000].

class Solution {
public:
    int findLongestChain(vector<vector<int>>& pairs) {
        sort(pairs.begin(), pairs.end());

        int last = pairs[0][1];
        int res = 1;
        for (int i = 1; i < pairs.size(); ++i) {
            if (pairs[i][0] > last) {
                // change the last value
                last = pairs[i][1];
                res++;
            } else {
                if (pairs[i][1] < last) {
                    // make the scope smaller
                    last = pairs[i][1];
                }
            }
        }
        return res;
    }
};

int main() {
    vector<vector<int>> array {
        {-10, -8},
        {8, 9},
        {-5, 0},
        {6, 10},
        {-6, -4},
        {1, 7},
        {9, 10},
        {-4, 7},
    };
    Solution s;
    cout << s.findLongestChain(array) << endl;
}