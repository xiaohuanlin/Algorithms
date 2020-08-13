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
#include <iterator>
using namespace std;


// Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

 

// Example 1:

// Input: [[1,2],[2,3],[3,4],[1,3]]
// Output: 1
// Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
// Example 2:

// Input: [[1,2],[1,2],[1,2]]
// Output: 2
// Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
// Example 3:

// Input: [[1,2],[2,3]]
// Output: 0
// Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 

// Note:

// You may assume the interval's end point is always bigger than its start point.
// Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.

class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), [] (vector<int> &a, vector<int> &b) {
            return a[1] < b[1];
        });

        vector<tuple<int, int>> dp(intervals.size() + 1, {INT32_MIN, 0});       
        for (int i = 1; i < intervals.size() + 1; ++i) {
            dp[i] = dp[i-1];
            if (get<0>(dp[i-1]) <= intervals[i-1][0]) {
                dp[i] = make_tuple(intervals[i-1][1], get<1>(dp[i]) + 1);
            }
        }
        return intervals.size() - get<1>(dp[intervals.size()]);
    }
};


int main() {
    Solution s;
    vector<vector<int>> array {{1,2}, {2,7}, {3,4}, {4,5}};
    cout << s.eraseOverlapIntervals(array);
}