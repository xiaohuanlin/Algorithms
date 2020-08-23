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


// Given a set of intervals, for each of the interval i, check if there exists an interval j whose start point is bigger than or equal to the end point of the interval i, which can be called that j is on the "right" of i.

// For any interval i, you need to store the minimum interval j's index, which means that the interval j has the minimum start point to build the "right" relationship for interval i. If the interval j doesn't exist, store -1 for the interval i. Finally, you need output the stored value of each interval as an array.

// Note:

// You may assume the interval's end point is always bigger than its start point.
// You may assume none of these intervals have the same start point.
 

// Example 1:

// Input: [ [1,2] ]

// Output: [-1]

// Explanation: There is only one interval in the collection, so it outputs -1.
 

// Example 2:

// Input: [ [3,4], [2,3], [1,2] ]

// Output: [-1, 0, 1]

// Explanation: There is no satisfied "right" interval for [3,4].
// For [2,3], the interval [3,4] has minimum-"right" start point;
// For [1,2], the interval [2,3] has minimum-"right" start point.
 

// Example 3:

// Input: [ [1,4], [2,3], [3,4] ]

// Output: [-1, 2, -1]

// Explanation: There is no satisfied "right" interval for [1,4] and [3,4].
// For [2,3], the interval [3,4] has minimum-"right" start point.
// NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.


class Solution {
public:
    vector<int> findRightInterval(vector<vector<int>>& intervals) {
        vector<pair<int,int>> sorted_ans;
        vector<int> res;
        if (intervals.empty()) {
            return res;
        }

        for (int i = 0; i < intervals.size(); ++i) {
            sorted_ans.push_back({intervals[i][0], i});
        }

        sort(sorted_ans.begin(), sorted_ans.end());

        for (int i = 0; i < intervals.size(); ++i) {
            res.push_back(binary_search_core(sorted_ans, intervals[i][1]));
        }
        return res;
    }

    int binary_search_core(vector<pair<int,int>> &ans, int value) {
        int start = 0;
        int end = ans.size() - 1;
        while (start < end) {
            int middle = start + (end - start) / 2;
            if (value > ans[middle].first) {
                start = middle + 1;
            } else if (value == ans[middle].first) {
                return ans[middle].second;
            } else {
                end = middle;
            }
        }

        return value <= ans[start].first ? ans[start].second: -1;
    }
};


int main() {
    Solution s;
    vector<vector<int>> array {
        {1,2},
        {2,3},
        {0,1},
        {3,4},
    };
    auto res = s.findRightInterval(array);

    for (auto e: res) {
        cout << e << ',';
    }
    cout << endl;
}