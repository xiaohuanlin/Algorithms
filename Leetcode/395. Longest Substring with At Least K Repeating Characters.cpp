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


// Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

// Example 1:

// Input:
// s = "aaabb", k = 3

// Output:
// 3

// The longest substring is "aaa", as 'a' is repeated 3 times.
// Example 2:

// Input:
// s = "ababbc", k = 2

// Output:
// 5

// The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.


class Solution {
public:
    int longestSubstring(string s, int k) {
        return core(s, 0, s.length(), k);
    }

    int core(string &s, int start, int end, int k) {
        vector<vector<int>> index(26, vector<int>());
        for (int i = start; i < end; i++) {
            index[s[i] - 'a'].push_back(i);
        }

        vector<int> res;
        for (int j = 0; j < index.size(); j++) {
            if (index[j].size() > 0 && index[j].size() < k) {
                res.insert(res.end(), index[j].begin(), index[j].end());
            }
        }
        if (res.empty()) {
            return end - start;
        }

        res.insert(res.end(), {start - 1, end});
        sort(res.begin(), res.end());

        vector<pair<int, int>> intervals;
        for (int m = res.size() - 1; m > 0; m--) {
            intervals.push_back(make_pair(res[m-1]+1, res[m]));
        }
        sort(intervals.begin(), intervals.end(), [] (pair<int, int> &a, pair<int, int> &b) {
            return a.second - a.first > b.second - b.first; 
        });

        int max_value = 0;
        for (int l = 0; l < intervals.size(); l++)  {
            if (max_value < intervals[l].second- intervals[l].first) {
                max_value = max(max_value, core(s, intervals[l].first, intervals[l].second, k));
            }
        }
        return max_value;
    }

};

int main() {
    Solution s;
    cout << s.longestSubstring("ibbicccccizzzktttt", 3);
}
