#include <stack>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;

// Given a collection of intervals, merge all overlapping intervals.

// Example 1:

// Input: [[1,3],[2,6],[8,10],[15,18]]
// Output: [[1,6],[8,10],[15,18]]
// Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
// Example 2:

// Input: [[1,4],[4,5]]
// Output: [[1,5]]
// Explanation: Intervals [1,4] and [4,5] are considered overlapping.
// NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.


class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());
        vector<vector<int>> res;
        if (intervals.empty()) {
            return res;
        }

        res.push_back(vector<int>(intervals[0]));
        for (int i = 1; i < intervals.size(); i++) {
            auto last_item = res[res.size() - 1];
            if (intervals[i][0] >= last_item[0] && intervals[i][0] <= last_item[1]) {
                vector<int> new_item;
                new_item.push_back(last_item[0]);
                new_item.push_back(intervals[i][1] > last_item[1] ? intervals[i][1]: last_item[1]);
                    
                res.pop_back();
                res.push_back(vector<int>(new_item));
            } else {
                res.push_back(vector<int>(intervals[i]));
            }
        }
        return res;
    }
};

int main() {
    Solution s;
    vector<vector<int>> array = {
        {4, 2},
        {3, 6},
        {8, 11}
    };
    auto res = s.merge(array);
    for (auto e : res) {
        for (auto l : e) {
            cout << l << ',';
        }
        cout << endl;
    }
}
