#include <vector>
#include <tuple>
#include <unordered_map>
#include <algorithm>
#include <assert.h>
using namespace std;

// You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

// Return a list of integers representing the size of these parts.

 

// Example 1:

// Input: s = "ababcbacadefegdehijhklij"
// Output: [9,7,8]
// Explanation:
// The partition is "ababcbaca", "defegde", "hijhklij".
// This is a partition so that each letter appears in at most one part.
// A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
// Example 2:

// Input: s = "eccbbbbdec"
// Output: [10]
 

// Constraints:

// 1 <= s.length <= 500
// s consists of lowercase English letters.

class Solution {
    enum {
        kInvalidPosition = -1
    };
public:
    vector<int> partitionLabels(string s) {
        using Start = int;
        using End = int;
        using Interval = pair<Start, End>;

        vector<Interval> intervals(26, {kInvalidPosition, kInvalidPosition});
        // collect all intervals of different alphabat
        for (int i = 0; i < s.size(); i++) {
            auto& interval = intervals[s[i] - 'a'];
            if (interval.first == kInvalidPosition) {
                interval.first = i;
            }
            interval.second = i;
        }

        // calculate the combine interval
        // sort the intervals first
        sort(intervals.begin(), intervals.end(), [] (Interval& a, Interval& b) {
            return a.first < b.first;
        });

        vector<int> res;
        Interval candidate {kInvalidPosition, kInvalidPosition};

        for (auto& interval : intervals) {
            if (candidate.first == kInvalidPosition) {
                // initial condition
                candidate = interval;
            } else if (candidate.first < interval.first && candidate.second > interval.first) {
                // interval is nested in the candidate interval, we update the candidate
                candidate.second = max(candidate.second, interval.second);
            } else {
                // get the right candidate, push it into the result.
                res.push_back(candidate.second - candidate.first + 1);
                candidate = interval;
            }
        }
        if (candidate.first != kInvalidPosition) {
            res.push_back(candidate.second - candidate.first + 1);
        }
        return res;
    }
};

int main() {
    Solution s;
    vector<tuple<string, vector<int>>> test_cases {
        {"ababcbacadefegdehijhklij", {9, 7, 8}},
        {"eccbbbbdec", {10}},
        {"a", {1}},
        {"abcd", {1, 1, 1, 1}},
    };

    for (auto& test_case: test_cases) {
        assert(s.partitionLabels(get<0>(test_case)) == get<1>(test_case));
    }
}