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


// Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

// You may assume that the intervals were initially sorted according to their start times.

 

// Example 1:

// Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
// Output: [[1,5],[6,9]]
// Example 2:

// Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
// Output: [[1,2],[3,10],[12,16]]
// Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
// Example 3:

// Input: intervals = [], newInterval = [5,7]
// Output: [[5,7]]
// Example 4:

// Input: intervals = [[1,5]], newInterval = [2,3]
// Output: [[1,5]]
// Example 5:

// Input: intervals = [[1,5]], newInterval = [2,7]
// Output: [[1,7]]
 

// Constraints:

// 0 <= intervals.length <= 104
// intervals[i].length == 2
// 0 <= intervals[i][0] <= intervals[i][1] <= 105
// intervals is sorted by intervals[i][0] in ascending order.
// newInterval.length == 2
// 0 <= newInterval[0] <= newInterval[1] <= 105


class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        vector<vector<int>> res;        
        vector<int> tmp(2, 0);
        bool merge_start = false;
        bool merge_done = false;

        for (auto &e: intervals) {
            if (merge_done) {
                res.push_back(e);
                continue;
            }

            if (merge_start) {
                if (tmp[1] < e[0]) {
                    // done before this interval
                    res.push_back(tmp);
                    res.push_back(e);
                    merge_start = false;
                    merge_done = true;
                } else {
                    // could be longer
                    tmp[1] = max(e[1], tmp[1]);
                }
            } else {
                if (e[1] < newInterval[0]) {
                    // e is in left side of newInterval
                    res.push_back(e);
                } else if (e[0] > newInterval[1]) {
                    // e is in right side of newInterval
                    res.push_back(newInterval);
                    res.push_back(e);
                    merge_done = true;
                } else { 
                    // e is overlaped with newInterval
                    tmp[0] = min(e[0], newInterval[0]);
                    tmp[1] = max(e[1], newInterval[1]);
                    merge_start = true;
                }
            }
        }

        if (merge_start) {
            res.push_back(tmp);
            merge_done = true;
        }

        if (!merge_done) {
            res.push_back(newInterval);
        }

        return res;
    }
};

int main() {
}
